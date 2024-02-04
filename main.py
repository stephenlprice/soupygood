import os
from dotenv import load_dotenv
from libs import parse, query, write

load_dotenv()

env_vars = os.environ

# The URL from which information is scraped
URL = env_vars['URL']
V_ID = env_vars['V_ID']

def main():
    """
    Main script for scraping information from a specified URL, parsing it, and writing it to files.

    Note:
        The script uses the 'query.soup' function to retrieve and parse HTML content from the
        specified URL. The parsed information is then extracted using the 'parse.info' function,
        and finally, it is written to files using the 'write.file' function.

        The URL is loaded from the environment variable 'URL', which should be set in a
        '.env' file in the same directory as this script.

    Raises:
        EnvironmentError: If the 'URL' environment variable is not set.
        Exception: Any other exceptions that might occur during the scraping, parsing, or writing process.
    """
    # Retrieve and parse HTML content from the specified URL
    soup = query.soup(URL, V_ID)

    # Extract information from the parsed HTML content
    info = parse.info(soup)

    # Write the extracted information to files
    write.file(info)

if __name__ == "__main__":
    main()
