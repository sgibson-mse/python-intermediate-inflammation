"""Defines metadata about the software eg. name, version. Used to distribute the package."""

from setuptools import setup, find_packages

setup(
    name="inflammation-analysis",
    version='1.0',
    packages=find_packages()
)