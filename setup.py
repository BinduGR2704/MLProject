from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will retuen the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name = 'MLProject',
    version = '0.0.1',
    author = 'bindu',
    author_email='bindugr2004@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

# this setup.py helps to us my MLProject as a package
# used to install/import python libraries and modules
# -e . in requirements is used trigger the setup file