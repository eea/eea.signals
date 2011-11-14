""" Doctests
"""
import doctest
import unittest
from eea.signals.tests.base import EEASignalsFunctionalTestCase
from Testing.ZopeTestCase import FunctionalDocFileSuite


OPTIONFLAGS = (
        doctest.REPORT_ONLY_FIRST_FAILURE |
        doctest.ELLIPSIS |
        doctest.NORMALIZE_WHITESPACE
)

def test_suite():
    """ Tests
    """
    return unittest.TestSuite((
            FunctionalDocFileSuite('README.txt',
                  optionflags=OPTIONFLAGS,
                  package='eea.signals',
                  test_class=EEASignalsFunctionalTestCase),
              ))
