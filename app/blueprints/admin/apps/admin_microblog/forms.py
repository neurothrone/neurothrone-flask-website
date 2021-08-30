from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import InputRequired
from wtforms.validators import Length
from wtforms.validators import ValidationError


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired(), Length(min=1, max=100)])
    body = TextAreaField("Body", validators=[Length(min=1, max=400)])

    # def __init__(self, original_name: str = None, *args, **kwargs) -> None:
    #     super(PostForm, self).__init__(*args, **kwargs)
    #     self.original_name = original_name

    # def validate_name(self, name_field: StringField) -> None:
    #     if self.original_name and name_field.data == self.original_name:
    #         return
    #     if Book.find_by_name(name_field.data):
    #         raise ValidationError("There is already a book by that name.")


class AddPostForm(PostForm):
    submit = SubmitField("Add Post", validators=[InputRequired()])


class EditPostForm(PostForm):
    submit = SubmitField("Edit Post", validators=[InputRequired()])
