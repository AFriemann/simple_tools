# -*- coding: utf-8 -*-
"""
.. module:: simple_tools.lists
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""


def find(function, lst):
    for element in lst:
        if function(element):
            return element

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
