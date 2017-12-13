# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import os


def walk_up(root, maxdepth=None):
    depth = 0

    for root, dirs, files in os.walk(os.path.abspath(root), topdown=True):
        parent_directory = os.path.dirname(root)
        dirs[:] = [ parent_directory ]

        yield root, parent_directory, files

        if parent_directory == root or (maxdepth is not None and depth >= maxdepth):
            break

        depth += 1


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
