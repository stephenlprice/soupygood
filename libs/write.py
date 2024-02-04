import os
import csv
import json

def file(input):
    """
    Writes input data to multiple files in the 'output' directory.

    Args:
        input (str): The input data to be written to files.

    Note:
        If the 'output' directory does not exist, it will be created.

        The input data is written to three different files:
        1. 'out/info.txt' - Raw input data as a string.
        2. 'out/info.csv' - Input data written as a single-row CSV file.
        3. 'out/info.json' - Prettified JSON representation of the input data.

    Raises:
        None: No specific exceptions are raised by this function.
    """
    if not os.path.exists('out'):
        os.makedirs('out')

    if input:
        # Write raw input data to a text file with UTF-8 encoding
        with open('out/info.txt', 'w', encoding='utf-8') as file:
            file.write(str(input))

        # Write the input data to a .csv file with UTF-8 encoding
        with open('out/info.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([input])

        # Assuming input is a JSON-formatted string, prettify and write to a .json file
        with open('out/info.json', 'w', encoding='utf-8') as file:
            prettified_json = json.dumps(input, indent=4)
            json.dump(input, file, indent=4)
            print(type(input))
            print(prettified_json)

    else:
        print('No input provided!')
