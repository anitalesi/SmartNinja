from requests_oauthlib import OAuth2Session
from flask import Flask, render_template, request, make_response, redirect, session
import os
import json

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

# User Authorization
@app.route("/login")
def login():
    github = OAuth2Session(os.environ.get("client_id"))
    authorization_url, state = github.authorization_url("https://github.com/login/oauth/authorize")
    # User Authorization on github
    # save user's authorization into a cookie
    response = make_response(redirect(authorization_url))
    response.set_cookie(authorization_url, httponly=True, samesite='Strict')

    return response


@app.route("/callback", methods=["GET"])
def call_back():
    # redirected back from the provider to callback URL
    github = OAuth2Session(os.environ.get("client_id", state=session['oauth_state']))
    token = github.fetch_token("https://github.com/login/oauth/access_token", client_id="client_id",
                               client_secret=os.environ.get("client_secret"), authorization_response=request.url)
    # token saved into a cookie
    response = make_response(redirect(token))
    response.set_cookie(token, httponly=True, samesite='Strict')

    return response


@app.route("/profile", methods=["GET"])
def profile():
    # Fetching a protected variables
    github = OAuth2Session(os.environ.get("client_id"))
    token = request.cookies.get("token")
    github_data = github.get('https://api.github.com/user')
    return render_template("profile.html", github_data=github_data, token=token)


if __name__ == '__main__':
    app.run(debug=True)  # if you use the port parameter, delete it before deploying to Heroku
