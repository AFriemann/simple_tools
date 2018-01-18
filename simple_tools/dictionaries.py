#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""


def walk(dictionary, root='.'):
    for key, value in dictionary.items():
        if type(value) is dict:
            for subkey, subvalue in walk(value, root + '.' + key):
                yield subkey, subvalue
        else:
            yield key, value

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
