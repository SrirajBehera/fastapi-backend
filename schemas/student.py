from typing import Optional

def get_value(data: dict, key: str, default=None) -> Optional[str]:
    """
    Retrieves a value from a nested dictionary, returning the default value if the key is not found.

    Args:
        data (dict): The dictionary to retrieve the value from.
        key (str): The key to search for in the dictionary.
        default (Optional[Any]): The default value to return if the key is not found. Defaults to None.

    Returns:
        Optional[str]: The value associated with the given key, or the default value if the key is not found.
    """
    try:
        return data[key]
    except KeyError:
        return default


def student_entity(item) -> dict:
    """
    Constructs a student entity dictionary from a MongoDB document.

    Args:
        item (dict): The MongoDB document representing a student.

    Returns:
        dict: A dictionary representation of the student entity, with the following keys:
            - "id": The ID of the student.
            - "name": The name of the student.
            - "age": The age of the student.
            - "address": A dictionary containing the city and country of the student's address.
    """
    return {
        "id": str(item["_id"]),
        "name": item.get("name", item["name"]),  # Use existing name if not provided
        "age": item.get("age", item["age"]),  # Use existing age if not provided
        "address": {
            "city": get_value(item["address"], "city"),  # Use existing city
            "country": get_value(item["address"], "country"),  # Use existing country
        }
    }
