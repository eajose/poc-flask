import json

from flask import (
    request, render_template, redirect, url_for, request, session, flash
)

from app import app

from models.models import db


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/autenticate', methods=['POST', ])
def autenticate():
    if 'admin' == request.form['usuario']:
        session['logged_user'] = request.form['usuario']
        flash(f"{request.form['usuario']} successfully logged in!", 'success')
        return redirect(url_for('index'))
    else:
        flash("Please enter a valid user", 'danger')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session['logged_user'] = None
    flash('No one user logged!', 'info')
    return redirect('/login')


@app.route('/index')
def index():
    if 'logged_user' not in session or session['logged_user'] is None:
        return redirect(url_for('login'))
    
    return render_template('dashboard.html')
    # return (
    #     'This repository was created to practice development of microservices with Flask and this page has been viewed'
    #     ' %s time(s).' % redis.get('hits')
    #     )

@app.route('/tables')
def tables():
    return render_template('tables.html')
