from setuptools import setup,find_packages
from typing import List

# Declaring variables for setup function
Project_name="housing-predictor"
Name="housing-predictor"
version="0.0.1"
Author="Arup"
Description="This is the 1st ML project"
Packages= ["Housing"]
Requirement_file_name = "requirements.txt"


def get_requirements_list()->List[str]:
    '''
    This function gowing to return a list which will contain name of libreies 
    mention in requirements.txt 
    '''
    with open(Requirement_file_name) as requirement:
        return requirement.readlines().remove("-e .")
setup(
    name=Name,
    version=version,
    author=Author,
    description=Description,
    packages= find_packages(),#Packages,
    install_requires=get_requirements_list()

)
