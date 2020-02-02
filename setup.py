from distutils.core import setup
from setuptools import setup

NAME = "ImageToAscii"
DESCRIPTION = 'fast converter image to ascii and fast rendering ascii to image'
URL = "https://github.com/ittybe/imageToAscii"
EMAIL = ""
AUTHOR = "ittybe"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0.4a"

PY_MODULES = []

REQUIRED = [
    'cffi',
    'numpy',
    'Pillow',
    'pycparser',
    'pyvips',
]
PACKEGES = [
    'ImageToAscii'
]
setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      install_requires=REQUIRED,
      packages=PACKEGES
     )