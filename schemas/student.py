from typing import Optional


def get_value(data: dict, key: str, default=None) -> Optional[str]:
    """Retrieves a value from a nested dictionary, returning None if not found."""
    try:
        return data[key]
    except KeyError:
        return default


def student_entity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item.get("name", item["name"]),  # Use existing name if not provided
        "age": item.get("age", item["age"]),  # Use existing age if not provided
        "address": {
            "city": get_value(item["address"], "city"),  # Use existing city
            "country": get_value(item["address"], "country"),  # Use existing country
        }
    }
