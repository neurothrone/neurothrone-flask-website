from app.models.post import db
from app.models.post import Post


class Micropost(Post):
    __tablename__ = "microposts"

    def update(self, data: dict[str, str]) -> None:
        self.title = data["title"]
        self.body = data["body"]
        db.session.commit()
