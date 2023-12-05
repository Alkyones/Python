from google.cloud import documentai
from google.api_core.client_options import ClientOptions

from typing import Optional, Sequence
from functions import *

class InvoiceParser:
    def __init__(
        self, project_id, document_type, document_path, mime_type,version,processor_id,location="eu"
    ):
        self.project_id = project_id
        self.document_type = document_type
        self.document_path = document_path
        self.mime_type = mime_type
        self.client = documentai.DocumentProcessorServiceClient()
        self.location = location
        self.version = version
        self.processor_id = processor_id

    def listProcessorDetails(self) -> None:
        opts = ClientOptions(api_endpoint=f"{self.location}-documentai.googleapis.com")
        client = documentai.DocumentProcessorServiceClient(client_options=opts)
        parent = client.common_location_path(self.project_id, self.location)

        processor_list = client.list_processors(parent=parent)

        for processor in processor_list:
            print(f"Processor Name: {processor.name}")
            print(f"Processor Display Name: {processor.display_name}")
            print(f"Processor Type: {processor.type_}")
            print("")


    def processInvoice_v1(self):
        with open(self.document_path, "rb") as pdf_file:
            content = pdf_file.read()
        document = documentai.types.Document(content=content)

        request = documentai.types.ProcessRequest(
            name=f"projects/{self.project_id}/locations/us/processors/{self.document_type}",
            raw_document=documentai.types.RawDocument(content=content),
        )
        result = self.client.process_document(request=request)
        extracted_data = {}
        for entity in result.document.entities:
            extracted_data[entity.type_] = entity.mention_text
        return extracted_data

    
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
    
        document = process_document(
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
            print_page_dimensions(page.dimension)
            print_detected_langauges(page.detected_languages)

            print_blocks(page.blocks, text)
            print_paragraphs(page.paragraphs, text)
            print_lines(page.lines, text)
            print_tokens(page.tokens, text)

            if page.symbols:
                print_symbols(page.symbols, text)

            if page.image_quality_scores:
                print_image_quality_scores(page.image_quality_scores)

            if page.visual_elements:
                print_visual_elements(page.visual_elements, text)
                
    def saveDocumentOCR(document) -> None:
        pass
    def saveDocumentInvoice(invoice) -> None:
        pass
    
    def editProcessedDocument(document) -> None:
        pass