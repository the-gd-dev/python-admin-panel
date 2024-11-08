from flask import render_template, request, redirect, url_for, session, flash
from .utils import check_auth
from . import auth_bp


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if check_auth(username, password):
        session["authenticated"] = True
        return redirect(url_for("auth.secret"))
    else:
        flash("Invalid Credentials", "danger")
    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")


@auth_bp.route("/secret")
def secret():
    if not session.get("authenticated"):
        return redirect(url_for("auth.login"))
    return render_template("secret.html")


@auth_bp.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("auth.login"))
