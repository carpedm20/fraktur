# -*- coding: utf-8 -*-
"""
fraktur
=======

inpired by [fraktur](https://github.com/substack/fraktur)1

"""
from __future__ import with_statement
import re

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='fraktur',
    packages=['fraktur'],
    version='0.0.1',
    description='𝔠𝔬𝔫𝔳𝔢𝔯𝔱 𝔱𝔥𝔢 𝔩𝔞𝔱𝔦𝔫 𝔞𝔩𝔭𝔥𝔞𝔟𝔢𝔱 𝔱𝔬 𝔣𝔯𝔞𝔨𝔱𝔲𝔯 𝔲𝔫𝔦𝔠𝔬𝔡𝔢 𝔠𝔥𝔞𝔯𝔞𝔠𝔱𝔢𝔯𝔰',
    long_description='',
    license='BSD License',
    author='Taehoon Kim',
    author_email='carpedm20@gmail.com',
    url='http://github.com/carpedm20/franktur',
    keywords=['franktur'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
