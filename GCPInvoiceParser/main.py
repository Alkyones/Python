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
        credentials["LOCATION"]
        )
    
    #TODO V1 needs more debugging
    # extracted_data = InvoiceParserInit.processInvoice_v1()
    # print("Extracted Data:")
    # for key, value in extracted_data.items():
    #     print(f"{key}: {value}")
    
    
    #* COMPLETED
    listProcessors = InvoiceParserInit.listProcessorDetails()

    readInvoice = InvoiceParserInit.processDocumentOCR_v1()