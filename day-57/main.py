import requests
from flask import Flask, render_template

from post import Post

app = Flask(__name__)

def collect_post():
    end_point = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(end_point)
    response.raise_for_status()
    posts = response.json()
    post_objects = []
    for post in posts:
        post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
        post_objects.append(post_obj)
    return post_objects

@app.route('/')
def home():
    post_objects = collect_post()
    return render_template("index.html", all_posts=post_objects)


@app.route("/post/<int:index>")
def show_post(index):
    post_objects = collect_post()
    requested_post = None
    for blog_post in post_objects:
        if blog_post.post_id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
