#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import unittest

from simple_tools.strings import compact

class StringTestCase(unittest.TestCase):
    def test_string_compacting(self):
        string = 'foo\nbar\n\nbaz\n    \nbam boo\n'

        self.assertEqual(compact(string), 'foo\nbar\nbaz\nbam boo')

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
