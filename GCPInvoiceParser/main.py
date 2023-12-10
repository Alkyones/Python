# import pandas as pd // first learn how to read document we will come here later xD
from invoiceParser import InvoiceParser
import os
import json


if __name__ == "__main__":

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './credentials.json'


    with open("./creds.json", 'r') as file:
        credentials = json.load(file)


    InvoiceParserInit = InvoiceParser(
        credentials["PROJECT_ID"],
        credentials["DOCUMENT_TYPE"],
        credentials["DOCUMENT_PATH"],
        credentials["MIME_TYPE"],
        credentials["PROCESSOR_VERSION"],
        credentials["PROCESSOR_ID"],
        credentials["PROCESSOR_TYPE"],
        credentials["PROCESSOR_NAME"],
        credentials["LOCATION"]
        )
    
 
    
    
    #* COMPLETED
    listProcessors = InvoiceParserInit.listProcessorDetails()
    
    #* COMPLETED - Enable Processor
    # enableProcessor = InvoiceParserInit.enableProcessor()
    #* COMPLETED - Disable Processor
    # disableProcessor = InvoiceParserInit.disableProcessor()
    
    #* COMPLETED - Active processor schema
    # schemaProcessor = InvoiceParserInit.getProcessorSchema()

    #* COMPLETED
    # readDocument = InvoiceParserInit.processDocumentOCR_v1()
    
    #TODO CREATE TRAIN FUNCTION FOR RECEIVED DOCUMENT
    
    #* COMPLETED
    readInvoice = InvoiceParserInit.processInvoiceParser_v1()
    # #TODO CREATE SAVE FUNCTION FOR RECEIVED DOCUMENT
    saveInvoice = InvoiceParserInit.saveDocumentInvoice(readInvoice)
    
    
    #TODO IMPLEMENT PIPELINE TO COMPANY TO CREATE OFFER AND INVOICE
    #pipeline