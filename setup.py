# -*- coding: utf-8 -*-
import sys
from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 4 - Beta",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Database",
    "Topic :: Software Development",
    "Topic :: Software Development :: Testing",
]

install_requires = ['testing.common.database @ git+https://github.com/brennane/testing.common.database@master#egg=testing.common.database',
                    'pymysql']


setup(
    name='testing.mysqld',
    version='1.4.1',
    description='automatically setups a mysqld instance in a temporary directory, and destroys it after testing',
    long_description=open('README.rst').read(),
    classifiers=classifiers,
    keywords=[],
    author='Takeshi Komiya (ed. B. Evans)',
    author_email='fw-be-github @ wumpus dot org',
    url='https://github.com/brennane/testing.mysqld',
    license='Apache License 2.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'': ['buildout.cfg']},
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        'testing': ['mock', 'nose', 'SQLAlchemy'],
    },
    test_suite='nose.collector',
    namespace_packages=['testing'],
)
