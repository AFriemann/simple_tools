Simple Tools
============

decorators
~~~~~~~~~~

timeout
-------

.. code:: python

    >>> import time
    >>> from simple_tools.decorators.time import timeout
    >>> from simple_tools.exceptions import TimeoutException

    >>> @timeout(3)
    ... def long_running_task():
    ...     time.sleep(5)

    >>> long_running_task() # doctest: +ELLIPSIS
    Traceback (most recent call last):
        ...
    simple_tools.exceptions.TimeoutException: execution of <function long_running_task at ...> timed out after 3s
