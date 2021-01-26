#!/usr/bin/env python

# 
# Copyright (c) 2017-2021 Fernando Pelliccioni
# 

from setuptools import setup

__title__ = "cpuid"
__summary__ = "cpuid Pythonic API"
__uri__ = "https://github.com/fpelliccioni/cpuid-py"
__version__ = "0.0.10"
__author__ = "Fernando Pelliccioni"
__email__ = "fpelliccioni@gmail.com"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2017-2021 Fernando Pelliccioni"


install_requires = [
    "cpuid-native >= 0.0.7",
]

setup(
    name = __title__,
    version = __version__,
    description = __summary__,
    # long_description=open("./README.rst").read(),
    # long_description_content_type="text/x-rst",

    long_description=open("./README.md").read(),
    long_description_content_type="text/markdown",

    license = __license__,
    url = __uri__,
    author = __author__,
    author_email = __email__,

    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Natural Language :: English",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
    ],    

    # What does your project relate to?
    keywords='cpuid intel amd x86 cpu',

    py_modules=["cpuid"],

    install_requires=install_requires,
    # setup_requires=setup_requires,
    

    dependency_links=[
        'https://testpypi.python.org/pypi',
        'https://testpypi.python.org/pypi/cpuid-native/',
    ],

    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
)

