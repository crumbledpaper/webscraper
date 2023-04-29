from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from . import app, db
from .models import User, Product
from .scrapers import get_bonita_smoke_shop_price, get_neptune_cigar_price, get_cigars_international_price


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    # This is a very basic example. In a real application, you would want to validate the form data.
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form['email']).first()
        if user and user.check_password(request.form['password']):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Invalid email or password')
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/compare/<product_name>')
@login_required
def compare_prices(product_name):
    # Get the product from the database
    product = Product.query.filter_by(name=product_name).first()

    if not product:
        flash('Product not found')
        return redirect(url_for('home'))

    # Scrape the prices
    product.bonita_smoke_shop_price = get_bonita_smoke_shop_price(product_name)
    product.neptune_cigar_price = get_neptune_cigar_price(product_name)
    product.cigars_international_price = get_cigars_international_price(
        product_name)

    db.session.commit()

    return render_template('compare.html', product=product)
