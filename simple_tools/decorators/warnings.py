# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import warnings
import functools


def deprecated(function):
    @functools.wraps(function)
    def deprecated_function(*args, **kwargs):
        warnings.warn(
            "function {} has been deprecated".format( function.__name__),
            DeprecationWarning, stacklevel=2
        )
        return function(*args, **kwargs)
    return deprecated_function

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
