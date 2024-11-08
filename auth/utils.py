from models import User, db


def check_auth(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return True
    return False


def create_user(username, password):
    user = User(username=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
