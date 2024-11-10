from flask import Flask, render_template, url_for, session, request, redirect
from config import SECRET_KEY, SQLALCHEMY_DATABASE_URL, SQLALCHEMY_TRACK_MODIFICATIONS

from auth import auth_bp
from models import db

app = Flask(__name__)
app.secret_key = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)
app.register_blueprint(auth_bp)


@app.before_request
def create_tables():
    if (
        request.endpoint
        in [
            "auth.login",
            "auth.register",
            "auth.forgot_password",
            "auth.reset_password",
        ]
        and session.get("authenticated") == True
    ):
        return redirect("/secret")
    db.create_all()


@app.route("/")
def home():
    return render_template("landing.html")


if __name__ == "__main__":
    app.run(debug=True)
