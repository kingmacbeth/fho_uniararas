from flask import Flask, render_template, url_for, session, abort, redirect
from authlib.integrations.flask_client import OAuth
import json
from urllib.parse import quote_plus, urlencode

app = Flask(__name__)

app_conf = {
    "OAUTH2_CLIENT_ID": "hr_web_app",
    "OAUTH2_CLIENT_SECRET": "QkpD9nZ7RQziUltvDpe3V82Ip9gyL05z",
    "OAUTH2_ISSUER": "http://localhost:8080/realms/AuthApp",
    "FLASK_SECRET": "MyLongFlaskSecret",
    "FLASK_PORT": 3000
}

app.secret_key = app_conf.get("FLASK_SECRET")

oauth = OAuth(app)
oauth.register(
    "hrApp",
    client_id=app_conf.get("OAUTH2_CLIENT_ID"),
    client_secret=app_conf.get("OAUTH2_CLIENT_SECRET"),
    client_kwargs={
        "scope": "openid profile email",
        "code_challenge_method": "S256"
    },
    server_metadata_url=f"{app_conf.get('OAUTH2_ISSUER')}/.well-known/openid-configuration",
)


@app.route("/")
def home():
    return render_template("home.html", session=session.get("user"), pretty=json.dumps(session.get("user"), indent=4))


@app.route("/callback")
def callback():
    token = oauth.hrApp.authorize_access_token()
    session["user"] = token

    return redirect(url_for("home"))


@app.route("/login")
def login():
    if "user" in session:
        abort(404)
    return oauth.hrApp.authorize_redirect(redirect_uri=url_for("callback", _external=True))


@app.route("/logout")
def logout():
    id_token = session["user"]["id_token"]
    session.clear()

    return redirect(app_conf.get("OAUTH2_ISSUER")
                    + "/protocol/openid-connect/logout?"
                    + urlencode(
                        {
                            "post_logout_redirect_uri": url_for("loggedout", _external=True),
                            "id_token_hint": id_token
                        },
                        quote_via=quote_plus,
    ))


@app.route("/loggedout")
def loggedout():
    if "user" in session:
        abort(404)
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
