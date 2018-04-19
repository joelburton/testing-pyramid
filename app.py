from flask import Flask, request, render_template

import taxes


app = Flask(__name__)

@app.route('/')
def form():
    """Show form."""

    return render_template("form.html")


@app.route('/results')
def calculate_taxes():
    """Calculate taxes owed."""

    if "income" not in request.args:
        raise Exception("Missing Income")

    income = int(request.args.get("income"))
    state = request.args.get("state", "CA")
    donations = [int(donation) for donation in request.args.getlist("donations") if donation]
    joint = request.args.get("joint", False)

    owed = taxes.calculateTaxesOwed(income, donations, joint, state)

    return render_template("results.html", owed=owed)


if __name__ == '__main__':
    app.run()
