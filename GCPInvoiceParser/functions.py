from google.cloud import documentai
from typing import Optional, Sequence
from google.api_core.client_options import ClientOptions

class style():
  RED = '\033[31m'
  ORANGE= '\033[33m'
  GREEN = '\033[32m'
  BLUE = '\033[34m'
  RESET = '\033[0m'

def printPageDimensions(dimension: documentai.Document.Page.Dimension) -> None:
    print(f"    Width: {str(dimension.width)}")
    print(f"    Height: {str(dimension.height)}")


def printDetectedLanguages(
    detected_languages: Sequence[documentai.Document.Page.DetectedLanguage],
) -> None:
    print("    Detected languages:")
    for lang in detected_languages:
        print(f"        {lang.language_code} ({lang.confidence:.1%} confidence)")


def printBlocks(blocks: Sequence[documentai.Document.Page.Block], text: str) -> None:
    print(f"    {len(blocks)} blocks detected:")
    first_block_text = layoutToText(blocks[0].layout, text)
    print(f"        First text block: {repr(first_block_text)}")
    last_block_text = layoutToText(blocks[-1].layout, text)
    print(f"        Last text block: {repr(last_block_text)}")


def printParagraphs(
    paragraphs: Sequence[documentai.Document.Page.Paragraph], text: str
) -> None:
    print(f"    {len(paragraphs)} paragraphs detected:")
    first_paragraph_text = layoutToText(paragraphs[0].layout, text)
    print(f"        First paragraph text: {repr(first_paragraph_text)}")
    last_paragraph_text = layoutToText(paragraphs[-1].layout, text)
    print(f"        Last paragraph text: {repr(last_paragraph_text)}")


def printLines(lines: Sequence[documentai.Document.Page.Line], text: str) -> None:
    print(f"    {len(lines)} lines detected:")
    first_line_text = layoutToText(lines[0].layout, text)
    print(f"        First line text: {repr(first_line_text)}")
    last_line_text = layoutToText(lines[-1].layout, text)
    print(f"        Last line text: {repr(last_line_text)}")


def printTokens(tokens: Sequence[documentai.Document.Page.Token], text: str) -> None:
    print(f"    {len(tokens)} tokens detected:")
    first_token_text = layoutToText(tokens[0].layout, text)
    first_token_break_type = tokens[0].detected_break.type_.name
    print(f"        First token text: {repr(first_token_text)}")
    print(f"        First token break type: {repr(first_token_break_type)}")
    if tokens[0].style_info:
        printStyleInfo(tokens[0].style_info)

    last_token_text = layoutToText(tokens[-1].layout, text)
    last_token_break_type = tokens[-1].detected_break.type_.name
    print(f"        Last token text: {repr(last_token_text)}")
    print(f"        Last token break type: {repr(last_token_break_type)}")
    if tokens[-1].style_info:
        printStyleInfo(tokens[-1].style_info)


def printSymbols(
    symbols: Sequence[documentai.Document.Page.Symbol], text: str
) -> None:
    print(f"    {len(symbols)} symbols detected:")
    first_symbol_text = layoutToText(symbols[0].layout, text)
    print(f"        First symbol text: {repr(first_symbol_text)}")
    last_symbol_text = layoutToText(symbols[-1].layout, text)
    print(f"        Last symbol text: {repr(last_symbol_text)}")


def printImageQualityScores(
    image_quality_scores: documentai.Document.Page.ImageQualityScores,
) -> None:
    print(f"    Quality score: {image_quality_scores.quality_score:.1%}")
    print("    Detected defects:")

    for detected_defect in image_quality_scores.detected_defects:
        print(f"        {detected_defect.type_}: {detected_defect.confidence:.1%}")


def printStyleInfo(style_info: documentai.Document.Page.Token.StyleInfo) -> None:
 
    print(f"           Font Size: {style_info.font_size}pt")
    print(f"           Font Type: {style_info.font_type}")
    print(f"           Bold: {style_info.bold}")
    print(f"           Italic: {style_info.italic}")
    print(f"           Underlined: {style_info.underlined}")
    print(f"           Handwritten: {style_info.handwritten}")
    print(
        f"           Text Color (RGBa): {style_info.text_color.red}, {style_info.text_color.green}, {style_info.text_color.blue}, {style_info.text_color.alpha}"
    )


def printVisualElements(
    visual_elements: Sequence[documentai.Document.Page.VisualElement], text: str
) -> None:
    checkboxes = [x for x in visual_elements if "checkbox" in x.type]
    math_symbols = [x for x in visual_elements if x.type == "math_formula"]

    if checkboxes:
        print(f"    {len(checkboxes)} checkboxes detected:")
        print(f"        First checkbox: {repr(checkboxes[0].type)}")
        print(f"        Last checkbox: {repr(checkboxes[-1].type)}")

    if math_symbols:
        print(f"    {len(math_symbols)} math symbols detected:")
        first_math_symbol_text = layoutToText(math_symbols[0].layout, text)
        print(f"        First math symbol: {repr(first_math_symbol_text)}")


def processDocument(
    project_id: str,
    location: str,
    processor_id: str,
    processor_version: str,
    file_path: str,
    mime_type: str,
    process_options: Optional[documentai.ProcessOptions] = None,
) -> documentai.Document:
    client = documentai.DocumentProcessorServiceClient(
        client_options=ClientOptions(
            api_endpoint=f"{location}-documentai.googleapis.com"
        )
    )

    name = client.processor_version_path(
        project_id, location, processor_id, processor_version
    )

    # Read the file into memory
    with open(file_path, "rb") as image:
        image_content = image.read()

    # Configure the process request
    request = documentai.ProcessRequest(
        name=name,
        raw_document=documentai.RawDocument(content=image_content, mime_type=mime_type),
        process_options=process_options,
    )

    result = client.processDocument(request=request)
    return result.document


def layoutToText(layout: documentai.Document.Page.Layout, text: str) -> str:
    
    return "".join(
        text[int(segment.start_index) : int(segment.end_index)]
        for segment in layout.text_anchor.text_segments
    )


def getText(doc_element: dict, document: dict):
    
    response = ""

    for segment in doc_element.text_anchor.text_segments:
        start_index = (
            int(segment.start_index)
            if segment in doc_element.text_anchor.text_segments
            else 0
        )
        end_index = int(segment.end_index)
        response += document.text[start_index:end_index]
    return response

def humanProcessInfo(input) -> None:
    strInput = str(input.human_review_status.state_message)
    print(f"{style.BLUE}Document processing complete.")
    print(f"Human Process information: {style.RESET}")
    if "DISABLED" in strInput: 
        inputArray = strInput.split(" ")
        newOutput = []
        for word in inputArray:
            if word != "DISABLED,":
                newOutput.append(word)
            else:
                newOutput.append(f"{style.RED}{word[:-1]}{style.RESET}{style.GREEN}")
        newOutput = ' '.join(newOutput)
        print("\t", f"{style.GREEN}{newOutput}{style.RESET}")    
    else:    
        print("\t", f"{style.GREEN}{strInput}{style.RESET}")
    print("\n")