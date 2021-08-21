from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError

from app.blueprints.projects.cog.apps.book_library.model import Book


class AddBookForm(FlaskForm):
    CATEGORIES = [
        ("reading", "Reading"),
        ("have_read", "Have Read"),
        ("will_read", "Will Read")
    ]

    name = StringField("Name", validators=[DataRequired()])
    author = StringField("Author", validators=[DataRequired()])
    category = SelectField("Category", choices=CATEGORIES, validators=[DataRequired()])
    book_link = StringField("Book link", validators=[DataRequired()])
    image_link = StringField("Image link", validators=[DataRequired()])
    submit = SubmitField("Add Book")

    # Custom defined methods of the format: validate_<field_name> will be used
    # by WTForms as custom validators and are invoked in addition to the
    # stock validators in the validators=[] argument

    # NOTE: will not work if it is a classmethod or staticmethod
    def validate_name(self, name_field: StringField) -> None:
        if Book.find_by_name(name_field.data):
            raise ValidationError("There is already a book by that name.")
