from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    post_id: int | None = None
    title: str = ""
    subtitle: str = ""
    body: str = ""
    author: str = ""
    date: str = ""
    image_url: str = ""
