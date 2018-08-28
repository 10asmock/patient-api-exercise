from wtforms import Form, StringField, SelectField

class PatientSearchForm(Form):
    choices = [('id', 'id'),
               ('first_name', 'first_name'),
               ('last_name', 'last_name')]
    select = SelectField('Search for patient:', choices=choices)
    search = StringField('')
