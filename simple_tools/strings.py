# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import os


def compact(string):
    return os.linesep.join([s for s in string.splitlines() if s.strip()])

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
