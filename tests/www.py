# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""

import unittest

from simple_tools.www import url


class TestUrlTools(unittest.TestCase):
    def test_urljoin(self):
        self.assertEqual(url.join('http://foobar.com'), 'http://foobar.com')
        self.assertEqual(url.join('http://foobar.com/'), 'http://foobar.com')
        self.assertEqual(url.join('http://foobar.com/', 'bar'), 'http://foobar.com/bar')
        self.assertEqual(
            url.join('http://foobar.com', 'baz', 'bam'),
            'http://foobar.com/baz/bam'
        )
        self.assertEqual(
            url.join('http://foobar.com', foobar="baz", zomg="fasel"),
            'http://foobar.com?foobar=baz&zomg=fasel'
        )
        self.assertEqual(
            url.join('https://foobar.com', 'baz', 'bam', foobar="baz", zomg="fasel"),
            'https://foobar.com/baz/bam?foobar=baz&zomg=fasel'
        )

        with self.assertRaises(ValueError):
            url.join('foobar.com', 'baz', 'bam'),

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
