from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:

    requirements_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            files=file.readlines()
            for line in files:
                requirement=line.strip()
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("file not found")
    return requirements_lst


setup(
    name="NETWORK_SECURITY_SYSTEM",
    version="0.0.1",
    author="SunnyKumar",
    author_email="sunnyrajmatikumar@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
