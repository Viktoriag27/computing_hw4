# setup.py

from setuptools import setup, find_packages

setup(
    name='tarenzvi',  # Library name
    version='0.1',  # Version number
    packages=find_packages(),  # Automatically find all packages
    install_requires=[  # External dependencies (if any)
        'numpy',  # Example dependency
        'pandas',
        'datetime',
        'geopy'
    ],
    description='A simple Python library',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Viktoria, Tarang and Enzo from DSDM 2025',
    author_email='viktoria.gagua@bse.eu',
    url='https://github.com/Viktoriag27/computing_hw4',  # URL of your project repository
    classifiers=[  # Classifiers for Python Package Index (PyPI)
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]
)
