import os
from flask import Flask, flash, render_template, request, redirect, url_for, json
from forms import PatientSearchForm

app = Flask(__name__)

def showjson():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    filename = os.path.join(SITE_ROOT, 'static', 'MOCK_DATA.json')
    data = json.load(open(json_url))

@app.route('/', methods=['GET', 'POST'])
def index():
    search = PatientSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        qry = app.query(MOCK_DATA)
        results = qry.all()
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('index.html', results=results)

if __name__ == '__main__':
    app.debug = True
    app.run(port=3000)
