# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

from contextlib import contextmanager

import os


@contextmanager
def chdir(path):
    old_dir = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(old_dir)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
