#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# THE WISKEY-WARE LICENSE
# -----------------------
#
# "THE WISKEY-WARE LICENSE":
# <jbc.develop@gmail.com> wrote this file. As long as you retain this notice you
# can do whatever you want with this stuff. If we meet some day, and you think
# this stuff is worth it, you can buy me a wiskey in return JuanBC
#

# ==============================================================================
# DOCS
# ==============================================================================

'''

'''
# ==============================================================================
# IMPORTS
# ==============================================================================

import os


# ==============================================================================
# CONSTANTS
# ==============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))


# ==============================================================================
# FUNCTIONS
# ==============================================================================

def get(filename):
    fullname = os.path.join(PATH, filename)
    if not os.path.isfile(fullname):
        raise IOError("File {0} not exists".format(fullname))
    return fullname


# ==============================================================================
# MAIN
# ==============================================================================

if __name__ == '__main__':
    print(__doc__)
