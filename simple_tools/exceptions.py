#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: simple_tools.exceptions
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import logging


LOGGER = logging.getLogger(__name__)


class TimeoutException(RuntimeError):
    def __init__(self, seconds, function):
        self._seconds_ = seconds
        self._function_ = function

    def __str__(self):
        return "execution of {} timed out after {}s".format(self._function_, self._seconds_)


def catch(exception, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except exception as e:
        LOGGER.debug("caught exception %s", e)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
