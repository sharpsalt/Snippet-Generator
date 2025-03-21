import os
import json

#here you can use your location for the file.txt as per your need
file_path = r"C:\Users\Srija\Codes\Web Development\Snippet Generator\file.txt"

try:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = [line.strip() for line in file if line.strip()]

        snippet_structure = {
            "": {
                "prefix": "",
                "body": lines,
                "description": ""
            }
        }

        snippet_json = json.dumps(snippet_structure, indent=2)
        print(snippet_json) 

    else:
        raise FileNotFoundError  # Raising an error if the file does not exist
except FileNotFoundError:
    print("File not found")
