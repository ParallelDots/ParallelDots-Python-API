from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='ParallelDots',
    version='0.2.0',
    description='Python Wrapper for ParallelDots API',
    url='https://github.com/ParallelDots/ParallelDots-Python-API.git',
    author='Ahwan Kumar',
    author_email='ahwan@paralleldots.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='paralleldots sentiment taxonomy ner semantic similarity deeplearning',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[],
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },
    entry_points={
        'console_scripts': [
            'paralleldots=paralleldots:main',
        ],
    },
)
