# -*- coding: utf-8 *-*

import nose
from ninja_testing.ninja_nose_plugin import NinjaNosePlugin

if __name__ == '__main__':
    nose.main(addplugins=[NinjaNosePlugin()])
