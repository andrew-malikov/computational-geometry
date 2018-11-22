from setuptools import find_packages, setup

setup(
    name='geometry',
    version='1.0',
    packages=find_packages(exclude=['tests', 'tests.*']),
)
