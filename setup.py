import sys
import os

from setuptools import setup

# XXX README needs to be converted to RestructuredText
#long_description = open('README.rst').read()

long_description = 'OCD'

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Intended Audience :: System Administrators',
    'Natural Language :: English',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
]

setup_kwargs = dict(
    name='ocd',
    version='0.1',
    description='A simplified developer experience for OpenShift.',
    long_description=long_description,
    url='https://github.com/openshift-evangelists/ocd',
    author='OpenShift Evangelists',
    license='MIT',
    classifiers=classifiers,
    keywords='openshift',
    py_modules=['ocd'],
    install_requires=['click>=4.0,<7.0'],
    entry_points={ 'console_scripts': ['ocd = ocd:cli'] },
)

setup(**setup_kwargs)
