# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

from simple_tools.regex import yes, no


def confirm(question, default=True):
    prompt = "{} {}/{} ".format(
        question,
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


def collect(resource, default=None):
    if default is not None:
        return input('{} [{}]: '.format(resource, default)) or default
    else:
        return input('{}: '.format(resource))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
