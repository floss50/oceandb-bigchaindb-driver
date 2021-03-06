#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGELOG.md') as changelog_file:
    changelog = changelog_file.read()

install_requirements = [
    'bigchaindb_driver',
    'bigchaindb==2.0.0b9',
    'oceandb-driver-interface',
    'singletonify',
]

setup_requirements = ['pytest-runner', ]

dev_requirements = [
    'bumpversion',
    'pkginfo',
    'twine',
    'watchdog',
]

test_requirements = [
    'codacy-coverage',
    'coverage',
    'mccabe',
    'pylint',
    'pytest',
    'tox',
]

setup(
    author="leucothia",
    author_email='devops@oceanprotocol.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="🐳 Ocean DB BigchainDB driver (Python).",
    extras_require={
        'test': test_requirements,
        'dev': dev_requirements + test_requirements,
    },
    install_requires=install_requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + changelog,
    long_description_content_type='text/x-rst',
    include_package_data=True,
    keywords='oceandb_bigchaindb_driver',
    name='oceandb_bigchaindb_driver',
    packages=find_packages(include=['oceandb_bigchaindb_driver']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/oceanprotocol/oceandb-bigchaindb-driver',
    version='0.1.4',
    zip_safe=False,
)
