"""Functions to calculate taxes owed."""

STATE_TAX_RATES = {
    "CA": 0.2,
    "OR": 0.15,
    "WA": 0.17,
}

DEFAULT_TAX_RATE = 0.16

MINIMUM_TAX = 100.0


def calculateTaxesOwed(income, donations, joint_filing, state):
    """Calculate how much is owed in taxes.

    Params:
      - income: income in USD (dollars)
      - donations: list of donations (in USD) over the past year
      - joint_filing (true/false): filing jointly with partner?
      - state: primary residency

    Returns: taxes owed (in USD)

    For example:

        >>> calculateTaxesOwed(50_000, [1000, 2000], False, "CA")
        9400.0

    There is a minimum $100 tax bill, even with no income:

        >>> calculateTaxesOwed(0, [], False, "CA")
        100.0

    [NOTE: Python can run that "test" above by running this as
    "python -m doctest taxes.py". This kind of in-documentation
    test, called a "doctest" in Python, isn't a great place to put
    lots and lots of testing code [it would drown out the code with
    tests], but it's a good way to make sure that your documentation
    is up-to-date with your code.]

    (This uses a COMPLETELY FICTITIOUS formula for calculating taxes.
    Do not use it to calculate your actual taxes, Gentle Reader ;) )
    """

    total_donations = sum(donations)

    # If they made more than 3 donations, grant a $1000 bonus donation
    if len(donations) > 3:
        total_donations += 1_000

    income -= total_donations

    # calculate effective state rate

    state_rate = STATE_TAX_RATES.get(state, DEFAULT_TAX_RATE)

    if joint_filing:
        state_rate = state_rate / 1.25

    taxes_owed = max([income * state_rate, MINIMUM_TAX])

    return taxes_owed
