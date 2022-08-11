#!/usr/bin/env python3
"""
Setup Guesslang

* Install with pip (recommended):
    pip install .

* Install with setuptools:
    pip install -r requirements.txt
    python setup.py install

* Run tests:
    python setup.py pytest

"""

import ast
from pathlib import Path
import re
from os import path

from setuptools import setup, find_packages

SCRIPT_DIR = path.abspath(path.dirname(__file__))

package_version = '2.2.3'

with open(path.join(SCRIPT_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    # Package info
    name='guesslang-experimental',
    author='jossef',
    url='https://github.com/jossef/guesslang',
    description='Detect the programming language of a source code',
    long_description_content_type='text/markdown',
    long_description=long_description,
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    # Install setup
    version=package_version,
    platforms='any',
    packages=find_packages(exclude=['tests', 'tools']),
    install_requires=Path('requirements.txt').read_text(),
    zip_safe=False,
    include_package_data=True,
    entry_points={'console_scripts': ['guesslang = guesslang.__main__:main']},
    tests_require=Path('requirements-dev.txt').read_text(),
    setup_requires=['pytest-runner']
)
