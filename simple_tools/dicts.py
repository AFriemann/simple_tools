#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann a.friemann@automate.wtf

"""

def walk(dictionary, root='.'):
    nodes  = []
    leaves = []

    for key, value in dictionary.items():
        if type(value) is dict:
            yield key, walk(value, root+'.'+key)
        else:
            yield key, value

d = {'a': 1, 'b': 2, 'c': [1, 2, 3, {1: 3}], 'd': {'m': 12}}

print('d: %s' % d)
print()

for w in walk(d):
    print('w: %s' % str(w))
    # print('root: %s' % root)
    # print('nodes: %s' % nodes)
    # print('leaves: %s' % leaves)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
