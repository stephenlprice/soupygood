import re, json

def info(soup):
    """
    Parses HTML content and extracts information into a 'dataLayer' data object.

    Args:
        soup (BeautifulSoup): The BeautifulSoup object representing the HTML content.

    Returns:
        str or None: The extracted dataLayer as a string, or None if not found.

    Note:
        The function looks for a script tag containing '__DATA_LAYER__' and extracts
        the content as a JSON-formatted string.

    Raises:
        None: No specific exceptions are raised by this function.
    """
    # stores target data object from HTML response
    target = None

    dataLayer = None
    # site responds with fully formed HTML and data in script tag
    script_tag = soup.find('script', text=lambda text: text and '__DATA_LAYER__' in text)
    # extract the content of the script as a string
    data_layer_content = script_tag.text.strip() if script_tag else None
    # remove window assignment
    left_trim = data_layer_content.lstrip('window.__DATA_LAYER__ = ')
    # regex to match everything before and including the first `};` to keep only valid json
    pattern = re.compile(r"(.*?};)")
    # search for the regex in the provided code
    match = pattern.search(left_trim)

    if match:
        # remove trailing semicolon
        dataLayer = match.group(1).rstrip(';')
        parsed_json = json.loads(dataLayer)
        print(type(parsed_json))
        for key in parsed_json.keys():
            print(key)

        data = parsed_json["dataLayerLoader"]["dataLayer"]["info"]
        target = data
    else:
        print("dataLayer not found.")

    print(target)
    return target
