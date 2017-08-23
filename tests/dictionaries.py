# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import unittest

from simple_tools.dictionaries import walk


class DictFunctionsTestCase(unittest.TestCase):
    def test_walk_function(self):
        test_dict = {
            'a': 0,
            'b': 1,
            'c': {
                'c.1': 0,
                'c.2': 1,
            },
            'd': [
                1, 2, 3
            ]
        }

        for key, value in walk(test_dict):
            assert key in ('a', 'b', 'c.1', 'c.2', 'd')


# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
