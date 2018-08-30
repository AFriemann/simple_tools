# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import os

from contextlib import contextmanager


@contextmanager
def environment(**kwargs):
    old_env = dict()

    try:
        for key, value in kwargs.items():
            if key in os.environ:
                old_env[key] = os.environ.get(key)

            os.environ[key] = str(value)

        yield
    finally:
        for key in kwargs:
            if key in old_env:
                os.environ[key] = old_env.get(key)
            else:
                del os.environ[key]

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
