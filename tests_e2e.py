"""Integration (browser) tests for tax application.

NOTE: these tests actually start our server, and use Google Chrome to
actually run our tests.

End-to-end tests are slow, harder to write, and a bit of a pain. BUT:
they test that the application *actually works*. If there were a bug in
our front-end Javascript or in our HTML form itself, we might never
notice those kinds of bugs otherwise.
"""

import time
import unittest
from flask_testing import LiveServerTestCase
from selenium import webdriver
from app import app


class TaxResultsTests(LiveServerTestCase):
    def create_app(self):
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())

    def test_form(self):
        self.driver.find_element_by_id("field-income").send_keys("1000")
        self.driver.find_element_by_id("submit-button").click()
        time.sleep(1)
        msg = self.driver.find_element_by_class_name("owed").text
        self.assertIn("$160.00", msg)

    def test_donations(self):
        self.driver.find_element_by_id("field-income").send_keys("10000")
        self.driver.find_element_by_id("field-donations-1").send_keys("1000")
        self.driver.find_element_by_id("field-donations-2").send_keys("1000")
        self.driver.find_element_by_id("submit-button").click()
        time.sleep(1)
        msg = self.driver.find_element_by_class_name("owed").text
        self.assertIn("$1280.00", msg)


if __name__ == '__main__':
    unittest.main()
