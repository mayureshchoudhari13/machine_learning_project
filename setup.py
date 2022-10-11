
from setuptools import setup , find_packages
from typing import List


# declaring variable for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Mayuresh Choudhari"
DESCRIPTION = "this is first ML project"
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines().remove("-e .")
       

setup(

    name=PROJECT_NAME ,
    version=VERSION ,
    author=AUTHOR ,
    description=DESCRIPTION ,
    packages= find_packages() , # it will return those folder which have __init_.py in it , that is pakages. like housing


    install_requires= get_requirements_list()
)
