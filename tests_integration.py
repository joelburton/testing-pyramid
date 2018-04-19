"""Integration (functional) tests for tax application.

NOTE: as these are "integration tests" or "function tests", we're testing
components playing together. So we'll test how your tax-calculating function
should work with Flask (or how it might work with the database, or other
functions of yours).

Functions tests are especially good for making sure different components
work together well. You don't often use these to test as many different inputs
as you would unit tests.
"""

import unittest
import app


class TaxResultsTests(unittest.TestCase):
    def setUp(self):
        self.client = app.app.test_client()

    def testSingleCalifornia(self):
        res = self.client.get("/results?income=5000&state=CA")
        self.assertIn(b"$1000.00", res.data)

    def testJointCalifornia(self):
        res = self.client.get("/results?income=5000&state=CA&joint=1")
        self.assertIn(b"$800.00", res.data)

    def testDonations(self):
        res = self.client.get("/results?income=5000&state=CA&donations=1000&donations=1000")
        self.assertIn(b"$600.00", res.data)

    def testMissingIncome(self):
        res = self.client.get("/results")
        self.assertEqual(res.status, "500 INTERNAL SERVER ERROR")

    # We might not have too many more tests here in a real app --- we're testing that
    # the "webby" parts of this work -- the real testing of all the possible tax incomes
    # would be handled by unit tests.


if __name__ == '__main__':
    unittest.main()
