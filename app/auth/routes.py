from datetime import datetime
from flask import request, render_template, session, url_for, redirect, flash, g
from werkzeug.security import check_password_hash, generate_password_hash
from app.auth import bp
from app.extensions import db
from app.models import User

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        # Buscar el usuario en la base de datos por nombre de usuario
        user = User.query.filter_by(username=username).first()

        if user is None or not check_password_hash(user.password, password):
            error = 'Invalid username and/or password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.home'))

        flash(error)

    if not g.user is None:
        return redirect(url_for('blog.home'))

    return render_template('auth/login.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        birthday = request.form['birthday']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        street_address = request.form['street_address']
        phone_number = request.form['phone_number']
        error = None

        # Validación de campos requeridos
        if User.query.filter_by(username=username).first() is not None:
            error = 'User {} is already registered.'.format(username)
        elif not password == password_confirm:
            error = 'The passwords entered do not match.'
        if User.query.filter_by(email=email).first() is not None:
            error = 'Email {} is already registered.'.format(email)

        if error is None:
            # Crear una instancia del modelo User
            new_user = User(
                username=username,
                password=generate_password_hash(password),
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                address=street_address,
                date_of_birth=birthday,
                created_at=datetime.now(),
                updated_at=datetime.now()
            )
            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('auth.login'))

        flash(error)
    
    if not g.user is None:
        return redirect(url_for('main.home'))

    return render_template('auth/register.html')

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.login'))