Simple Tools
============

A collection of various snippets and tools that come up regularly.

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

regular expressions
-------------------

.. code:: python

    >>> from simple_tools.regex import true

    >>> for value in ('y', 'yE', 'tru', 'True', '1'):
    ...     assert true.match(value)

