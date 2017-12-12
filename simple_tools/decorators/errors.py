# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import functools


def not_implemented(function):
    @functools.wraps(function)
    def not_implemented_function(*args, **kwargs):
        raise NotImplementedError(function)
    return not_implemented_function

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
