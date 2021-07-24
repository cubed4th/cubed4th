#!/usr/bin/env python3
# -*- encoding: utf-8
# SPDX-License-Identifier: MIT
# Copyright (c) https://github.com/scott91e1 ~ 2021 - 2021

__banner__ = r""" (

    As close to FORTH-79 as makes sense when the underling machine is Python.








)





"""  # __banner__

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

long_description += "\n\n"

with open("LICENSE.md", "r") as fh:
    long_description += fh.read()

from cubed4th.cli_FORTH import __version__

setuptools.setup(
    name="cubed4th",
    version=__version__,
    author="Scott McCallum <https://linkedin.com/in/scott-mccallum>",
    author_email="cubed4th@HQ.UrbaneInter.net",
    description=": cubed4th 'PYTHON 'FORTH 'OOP + * 3 ^ ;",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sno-ware/cubed4th",
    packages=setuptools.find_packages(),
    install_requires=[
    ],
    entry_points={"console_scripts": ["c4=cubed4th.cli_FORTH:ide_stdio"]},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Console :: Curses",
        "Environment :: Win32 (MS Windows)",
        "Environment :: No Input/Output (Daemon)",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: System Administrators",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: SQL",
        "Programming Language :: Forth",
        "Topic :: Education",
        "Topic :: Multimedia",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Interpreters",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Pre-processors",
        "Topic :: Software Development :: User Interfaces",
        "Topic :: Software Development :: Version Control",
        "Topic :: System :: Software Distribution",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: Markup :: Markdown",
    ],
    python_requires=">=3.7",
)
