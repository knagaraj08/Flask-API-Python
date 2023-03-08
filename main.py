from flask import Flask, jsonify, redirect, url_for

app = Flask(__name__)


@app.route('/')
def default_():
    return "Hey! Welcome to Flask"


@app.route('/admin/')
def admin():
    return "Welcome admin"


@app.route('/guest/<guest_name>')
def guest(guest_name):
    return "Welcome %s as Guest" % guest_name


@app.route('/user/<user_name>')
def user(user_name):
    if user_name == "admin":
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest', guest_name=user_name))


# summation method
@app.route('/calculate/add/<int:a>/<int:b>')
def summation(a, b):
    ans = int(a) + int(b)

    res = {
        "Number 1": a,
        "Number 2": b,
        "Summation of Two Numbers is = ": ans
    }

    return jsonify(res)


@app.route('/calculate/sub/<int:a>/<int:b>')
def difference(a, b):
    # ans = abs(int(a) - int(b))
    ans = int(a) - int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Difference of Two Numbers is = ": ans
    }
    return jsonify(res)


@app.route('/calculate/mul/<int:a>/<int:b>')
def mul(a, b):
    ans = int(a) * int(b)
    res = {
        "Number 1": a,
        "Number 2": b,
        "Product of Two Numbers : ": ans
    }
    return jsonify(res)


@app.route('/calculate/div/<int:a>/<int:b>')
def div(a, b):

    try:
        ans = float(a) / float(b)
        res = {
            "Number 1": a,
            "Number 2": b,
            "Division of Two Numbers : ": ans
        }
        return jsonify(res)

    except ZeroDivisionError as Z:
        return "It is a Zero Division Error"


if __name__ == "__main__":
    app.run(debug=True)
