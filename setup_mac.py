"""
    python setup.py py2app
"""

from setuptools import setup

APP = ['running-ui_v2.0.py']
DATA_FILES = []
OPTIONS = {}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
