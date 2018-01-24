# -*- coding: utf-8 -*-

from simple_tools.exceptions import catch


def test_exception_catching():
    assert catch(Exception, lambda: 2) == 2
    assert catch(ZeroDivisionError, lambda x: 2 / x, 2) == 1
    assert catch(ZeroDivisionError, lambda x: 2 / x, 0) is None

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 fenc=utf-8
