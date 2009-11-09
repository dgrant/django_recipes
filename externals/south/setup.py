#!/usr/bin/python

from distutils.core import setup
from south import __version__

setup(
    name='South',
    version=__version__,
    description='South: Migrations for Django',
    long_description='South is an intelligent database migrations library for the Django web framework. It is database-independent and DVCS-friendly, as well as a whole host of other features.',
    author='Andrew Godwin & Andy McCurdy',
    author_email='south@aeracode.org',
    url='http://south.aeracode.org/',
    download_url='http://south.aeracode.org/wiki/Download',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
    packages=["south", "south.db", "south.hacks", "south.introspection_plugins", "south.management", "south.management.commands", "south.tests", "south.tests.fakeapp", "south.tests.fakeapp.migrations", "south.tests.otherfakeapp", "south.tests.otherfakeapp.migrations"],
)
