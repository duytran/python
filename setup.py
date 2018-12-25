#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

readme = "This is the package for Python"

requirements = [
    'jupyterlab'
]

setup_requirements = []

test_requirements = []

dependency_links = []

setup(
    author="Duy Tran",
    author_email='tranduydn@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT license',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    description='A python training',
    entry_points={
        'console_scripts': [],
    },
    install_requires=requirements,
    dependency_links=dependency_links,
    license='MIT license',
    include_package_data=True,
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/duytran/python',
    version='1.0.0',
    zip_safe=False
)
