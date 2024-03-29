import yaml
from housing.exception import HousingException
import os,sys 



def read_yaml_file(file_path:str) -> dict:
    """
    This function takes yaml file path as input and return file content
    """
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException()