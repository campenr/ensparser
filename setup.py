#!/usr/bin/env python3

"""Setup.py for enparser."""

from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="multiplate",
    version="0.1a1",
    description="Parser for multiplate reader output files",
    long_description=long_description,
    url="https://github.com/campenr/multiplate",
    author="Richard Campen",
    author_email="richard@campen.co",
    license="BSD License",

    # TODO add more classifiers (e.g. platform)

    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],

    install_requires = [
        "pandas"
    ],

    keywords="EnSpire, csv, parse, multiplate",
    packages=find_packages(),
    include_package_data=True

)
