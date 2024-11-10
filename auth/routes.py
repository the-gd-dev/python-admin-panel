from flask import render_template, request, redirect, url_for, session, flash
from .utils import check_auth, create_user
from . import auth_bp
from models import User, db


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if check_auth(username, password):
            session["authenticated"] = True
            return redirect(url_for("auth.secret"))
        else:
            flash("Invalid Credentials", "error")
    return render_template("login.html", title="Login")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        print(request.form)
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        email = request.form.get("email")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        if not password == confirm_password:
            return render_template(
                "register.html",
                title="Register",
                errors={password: "password not matched!"},
            )
        try:
            user = User(
                firstname=firstname,
                lastname=lastname,
                email=email,
                username=username,
            )
            user.set_password(password)
            db.session.add(user)
            db.session.commit()
            session["authenticated"] = True
            return redirect(url_for("auth.secret"))
        except:
            return render_template(
                "register.html",
                title="Register",
                error_message="user not created!",
            )
    return render_template("register.html", title="Register")


@auth_bp.route("/secret")
def secret():
    if not session.get("authenticated"):
        return redirect(url_for("auth.login"))
    return render_template("secret.html")


@auth_bp.route("/logout")
def logout():
    session.pop("authenticated", None)
    return redirect(url_for("auth.login"))

@auth_bp.route("/forgot-password")
def forgot_password():
    return render_template("forgot-password.html", title="Forgot Password")


@auth_bp.route("/reset-password")
def reset_password():
    return render_template("reset-password.html", title="Reset Password")
