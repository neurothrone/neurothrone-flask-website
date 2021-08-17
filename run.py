from app import create_app
from app import db
from app.models.book import BookModel
from app.models.user import UserModel

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "BookModel": BookModel,
        "UserModel": UserModel
    }
