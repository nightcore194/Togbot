import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, Response, make_response
from flask_login import login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
from werkzeug import Response
from werkzeug.security import generate_password_hash, check_password_hash

from backend.models.engine import db_session
from backend.models.models import User
from backend.settings.settings import ENV_FILE

load_dotenv(ENV_FILE)
login_view = Blueprint('login', __name__, url_prefix='/auth')

# Setting up mail-server
mail = Mail()


@login_view.route('/login', methods=['POST'])
async def login() -> Response | str:
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        with db_session() as db:
            user = db.query(User).filter_by(email=email).first()

        if not user or not check_password_hash(user.password, password):  # check password hashes
            flash('Неверное имя пользователя или пароль', "error")
            return redirect('/app/login')
        else:
            login_user(user, remember=remember)  # login user
            return redirect('/')
    return redirect('/app')


@login_view.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/app/login')


@login_view.route('/check_authorization', methods=['GET'])
@login_required
def check_authorization():
    return jsonify({'authorized': True, 'user': current_user.id}), 200


@login_view.route('/signup', methods=['POST'])
async def signup() -> Response | str:  # basic sing up function
    config = os.environ
    email = request.form.get('email')
    username = request.form.get('username')
    display_name = request.form.get('display_name')
    birthday = request.form.get('birthday')
    password = request.form.get('password')
    async with db_session() as db:
        user = await db.query(User).filter_by(
            email=email).first()
    if user:  # check for user exist
        flash('Email address already exists', "error")
        return redirect('/login')
    # create a db cortege if user isnt exists
    new_user = User(email=email,
                    display_name=display_name,
                    birthday=datetime.strptime(birthday, "%Y-%m-%d"),
                    username=username,
                    password=generate_password_hash(password, method='pbkdf2:sha256'))
    await db.add(new_user)
    await db.commit()
    token = generate_token(email)
    html = render_template("confirm.html", confirm_url=f'{config["BASE_URL"]}/confirm?token={token}')
    msg = Message(
            "Confirm your email address!",
            recipients=[email],
            html=html,
            sender=config["MAIL_DEFAULT_SENDER"],
    )
    mail.send(msg)
    flash("Check your e-mail and confirm your registration!", "success")
    return redirect('/app/login')


@login_view.route("/confirm", methods=["POST"])
@login_required
async def confirm_email() -> Response:
    body = request.get_json(force=True)
    token = body["token"]
    if current_user.is_confirmed:
        response = jsonify({"message": "Is confirmed already!"})
        response.status = 208
        return response
    email = confirm_token(token)
    async with db_session() as db:
        user = db.query(User).filter_by(email=current_user.email).first_or_404()
        if user.email == email:
            user.is_confirmed = True
            user.confirmed_on = datetime.now()
            await db.add(user)
            await db.commit()
            response = jsonify({"message": "Successfully confirmed"})
            response.status = 200
        else:
            response = jsonify({"message": "Link has expired!"})
            response.status = 401
    return response


def generate_token(email):
    config = os.environ
    serializer = URLSafeTimedSerializer(config["SECRET_KEY"])
    return serializer.dumps(email, salt=config["SECURITY_PASSWORD_SALT"])


def confirm_token(token, expiration=3600):
    config = os.environ
    serializer = URLSafeTimedSerializer(config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token, salt=config["SECURITY_PASSWORD_SALT"], max_age=expiration
        )
        return email
    except Exception as e:
        return e
