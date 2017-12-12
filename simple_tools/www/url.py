# -*- coding: utf-8 -*-
"""
.. module: TODO
    :platform: TODO
    :synopsis: TODO

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf
"""


def join(root, *parts, **params):
    if not root.startswith('http'):
        raise ValueError("Invalid root domain, does not start with protocol: {}".format(root))

    root = root.rstrip('/')

    if not parts:
        url = root
    else:
        url = '{}/{}'.format(root, '/'.join(part.lstrip('/').rstrip('/') for part in parts))

    if not params:
        return url

    return '{}?{}'.format(url, '&'.join('='.join(kv) for kv in sorted(params.items())))

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
