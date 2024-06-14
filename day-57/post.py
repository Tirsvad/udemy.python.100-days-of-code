from dataclasses import dataclass


@dataclass
class Post:
    post_id: int | None = None
    title: str = ""
    subtitle: str = ""
    body: str = ""
