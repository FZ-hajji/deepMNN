from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

setup(
    name='deepMNN',

    version='0.01',

    description='',
    long_description=""" """,
    url='',

    author='Anonymous Authors',
    author_email='',

    license='ApacheV2',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Programming Language :: Python :: 3',
    ],

    install_requires=["numpy", "scipy", "torch", "scanpy", "fbpca", "annoy", "metrics"],

    keywords='',

    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'sample=sample:main',
        ],
    },
)
