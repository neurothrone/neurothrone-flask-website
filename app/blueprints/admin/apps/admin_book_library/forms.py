from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import SelectField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired
from wtforms.validators import ValidationError

from app.blueprints.projects.cog.apps.book_library.model import Book


class BookForm(FlaskForm):
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

    def __init__(self, original_name: str = None, *args, **kwargs) -> None:
        super(BookForm, self).__init__(*args, **kwargs)
        self.original_name = original_name

    # Custom defined methods of the format: validate_<field_name> will be used
    # by WTForms as custom validators and are invoked in addition to the
    # stock validators in the validators=[] argument

    # NOTE: will not work if it is a classmethod or staticmethod
    def validate_name(self, name_field: StringField) -> None:
        if self.original_name and name_field.data == self.original_name:
            return
        if Book.find_by_name(name_field.data):
            raise ValidationError("There is already a book by that name.")


class AddBookForm(BookForm):
    submit = SubmitField("Add Book", validators=[InputRequired()])


class EditBookForm(BookForm):
    submit = SubmitField("Edit Book", validators=[InputRequired()])
