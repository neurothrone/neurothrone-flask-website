from app import create_app
from app import db
from app.blueprints.projects.cog.apps.book_library.model import Book
from app.models.user import Account

app = create_app()

if __name__ == "__main__":
    app.run(port=5000)


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Account": Account,
        "Book": Book
    }
