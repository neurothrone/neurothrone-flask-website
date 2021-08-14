from app import create_app
from app import db
from app.models.book import BookModel

app = create_app()


if __name__ == "__main__":
    app.run(port=5000)

# admin.neurothrone.dev
# api.neurothrone.dev
# cot.neurothrone.dev

# neurothrone.dev
# home      /
# about     /about
# projects  /projects
# contact   /contact


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "BookModel": BookModel
    }

