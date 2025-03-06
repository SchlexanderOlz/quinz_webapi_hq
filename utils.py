import json

def pretty_print(json_data):
    """
    Pretty print JSON data.

    :param json_data: JSON data as a dictionary.
    """
    print(json.dumps(json_data, indent=4))
