import requests
from bs4 import BeautifulSoup

def soup(url, vid):
    """
    Retrieves and parses HTML content from a specified URL and returns a BeautifulSoup object.

    Args:
        url (str): The base URL for the web scraping.

    Returns:
        BeautifulSoup: A BeautifulSoup object representing the parsed HTML content.

    Note:
        The function appends a specific identifier to the provided URL
        to target a specific page for scraping.

        It uses the 'requests' library to make a GET request to the constructed URL
        and then utilizes BeautifulSoup to parse the HTML content.

    Raises:
        requests.exceptions.RequestException: If there is an issue with the HTTP request.
        Exception: Any other exceptions that might occur during the request or parsing process.
    """
    
    # Construct the URL with the specific vehicle identifier
    endpoint = url + vid

    try:
        # Make a GET request to the constructed URL
        response = requests.get(endpoint)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup

    except requests.exceptions.RequestException as e:
        print(f"Error making HTTP request: {e}")
        raise e
    except Exception as e:
        print(f"Error parsing HTML content: {e}")
        raise e
