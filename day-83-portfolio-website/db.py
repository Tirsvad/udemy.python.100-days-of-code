"""
    Create and populate the Db
    Handles save and get list of prjoects
"""
import json
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import Session
from sqlalchemy import String
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine


from constants import DB_FILE

class DbBase(DeclarativeBase):
    pass



class Portfolio(DbBase):
    """Database table "project"

    Args:
        id (int): _description_
        title (str): _description_
        type (str): _description_
        description (str): _description_
        img_url (str): _description_
        source_code_url (str): _description_

    Returns:
        _type_: _description_
    """
    __tablename__ = "project"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    type: Mapped[str] = mapped_column(String(30))
    description: Mapped[str] = mapped_column(String(250))
    img_url: Mapped[str] = mapped_column(String(75))
    source_code_url: Mapped[str] = mapped_column(String(75))

    def __repr__(self) -> str:
        return f"{self.id} {self.title}"

    def load_from_json(self, file: str = "project.json") -> None:
        engine = create_engine(f"sqlite:///{DB_FILE}", echo=True)
        DbBase.metadata.create_all(engine)
        projects_list = []
        with open(file, encoding="utf-8") as f:
            data = json.load(f)
        for record in data:
            projects_list.append(
                Portfolio(
                    id=record['id'],
                    title=record['title'],
                    type=record['type'],
                    description=record['description'],
                    img_url=record['img_url'],
                    source_code_url=record['source_code_url'],
                )
            )

        with Session(engine) as session:
            session.add_all(projects_list)
            session.commit()


if __name__ == "__main__":
    app = Portfolio()
    app.load_from_json()
