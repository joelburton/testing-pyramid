Testing Pyramid Example
=======================

This is a tiny, toy Flask application that calculates taxes owed (using
a completely fake tax algorithm). It is meant to demonstrate the idea of
different kinds of tests:

Unit Tests
    Test the functionality of single functions. In this case, this tests
    different inputs to the core math-y function that actually calculates
    taxes owed.

Integration Tests (often called "Functional Tests")
    Tests the functionality of components working together. This tests
    that our Flask route for calculating taxes owed works. It doesn't use
    a real web browser (like Firefox or Chrome) but does check that things
    like getting stuff off of work forms and templating results work.

End-to-End Tests
    Tests that the app works, for real, in a real browser. This fires up
    an instance of Google Chrome and drives it to use your application like
    a human would.

Requirements
------------

- Python 3.6 or better

- To run the e2e tests, you'll need "chromedriver"

To Demo
-------

::

    pip install -r requirements.txt

    python app.py   # Open browser to localhost:5000 and try the app out!

    python tests_unit.py
    python tests_integration.py
    python tests_e2e.py
