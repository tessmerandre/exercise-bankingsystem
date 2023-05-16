import json

def read_json(file_path):
    """
    Read data from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The loaded JSON data as a dictionary.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        json.JSONDecodeError: If there is an error decoding the JSON data.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def write_json(file_path, data):
    """
    Write data to a JSON file.

    Args:
        file_path (str): The path to the JSON file.
        data (dict): The data to be written as a dictionary.
    """
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)