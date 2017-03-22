#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: simple_tools.exceptions
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

class TimeoutException(RuntimeError):
    def __init__(self, seconds, function):
        self._seconds_ = seconds
        self._function_ = function

    def __str__(self):
        return "execution of {} timed out after {}s".format(self._function_, self._seconds_)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
