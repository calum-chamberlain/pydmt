"""A setuptools based setup module for pyDMT. package.
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import sys
import os
# To use a consistent encoding
from codecs import open
from os import path
import glob
try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    msg = ' '.join([])
    msg = ' '.join(["warning: pypandoc module not found,",
                    " could not convert Markdown to RST"])
    print(msg)
    read_md = lambda f: open(f, 'r').read()

READ_THE_DOCS = os.environ.get('READTHEDOCS', None) == 'True'

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
long_description = "pyDMT - python based Time-domain moment-tensor inversion"

# Get a list of all the scripts not to be installed
scriptfiles = glob.glob('pytdmt/pytdmt.pytdmt')

if sys.version_info.major == 2:
    if not READ_THE_DOCS:
        install_requires = ['numpy>=1.8.0', 'obspy>=1.0.0',
                            'matplotlib>=1.3.0',
                            'scipy>=0.14']
    else:
        install_requires = ['numpy>=1.8.0', 'obspy>=1.0.0',
                            'matplotlib>=1.3.0']
else:
    if not READ_THE_DOCS:
        install_requires = ['numpy>=1.8.0', 'obspy>=0.10.2',
                            'matplotlib>=1.3.0',
                            'scipy>=0.14']
    else:
        install_requires = ['numpy>=1.8.0', 'obspy>=0.10.2',
                            'matplotlib>=1.3.0']
# install_requires.append('ConfigParser')
setup(
    name='pyTDMT',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.pytdmt and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.5',

    description=long_description,
    long_description=long_description,

    # The project's main homepage.
    url='https://github.com/calum-chamberlain/pydmt',

    # Author details
    author='fabriziobernardi',
    author_email='',

    # Choose your license
    license='',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU Library or Lesser General Public ' +
        'License (LGPL)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='earthquake correlation detection match-filter',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),

    scripts=scriptfiles,

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=install_requires,

    # Test requirements for using pytest
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    # extras_require={
    #     'dev': ['check-manifest'],
    #     'test': ['coverage'],
    # },

)