
import os
from box import ConfigBox # for handling configurations as objects instead of dicts, 
                          # meaning we can access attributes like obj.attr instead of dict['attr']
from box.exceptions import BoxValueError # instead of writing my custom Exception messages.
from ensure import ensure_annotations # for type checking of function's arguments, and types of data it returns
from ChickenDisease import logger # that we can catch errors early in development not at runtime 
import json 
import joblib # for saving and loading binary files
import yaml # for reading and writing yaml files
from pathlib import Path # for handling file paths styles with ease across different OS, using '\' or '/'.
from typing import Any, Union # for type hinting
import base64 # for encoding and decoding binary data to/from base64 strings
              # convert images binary data to base64 strings for easy embedding in HTML or JSON
              # then convert base64 strings back to binary data for processing or storage
              # useful for data obfuscation, integrity checks, transmission over text-based protocols, storage in text-based formats,
              # and for data embedding in web pages or documents, serialization, deserialization, compression, encryption
              
# Utility functions for file operations and configurations
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns ConfigBox
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(msg=f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(msg=f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """save json data
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    with open(path, "w") as json_obj:
        json.dump(data, json_obj, indent=4)

    logger.info(msg=f"json file saved at: {path}")


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data
    Args:
        path (Path): path to json file
    Returns:
        Box: data as class attributes instead of dict
    """
    with open(path) as json_file:
        content = json.load(json_file)

    logger.info(msg=f"json file loaded succesfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file
    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(msg=f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    Args:
        path (Path): path to binary file
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(filename=path)
    logger.info(msg=f"binary file loaded from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_ = round(os.path.getsize(path)/1024)
    if size_ < 1024:
        return f"~ {size_} KB"
    return f"~ {round(size_/1024, 2)} MB"

@ensure_annotations
def decodeImage(img_string: str, filname: str) -> None:
    """Decode a base64 string and save it as an image file.
    Args:
        img_string (str): The base64 encoded string representing the image.
        filname (str): The path where the decoded image will be saved.
    """
    img_binaries = base64.b64decode(img_string)
    with open(filname, 'wb') as img_file:
        img_file.write(img_binaries)


@ensure_annotations
def encodeImage(img_path: str) -> str:
    """Encode an image file to a base64 string.
    Args:
        img_path (Union[str, Path]): The path to the image file to be encoded.
    Returns:
        str: The base64 encoded string representing the image.
    """
    with open(img_path, 'rb') as img_file:
        img_binaries = img_file.read()
        img_string = base64.b64encode(img_binaries).decode("utf-8")
    return img_string


