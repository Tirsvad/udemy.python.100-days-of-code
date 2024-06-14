import random
from datetime import datetime

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1, 10)
    year = datetime.now().year
    return render_template('index.html', num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name: str):
    c_year = datetime.now().year
    end_point = 'https://api.genderize.io'
    params = {
        'name': name
    }
    response = requests.get(end_point, params)
    response.raise_for_status()
    gender_data = response.json()
    end_point = 'https://api.agify.io'
    response = requests.get(end_point, params)
    response.raise_for_status()
    age_data = response.json()
    kwargs = {
        'age': age_data['age'],
        'name': name,
        'gender': gender_data['gender'],
        'copyright_year': c_year
    }
    return render_template(template_name_or_list='guess.html', context=kwargs)


@app.route('/blog/')
@app.route('/blog/<num>')
def get_blog(num=None):
    end_point = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(end_point)
    response.raise_for_status()
    if num is None:
        post_context = response.json()
    else:
        try:
            post_context = [response.json()[int(num)]]
        except IndexError:
            return f'Blog id {num} does not exist'
    context = {'copyright_year': datetime.now().year}
    return render_template('blog.html', context=context, posts=post_context)


if __name__ == "__main__":
    app.run(debug=True)
