#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    NTB Bloodbath
#

from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='pybase_db',
    version='1.0.0.dev0',
    description=
    'PyBase is a database manager for YAML, JSON, Bytes and SQLite3. Very poweful, simple and effective.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://pybase.github.io/',
    author='NTBBloodbath',
    author_email='bloodbathalchemist@protonmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['psutil>=5.7.2', 'pyyaml>=5.3.1', 'rich>=8.0.0'],
    classifiers=[
        'Programming Language :: Python :: 3 :: Only',
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Database',
        'Topic :: Database :: Database Engines/Servers',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=False)
