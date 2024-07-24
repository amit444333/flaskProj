from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length

        
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=60)])
    content = TextAreaField('Content', validators=[DataRequired()], render_kw={"cols": 15})
    submit = SubmitField('Post')
    