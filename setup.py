#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup, find_packages
import pysis

# Odd hack to get 'python setup.py test' working on py2.7
try:
    import multiprocessing
    import logging
except ImportError:
    pass

setup(
    name=pysis.__title__,
    version=pysis.__version__,
    author=pysis.__author__,
    author_email=pysis.__email__,
    url='https://github.com/sustainableis/python-sis',
    description='Python wrapper for the SIS API',
    long_description=open('README.rst').read(),
    license='',
    packages=find_packages(exclude=['*tests*']),
    zip_safe=False
    #install_requires=map(str.strip, open(join('requirements', 'base.txt'))),
    #include_package_data=True,
    #classifiers=(
    #    'Programming Language :: Python',
    #    'Programming Language :: Python :: 2.7',
    #    'Programming Language :: Python :: 3.3+',
    #    'License :: None',
    #    'Operating System :: OS Independent',
    #    'Intended Audience :: Developers',
    #),
)