# Requirements --------------------------------------
# pip install wheel
# pip install twine
# ---------------------------------------------------

sudo ./reset.sh
sudo pip install -v -e .

sudo python setup.py sdist                       # Source Distribution, for Linux
sudo python setup.py bdist_wheel --universal     # Universal Wheels, Pure Python, for py2 and py3

twine upload dist/*
sudo ./reset.sh


# sudo python setup.py sdist                       # Source Distribution, for Linux
# python setup.py bdist_wheel --universal     # Universal Wheels, Pure Python, for py2 and py3
# python setup.py bdist_wheel                 # Pure Python Wheels, Pure Python, but don’t natively support both Python 2 and 3.
# python setup.py bdist_wheel                 # Platform Wheels, with compiled extensions, for macOS and Windows


# /home/fernando/.local/bin/twine upload dist/*

# sudo ./reset.sh

# --------------------------------------------------
# Luego, para el que instala

# pip install bitprim-native --no-cache-dir