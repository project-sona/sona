#!/usr/bin/env python
"""
Setuptools installation file

https://github.com/project-sona/sona
"""

from setuptools import setup, find_packages
# encoding
from codecs import open
from os import path

VERSION = '0.1'

setup(
        name = 'Sona',

        version = VERSION,

        description = 'Minimal, hackable memorization tool',

        url = 'https://github.com/project-sona/sona',

        author = 'Daniil Soloviev and Marnix Massar',

        license = 'GPLv3',

        classifiers = [
            'Development Status :: 3 - Alpha',

            # Pick your license as you wish (should match "license" above)
            'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

            # Specify the Python versions you support here. In particular, ensure
            # that you indicate whether you support Python 2, Python 3 or both.
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            ],

        packages = find_packages(exclude=['docs']),

        entry_points = {'console_scripts': [
            'sona = sona.main:main'
            ]
            }
        )
