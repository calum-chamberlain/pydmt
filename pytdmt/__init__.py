#!/usr/bin/python
r"""
Calum Chamberlain's fork of pytdmt to make it more like an actual Python package
"""

__version__ = '2.5'

if __name__ == '__main__':
    import doctest
    doctest.testmod(exclude_empty=True)