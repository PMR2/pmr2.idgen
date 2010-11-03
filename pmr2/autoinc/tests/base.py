from unittest import TestSuite, makeSuite
from Testing import ZopeTestCase as ztc

import zope.component
from zope.app.component.hooks import getSite

from pmr2.autoinc.interfaces import *

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup, onteardown


@onsetup
def setup():
    import pmr2.app
    fiveconfigure.debug_mode = True
    zcml.load_config('configure.zcml', pmr2.autoinc)
    fiveconfigure.debug_mode = False
    ztc.installPackage('pmr2.autoinc')

@onteardown
def teardown():
    pass

setup()
teardown()
ptc.setupPloneSite(products=('pmr2.autoinc',))


class TestCase(ptc.PloneTestCase):
    pass