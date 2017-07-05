# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

import re

yes   = re.compile(r'y(?:e(?:s)?)?', re.IGNORECASE)
no    = re.compile(r'n(?:o)?', re.IGNORECASE)
true  = re.compile(r'{}|t(?:rue)?|1'.format(yes.pattern), re.IGNORECASE)
false = re.compile(r'{}|f(?:alse)?|0'.format(no.pattern), re.IGNORECASE)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
