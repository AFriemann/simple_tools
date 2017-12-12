#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import unittest
import time

from simple_tools.decorators.errors import not_implemented
from simple_tools.decorators.time import timeout
from simple_tools.exceptions import TimeoutException


class TimeDecoratorTestCase(unittest.TestCase):
    def test_timeout_times_out_function(self):
        @timeout(2)
        def task():
            time.sleep(3)

        with self.assertRaises(TimeoutException):
            task()


class ErrorDecoratorTestCase(unittest.TestCase):
    def test_not_implemented_decorator(self):
        @not_implemented
        def foo():
            pass

        with self.assertRaises(NotImplementedError):
            foo()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
