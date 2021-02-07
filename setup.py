
from setuptools import find_packages
from setuptools import setup

setup(
    name='nametils',
    version='0.0.1',
    author='Andrey Bondar',
    author_email='andreybondar@yahoo.com',
    description="Bag-of-words classificator of russian personal names.",
    license='MIT',
    python_requires='>=3.5.0',
    install_requires=['pytils>=0.3'],
    packages=['nametils'],
    url='https://github.com/andreybondarb/nametils'
) 
