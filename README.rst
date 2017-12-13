Simple Tools
============

.. image:: https://travis-ci.org/AFriemann/simple_tools.svg?branch=master
    :target: https://travis-ci.org/AFriemann/simple_tools
.. image:: https://badge.fury.io/py/simple_tools.svg
    :target: https://badge.fury.io/py/simple_tools


A collection of various snippets and tools that come up regularly.

.. code:: python

    >>> from mock import Mock

decorators
----------

timeout
~~~~~~~

.. code:: python

    >>> import time
    >>> from simple_tools.decorators.time import timeout
    >>> from simple_tools.exceptions import TimeoutException

    >>> @timeout(3)
    ... def long_running_task():
    ...     time.sleep(5)

    >>> long_running_task() # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    TimeoutException: execution of <function long_running_task at ...> timed out after 3s

errors
~~~~~~

.. code:: python

    >>> from simple_tools.decorators.errors import not_implemented

    >>> @not_implemented
    ... def some_method():
    ...     pass

    >>> some_method() # doctest: +ELLIPSIS +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
        ...
    NotImplementedError

regular expressions
-------------------

.. code:: python

    >>> from simple_tools.regex import true

    >>> for value in ('y', 'yE', 'tru', 'True', '1'):
    ...     assert true.match(value)

lists
-----

.. code:: python

    >>> from simple_tools.lists import find

    >>> l = [Mock(a=1, b=1), Mock(a=2), Mock(a=1, b=2)]

    >>> find(lambda e: e.a == 1, l).b == 1
    True

strings
-------

.. code:: python

    >>> from simple_tools.strings import compact

    >>> s = "a multiline string\n \n   \nwith serveral\nunnecessary\n\n linebreaks"

    >>> print(compact(s))
    a multiline string
    with serveral
    unnecessary
     linebreaks

www
---

.. code:: python

    >>> from simple_tools.www import url

    >>> url.join('http://example.org', 'foo', 'bar', baz='bam')
    'http://example.org/foo/bar?baz=bam'

files
-----

.. code:: python

  >>> from simple_tools.files import walk_up

  >>> for root, parent, files in walk_up('/tmp'):
  ...   print('%s -> %s' % (root, parent))
  /tmp -> /
  / -> /

