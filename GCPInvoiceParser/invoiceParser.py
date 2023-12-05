from google.cloud import documentai
from google.api_core.client_options import ClientOptions
from google.api_core.client_options import ClientOptions
from google.api_core.exceptions import FailedPrecondition


import os
import pandas as pd
import inspect

from typing import Optional, Sequence
from functions import *

class InvoiceParser:
    def __init__(
        self, project_id, document_type, document_path, mime_type,version,processor_id,processor_type,processor_name,location="eu"
    ):
        self.client = documentai.DocumentProcessorServiceClient(client_options={'api_endpoint': f'{location}-documentai.googleapis.com'})
        self.project_id = project_id
        self.document_type = document_type
        self.document_path = document_path
        self.mime_type = mime_type
        self.location = location
        self.version = version
        self.processor_id = processor_id
        self.processor_type = processor_type
        self.processor_name = processor_name

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    #Save 
    def saveDocumentOCR(document) -> None:
        pass
    def saveDocumentInvoice(self,dataFrame) -> bool:
        print(dataFrame)
        return True
    
    #Update
    def editProcessedDocument(document) -> None:
        pass
    
    #Processor methods
    def enableProcessor(self) -> None:
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        client = documentai.DocumentProcessorServiceClient(client_options=opts)

        processor_name = client.processor_path(self.project_id, self.location, self.processor_id)
        request = documentai.EnableProcessorRequest(name=processor_name)

        try:
            operation = client.enable_processor(request=request)

           
            print(f"{style.GREEN}{operation.operation.name} - Enabling {style.RESET}")
            operation.result()
        # Cannot disable a processor that is already disabled
        except FailedPrecondition as e:
            print(style.RED  + e.message + style.RESET) 
    
    def disableProcessor(self) -> None:
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        client = documentai.DocumentProcessorServiceClient(client_options=opts)

        processor_name = client.processor_path(self.project_id, self.location, self.processor_id)
        request = documentai.DisableProcessorRequest(name=processor_name)

        try:
            operation = client.disable_processor(request=request)

           
            print(f"{style.GREEN}{operation.operation.name} - Disabling {style.RESET}")
            operation.result()
        # Cannot disable a processor that is already disabled
        except FailedPrecondition as e:
            print(style.RED  + e.message + style.RESET) 

    
    def listProcessorDetails(self) -> None:
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        client = documentai.DocumentProcessorServiceClient(client_options=opts)
        parent = client.common_location_path(self.project_id, self.location)

        processor_list = client.list_processors(parent=parent)

        for processor in processor_list:
            print(f"{style.ORANGE}Processor Name: {processor.name}")
            print(f"Processor Display Name: {processor.display_name}")
            print(f"Processor Type: {processor.type_}")
            print(f"{style.RESET}")

    def getProcessorSchema(self):
        client = self.client

        processor_name = f"projects/{self.project_id}/locations/eu/processors/{self.processor_id}"
        processor = client.get_processor(name=processor_name)

        schema = processor
        print(f"Processor Schema: {schema}")
        return schema

    #Processors
    def processDocumentOCR_v1(self) -> None:
        process_options = documentai.ProcessOptions(
            ocr_config=documentai.OcrConfig(
                enable_native_pdf_parsing=True,
                enable_image_quality_scores=True,
                enable_symbol=True,
            
                premium_features=documentai.OcrConfig.PremiumFeatures(
                    compute_style_info=False,
                    enable_math_ocr=False,
                    enable_selection_mark_detection=False,
                ),
            )
        )
        if(self.processor_type == "INVOICE_PARSER"):
            print(inspect.stack()[-1].code_context[0].strip(), 'is not able to process an INVOICE_PARSER processor.')
            return False
        
        document = processDocument(
            self.project_id,
            self.location,
            self.processor_id,
            self.version,
            self.document_path,
            self.mime_type,
            process_options=process_options,
        )

        text = document.text
        print(f"Full document text: {text}\n")
        print(f"There are {len(document.pages)} page(s) in this document.\n")

        for page in document.pages:
            print(f"Page {page.page_number}:")
            printPageDimensions(page.dimension)
            printDetectedLanguages(page.detected_languages)

            printBlocks(page.blocks, text)
            printParagraphs(page.paragraphs, text)
            printLines(page.lines, text)
            printTokens(page.tokens, text)

            if page.symbols:
                printSymbols(page.symbols, text)

            if page.image_quality_scores:
                printImageQualityScores(page.image_quality_scores)

            if page.visual_elements:
                printVisualElements(page.visual_elements, text)
                
    def processInvoiceParser_v1(self) -> None:
       
        client_options = {"api_endpoint": f"{self.location}-documentai.googleapis.com"}
        client = documentai.DocumentProcessorServiceClient(client_options=client_options)
        name = f"projects/{self.project_id}/locations/{self.location}/processors/{self.processor_id}"

        with open(self.document_path, "rb") as invoice:
            invoice_content = invoice.read()

       
        document = {"content": invoice_content, "mime_type": "application/pdf"}
        request = {"name": name, "raw_document": document}

       
        result = client.process_document(request=request)
        document = result.document
        entities = document.entities
        print(f"{style.BLUE}Document reading complete.{style.RESET}\n\n")

    
        types = []
        values = []
        confidence = []
        
        for entity in entities:
            types.append(entity.type_)
            values.append(entity.mention_text)
            confidence.append(round(entity.confidence,4))
            
    
        df = pd.DataFrame({'Type': types, 'Value': values, 'Confidence': confidence})
        # print(document) - for vertex improvement
        humanProcess = humanProcessInfo(result)
        return df