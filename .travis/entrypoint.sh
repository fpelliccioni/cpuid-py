#!/bin/bash
#
# Copyright (c) 2017-2023 Fernando Pelliccioni
#
set -e
set -x

python --version

if [[ $TRAVIS_PYTHON_VERSION == 2.7 ]]; then
    export BITPRIM_PYTHON=python
    export BITPRIM_PIP=pip
else
    sudo apt-get update
    sudo apt-get --yes install python3.6
    sudo apt-get --yes install python3.6-dev

    wget https://bootstrap.pypa.io/get-pip.py
    sudo python3.6 get-pip.py
    export BITPRIM_PYTHON=python3.6
    export BITPRIM_PIP=pip3.6
fi

sudo $BITPRIM_PIP install --upgrade pip
sudo $BITPRIM_PIP install --upgrade wheel
sudo $BITPRIM_PIP install --upgrade twine
sudo $BITPRIM_PIP install --upgrade setuptools


if [[ "${TRAVIS_BRANCH}" == "dev" ]]; then
    # Just for dev branch
    sudo $BITPRIM_PIP install --upgrade --index-url https://test.pypi.org/pypi/ cpuid-native
fi

cd /home/conan/project

# sudo $BITPRIM_PIP install -v -e .
sudo $BITPRIM_PIP install -e .

# if [[ "${UNIT_TESTS}" == "true" ]]; then
#     $BITPRIM_PYTHON test/test_chain.py
# fi

if [[ "${UPLOAD_PKG}" == "true" ]]; then
    sudo $BITPRIM_PYTHON setup.py sdist
    sudo $BITPRIM_PYTHON setup.py bdist_wheel --universal
fi
