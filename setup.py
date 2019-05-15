#!/usr/bin/env python3

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='jflint',
    version='0.1',
    scripts=['jflint'],
    author="Andrei Neustroev",
    author_email="andrei.neustroev@gmail.com",
    description="Linter wrapper for jenkinsfile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andreineustroev/jenkinsfile-validator",
    packages=setuptools.find_packages(),
    classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
)
