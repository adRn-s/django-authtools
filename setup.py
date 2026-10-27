#!/usr/bin/env python
import os

from setuptools import find_packages, setup

__doc__ = "Custom user model app for Django featuring email as username."


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


install_requires = [
    "Django>=5.2",
]

setup(
    name="django-authtools",
    version="2.0.2.dev0",
    author="Fusionbox, Inc.",
    author_email="programmers@fusionbox.com",
    description=__doc__,
    long_description="\n\n".join([read("README.rst"), read("CHANGES.rst")]),
    url="https://django-authtools.readthedocs.org/",
    license="BSD",
    packages=[
        package for package in find_packages() if package.startswith("authtools")
    ],
    python_requires=">=3.10",
    install_requires=install_requires,
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 5.2",
        "Framework :: Django :: 6.0",
        "Framework :: Django :: 6.1",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
    ],
)
