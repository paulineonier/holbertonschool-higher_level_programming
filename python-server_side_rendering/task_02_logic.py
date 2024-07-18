import json

def load_items_from_json(file_path):
    """
    Charge les items à partir d'un fichier JSON.
    
    Args:
        file_path (str): Le chemin vers le fichier JSON.
        
    Returns:
        list: Une liste d'items.
    """
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            return data.get("items", [])
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
