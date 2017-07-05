# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

from simple_tools.regex import yes, no

def confirm(question, default=True):
    prompt = "{} {}/{} ".format(question,
        '[y]' if default else 'y',
        '[n]' if not default else 'n'
    )

    response = input(prompt)

    if yes.match(response):
        return True
    elif no.match(response):
        return False
    else:
        return default

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
