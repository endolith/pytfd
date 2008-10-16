#!/usr/bin/env python
"""pytfd: A library of time-frequency distributions.

pytfd is a python library of the most common time-frequency distributions used in
signal processing.  It builds upon numpy.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

import sys, os

DOCLINES = __doc__.split("\n")

CLASSIFIERS = """\
Development Status :: 1 - Alpha
Intended Audience :: Science/Research
Intended Audience :: Developers
License :: OSI Approved :: BSD License
Programming Language :: Python
Topic :: Software Development
Topic :: Scientific/Engineering
Operating System :: Microsoft :: Windows
Operating System :: POSIX
Operating System :: Unix
Operating System :: MacOS
"""

version = '0.0'

setup(
    name='pytfd',
    version=version,
    description=DOCLINES[0],
    long_description="\n".join(DOCLINES[2:]),
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='science engineering dsp',
    author='Edin Salkovic',
    author_email='edin.salkovic@gmail.com',
    url='',
    license='BSD',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    #install_requires=["numpy>=1.0"],
)
