"""Unit tests for tax application.

NOTE: as these are "unit tests", we're going to test individual units [functions or
classes], trying to make sure we're testing these "in isolation" (ie, not involving
other stuff, like the web framework or the database.

Unit tests are especially good for trying lots of different inputs to make sure
that calculate-y functions or complex algorithms produce the correct answers.
"""

import unittest
import taxes


class TaxTests(unittest.TestCase):
    def testSingleCalifornia(self):
        owed = taxes.calculateTaxesOwed(50_000, [2000, 1000], False, "CA")
        self.assertEqual(owed, 9400)

    def testJointFiling(self):
        owed = taxes.calculateTaxesOwed(50_000, [2000, 1000], True, "CA")
        self.assertEqual(owed, 7520)

    def testFrequentDonationBounus(self):
        owed = taxes.calculateTaxesOwed(50_000, [1000, 1000, 500, 500], False, "CA")
        self.assertEqual(owed, 9200)

    def testMinimumTax(self):
        owed = taxes.calculateTaxesOwed(500, [], False, "CA")
        self.assertEqual(owed, 100)

    def testDefaultStateRate(self):
        owed = taxes.calculateTaxesOwed(50_000, [1000, 1000, 500, 500], False, "PR")
        self.assertEqual(owed, 7360)

    # In a real life app with a complex function like calculateTaxesOwed, there might
    # be dozens (or more!) unit tests: they're fast and easy to write, and run very
    # quickly.


if __name__ == '__main__':
    unittest.main()
