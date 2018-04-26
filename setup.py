# -*- coding: utf-8 -*-
"""
.. module:: TODO
   :platform: Unix
   :synopsis: TODO.

.. moduleauthor:: Aljosha Friemann aljosha.friemann@gmail.com

"""

import os, sys
from subprocess import Popen, PIPE

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

from simple_tools import __version__

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname), 'r').read()

def sh(*args):
    return Popen(args, stdout=PIPE).communicate()[0].strip().decode()

def current_commit():
    return sh('git', 'rev-parse', '--short', 'HEAD')

def git_tag_for(commit):
    return sh('git', 'tag', '--points-at', commit)

def check_version_against_tag():
    commit = current_commit()
    tag = git_tag_for(commit)

    if tag and tag != __version__:
        raise Exception('internal version {} is not equal to deployed version {}'.format(__version__, tag))

if 'upload' in sys.argv or 'register' in sys.argv:
    check_version_against_tag()

setup(name             = "simple_tools",
      author           = "Aljosha Friemann",
      author_email     = "a.friemann@automate.wtf",
      description      = "A collection of various snippets that come up regularly",
      url              = "https://www.github.com/afriemann/simple_tools.git",
      download_url     = "https://github.com/afriemann/simple_tools/archive/{}.tar.gz".format(__version__),
      keywords         = ['snippets'],
      version          = __version__,
      license          = read('LICENSE.txt'),
      long_description = read('README.rst'),
      install_requires = ['futures'],
      classifiers      = [],
      packages         = find_packages(),
      platforms        = 'linux'
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
