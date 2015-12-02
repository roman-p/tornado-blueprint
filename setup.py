#!/usr/bin/env python3

# The MIT License (MIT)
#
# Copyright (c) 2015 Benedikt Schmitt <benedikt@benediktschmitt.de>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# std
from setuptools import setup

# local
try:
    import tornado_blueprint
except ImportError:
    tornado_blueprint = None


# Setup
# -----------------------------------------------

try:
    long_description = open("README.rst").read()
except OSError:
    long_description = "not available"

try:
    license_ = open("LICENSE.rst").read()
except OSError:
    license_ = "not available"


if tornado_blueprint:
    version = tornado_blueprint.__version__
else:
    version = "- n/a -"

setup(
    name = "tornado-blueprint",
    version = version,
    description = "Modularize your large tornado application with blueprints.",
    long_description = long_description,
    author = "Benedikt Schmitt",
    author_email = "benedikt@benediktschmitt.de",
    url = "https://github.com/benediktschmitt/tornado-blueprint",
    download_url = "https://github.com/benediktschmitt/tornado-blueprint/archive/master.zip",
    packages = ["tornado_blueprint"],
    license = license_,
    install_requires = ["tornado"],
    include_package_data = True,
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Communications",
        "Topic :: Internet",
        "Framework :: Tornado"
        ],
    )
