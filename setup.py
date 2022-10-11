
from setuptools import setup
from typing import List


# declaring variable for setup function
PROJECT_NAME = "housing-predictor"
VERSION = "0.0.1"
AUTHOR = "Mayuresh Choudhari"
DESCRIPTION = "this is first ML project"
PACKAGE = ["housing"]
REQUIREMENT_FILE_NAME="requirements.txt"

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
       

setup(

    name=PROJECT_NAME ,
    version=VERSION ,
    author=AUTHOR ,
    description=DESCRIPTION ,
    packages= PACKAGE ,
    install_requires= get_requirements_list()
)
