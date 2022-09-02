from setuptools import setup
from typing import List

def get_requirements_list()->List:
    with open("requirements.txt") as f:
        f.readlines()

setup(name='housing-prediction',
version=0.1,
author='Arun',
description='Housing Project',
packages=['housing'],
install_requires=get_requirements_list()
)

if __name__=="__main__":
    print(get_requirements_list())