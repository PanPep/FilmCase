from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired


class LibForm(FlaskForm):
    title = StringField('Tytuł', validators=[DataRequired()])
    production = StringField('Produkcja', validators=[DataRequired()])
    format = SelectField('Format', choices=[('CD'), ('Blu-Ray'), ('Cyfrowy')])
    available = SelectField('Dostępny?', choices=[('Tak'), ('Nie'), ('MOST WANTED!')])