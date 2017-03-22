#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: simple_tools.decorators.time
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

from concurrent.futures import ThreadPoolExecutor, wait, TimeoutError

from simple_tools.exceptions import TimeoutException

def timeout(seconds):
    def timed_function(f):
        def new_function(*args, **kwargs):
            try:
                with ThreadPoolExecutor(max_workers=1) as executor:
                    future = executor.submit(f, *args, **kwargs)
                    return future.result(timeout=seconds)
            except TimeoutError:
                raise TimeoutException(seconds, f)

        return new_function
    return timed_function

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
