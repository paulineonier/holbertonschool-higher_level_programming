#!/usr/bin/python3
import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the file to save the serialized data.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, "item")
        key_element = ET.SubElement(item, "key")
        key_element.text = str(key)
        value_element = ET.SubElement(item, "value")
        value_element.text = str(value)

    tree = ET.ElementTree(root)
    try:
        tree.write(filename)
        return True
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")
        return False

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The name of the file to read the serialized data from.

    Returns:
    dict: The deserialized dictionary.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        dictionary = {}
        for item in root.findall('item'):
            key = item.find('key').text
            value = item.find('value').text
            # Attempt to handle data type conversion
            if value.isdigit():
                value = int(value)
            elif value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            else:
                try:
                    value = float(value)
                except ValueError:
                    pass
            dictionary[key] = value

        return dictionary
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None
    except ET.ParseError as e:
        print(f"An error occurred while parsing the XML file: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
