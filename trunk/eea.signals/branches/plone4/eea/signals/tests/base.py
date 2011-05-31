""" Tests setup
"""
from Products.PloneTestCase import PloneTestCase
from Products.PloneTestCase.layer import onsetup
from Products.Five import zcml
from Products.Five import fiveconfigure

PRODUCTS = ['eea.signals']

@onsetup
def setup_eea_signals():
    """ Setup
    """
    fiveconfigure.debug_mode = True
    import Products.Five
    import eea.signals
    zcml.load_config('meta.zcml', Products.Five)
    zcml.load_config('configure.zcml', Products.Five)
    zcml.load_config('configure.zcml', eea.signals)
    fiveconfigure.debug_mode = False

    PloneTestCase.installProduct('Five')
    for i in PRODUCTS:
        PloneTestCase.installProduct(i)

setup_eea_signals()
PloneTestCase.setupPloneSite(products=PRODUCTS)


class EEASignalsFunctionalTestCase(PloneTestCase.FunctionalTestCase):
    """ Functional test case
    """
