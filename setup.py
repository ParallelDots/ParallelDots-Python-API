from setuptools import setup, find_packages
from codecs import open
from os import path

def read( fname ):
    with open(fname) as fp:
        content = fp.read()
    return content

setup(
    name="ParallelDots",
    version="1.0.13",
    description="Python Wrapper for ParallelDots APIs",
    long_description=read("DESCRIPTION.rst"),
    url="https://github.com/ParallelDots/ParallelDots-Python-API.git",
    author="Ahwan Kumar,Meghdeep Ray",
    author_email="ahwan@paralleldots.com,meghdeepr@paralleldots.com",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",

        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",

    ],
    keywords="paralleldots sentiment taxonomy ner semantic similarity deeplearning intent emotion abuse",
    packages=find_packages(exclude=["contrib", "docs", "tests*"]),
    setup_requires=[
        "requests"
    ],
    install_requires=[
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "paralleldots=paralleldots:main",
        ],
    },
)
