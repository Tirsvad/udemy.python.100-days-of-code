import requests
from flask import Flask, render_template, redirect, url_for

from post import Post

app = Flask(__name__)


@app.route('/')
def home():
    post_objects = collect_posts()
    return render_template('index.html', all_posts=post_objects)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/post/<int:post_id>')
def show_post(post_id: int):
    post = get_post(post_id)
    if post is not None:
        return render_template('post.html', post=post)
    return redirect(url_for('home'))



def collect_posts() -> list[Post]:
    end_point = "https://api.npoint.io/da5606ba2321798b51e1"
    response = requests.get(end_point)
    response.raise_for_status()
    posts = response.json()
    post_objects: list[Post] = []
    for post in posts:
        post_obj = Post(
            post_id=post["id"],
            title=post["title"],
            subtitle=post["subtitle"],
            body=post["body"],
            author=post["author"],
            date=post["date"],
            image_url=post["image_url"]
        )
        post_objects.append(post_obj)
    return post_objects


def get_post(post_id: int) -> Post | None:
    for post in collect_posts():
        if post.post_id == post_id:
            return post
    return None


if __name__ == "__main__":
    app.run(debug=True)
