"""The setup script."""

from setuptools import setup, find_packages
import os

version = os.getenv('VERSION', '0.0.1')

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="teeny-romatic-consequence",
    version=version,
    author="Antonin Thioux",
    author_email="antonin.thioux@gmail.com",
    description="testing pypi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntoninThioux/TeenyRomaticConsequence",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    license="WTFPL linence",
    packages=find_packages(
        include=['teenyromaticconsequence', 'teenyromaticconsequence.*']
    ),
    python_requires=">=3.8"
)
