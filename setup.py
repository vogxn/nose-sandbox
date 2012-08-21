import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()

VERSION = '0.1.0'

setup(
    name = "myplugin-nose",
    version = VERSION,
    author = "Prasanna Santhanam",
    author_email = "Prasanna.Santhanam@citrix.com",
    description = "MyPLugin",
    license = 'ASL 2.0',
    classifiers = [
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        ],

    py_modules = ['myplugin'],
    zip_safe = False,
    
    entry_points = {
        'nose.plugins': ['myplugin = myplugin:myplugin']
        },
    install_requires = ['nose'],
)
