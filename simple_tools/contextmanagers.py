# -*- coding: utf-8 -*-
"""
.. module:: simple_tools.contextmanagers
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

from contextlib import contextmanager

import time

@contextmanager
def timer(name):
    startTime = time.time()
    yield
    elapsedTime = time.time() - startTime
    print('[{}] finished in {} ms'.format(name, int(elapsedTime * 1000)))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
