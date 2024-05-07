from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    this function will return the list requirements 

    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]


        if  HYPEN_E_DOT in  requirements : # we need this
            requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='MLproject-Student-Performance-Prediction',
    version='0.0.1',
    author='affan',
    author_email='affinaeem02@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)