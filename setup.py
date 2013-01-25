# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="spectroid",
    version="0.0.1",
    url="https://github.com/kanzure/spectroid",
    license="BSD",
    author="Bryan Bishop",
    author_email="kanzure@gmail.com",
    description="API for spectrophotometers",
    long_description=open("README.rst", "r").read(),
    packages=["spectroid"],
    zip_safe=False,
    include_package_data=True,
    install_requires=[],
    platforms="any",
    classifiers=[
        'Natural Language :: English',
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        #"Programming Language :: Python :: 2.6",
        #"Programming Language :: Python :: 2.7",
        #"Programming Language :: Python :: 3",
        #"Programming Language :: Python :: 3.1",
        #"Programming Language :: Python :: 3.2",
        #"Programming Language :: Python :: 3.3",
    ]
)