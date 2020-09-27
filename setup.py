#!/usr/bin/env python
"""Pythonic Setup for autoenv."""


import setuptools


def readme():
    with open("README.md") as f:
        README = f.read()
    return README


setuptools.setup(
    version='0.2.1',
    name='autoenv',
    description='Directory-based environments.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    author='Ralph Göstenmeier',
    author_email='rg@via-internet.de',
    license='See LICENSE.',
    url='https://github.com/r14r/autoenv',
    scripts=['activate.sh'],
)
