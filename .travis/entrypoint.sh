#!/bin/bash
#
# Copyright (c) 2017 Bitprim developers (see AUTHORS)
#
# This file is part of Bitprim.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
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
sudo $BITPRIM_PIP install --upgrade conan_package_tools
sudo $BITPRIM_PIP install --upgrade wheel
sudo $BITPRIM_PIP install --upgrade twine
sudo $BITPRIM_PIP install --upgrade setuptools 

conan user
conan remote add bitprim_temp https://api.bintray.com/conan/bitprim/bitprim

if [[ "${TRAVIS_BRANCH}" == "dev" ]]; then
    # Just for dev branch
    sudo $BITPRIM_PIP install --upgrade --index-url https://test.pypi.org/pypi/ bitprim-native
fi    

cd /home/conan/project

# sudo $BITPRIM_PIP install -v -e .
sudo $BITPRIM_PIP install -e .

if [[ "${UNIT_TESTS}" == "true" ]]; then
    $BITPRIM_PYTHON test/test_chain.py
fi    

if [[ "${UPLOAD_PKG}" == "true" ]]; then
    sudo $BITPRIM_PYTHON setup.py sdist
    sudo $BITPRIM_PYTHON setup.py bdist_wheel --universal
fi    
