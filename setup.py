
from setuptools import find_packages
from setuptools import setup

setup(
    author='Andrey Bondar',
    author_email='andreybondar@yahoo.com',
    description="Bag-of-words classificator of russian personal names.",
    license='MIT',
    name='Nametils',
    python_requires='>=3.5.0',
    install_requires=[
        'pytils>=0.3'],
    packages=find_packages(exclude=['examples']),
    url='https://github.com/andreybondarb/Nametils',
    version='0.0.1',
) 
