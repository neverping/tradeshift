Tradeshift Triangle Code Challenge
==================================

Here is my triangle code challenge results.
This challenge will work with Python 2.x and Python 3.x as well.

Installing
----------

Install and update using Python's regular method using setup.py:

.. code-block:: text

    $ python setup.py build
    $ python setup.py test
    $ python setup.py install

NOTE: In order to run the tests, you must have pytest and pytest-runner already
installed in your environment.

Testing
-------

Tests are covered by pytest module. You need to have it installed
in order to make use of it.

You can achieve this by installing it using the requirements.txt

.. code-block:: text

    $  pip install -r requirements.txt
    (...)
    $ pytest -vvv


It will generate an output like this:

.. code-block:: text

    ========================================================================== test session starts ==========================================================================
    platform linux2 -- Python 2.7.10, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- ###/bin/python2
    cachedir: .pytest_cache
    rootdir: ###, inifile:
    collected 5 items
    tests/test_triangle.py::TestClass::test_if_inputs_are_ok PASSED                                                                                                   [ 20%]
    tests/test_triangle.py::TestClass::test_for_numbers_above_zero PASSED                                                                                             [ 40%]
    tests/test_triangle.py::TestClass::test_it_must_be_a_equilateral_triangle PASSED                                                                                  [ 60%]
    tests/test_triangle.py::TestClass::test_it_must_be_a_isosceles_triangle PASSED                                                                                    [ 80%]
    tests/test_triangle.py::TestClass::test_it_must_be_a_scalene_triangle PASSED                                                                                      [100%]
    ======================================================================= 5 passed in 0.04 seconds ========================================================================


A Simple Example
----------------

Below are the examples within python or running the code direcly:

.. code-block:: python

    from triangle import check_triangle_type

    check_triangle_type(8,8,8)

.. code-block:: text

    $  python -c 'from triangle import check_triangle_type; print(check_triangle_type(1,2,3))'
    This triangle is scalene type.
