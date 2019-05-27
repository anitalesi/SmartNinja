from flask import Flask, render_template, request, make_response
import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    # Abfrage und Antwort von Server, ob wir schon Cookie haben
    secret_number = str(request.cookies.get("secret_number"))
    response = make_response(render_template("index.html"))

    if not secret_number:
        response.set_cookie("secret_number", str(random.randint(1, 30))) # speichern

    return response


@app.route("/result", methods=["POST"])
def result():
    # Abfrage von Benutzer (guess) und von Zufallszahl(secret_number)
    guess = str(request.form.get("guess"))
    secret_number = str(request.cookies.get("secret_number"))

    if str(secret_number) == str(guess):  # Dann vergleichen wir die zwei Nummern
        text = "Success! Congratulation! You have guessed it!"
        response = make_response(render_template("result.html", text=text)) # Objekt Response
        response.set_cookie("secret_number", str(random.randint(1, 30))) # Am Ende speichern wir ein neues Cookie
        return response

    elif str(secret_number) > str(guess):
        text = "Try something bigger!"
        print(guess)
        return render_template("result.html", text=text)

    elif str(secret_number) < str(guess):
        text = "Try something smaller!"
        return render_template("result.html", text=text)
    else:
        pass


if __name__ == '__main__':
    app.debug = True
    app.run()