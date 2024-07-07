"""
Website to show my portfolio
"""
import os
from datetime import datetime

from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql.expression import func

from db import DbBase, Portfolio

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('FLASK_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///portfolio.db"
Bootstrap5(app)


# Create the extension
db = SQLAlchemy(model_class=DbBase)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.context_processor
def inject_now() -> dict:
    """Inject variables for jinja2 templates

    Returns:
        dict: ditonary for jinja2
    """
    return {'now': datetime.now()}


@app.route('/')
def home() -> str:
    """ Main page

    Returns:
        str: _description_
    """
    result = db.session.query(Portfolio).order_by(func.random()).limit(10).all()
    return render_template('index.html', random_portfolio=result)


@app.route('/about')
def about() -> str:
    """ About page

    Returns:
        str: _description_
    """
    return render_template('about.html')


if __name__ == "__main__":
    app.run(debug=True, port=5001)
