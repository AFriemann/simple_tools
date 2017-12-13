# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import os
import unittest

from simple_tools.files import walk_up


class FilesTestCase(unittest.TestCase):
    def test_walk_up_method(self):
        CWD = os.getcwd()

        for root, parent, files in walk_up('.'):
            assert os.path.dirname(root) == parent

        assert len(list(walk_up('.'))) == len(CWD.split('/'))
        assert len(list(walk_up('.', maxdepth=0))) == 1

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
