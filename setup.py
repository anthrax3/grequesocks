#!/usr/bin/env python
__author__ = 'Tomerz'

from distutils.core import setup


setup(
    name='grequesocks',
    version='1.0',
    description='Grequests Monkey Patch To Use Requesocks',
    author='RealGame (Tomer Zait)',
    author_email='realgam3@gmail.com',
    install_requires=[
        'grequests',
        'requesocks'
    ],
    py_modules=['grequesocks'],
)