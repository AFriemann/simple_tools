# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

from simple_tools.regex import true, false

def bool2str(b):
    return 'yes' if b else 'no'

def str2bool(s):
    s = s if s is not None else ''

    if true.match(s): return True
    elif false.match(s): return False
    else:
        raise ValueError("Value '{}' is not valid for boolean conversion.")

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
