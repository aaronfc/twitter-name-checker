#!/usr/bin/env python

from distutils.core import setup

setup(name='TwitterNameChecker',
 version='1.0',
 description='Python script to check the availability of an account name on Twitter',
 author='Aaron Fas',
 author_email='yo@aaron.com.es',
 url='http://github.com/aaronfc/twitter-name-checker',
 packages=['TwitterNameChecker'],
 scripts=['twitter-check-name'],
)
