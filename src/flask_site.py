from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def _():
    return(render_template('home.html'))
@app.route('/notes')
def _notes():
    return(render_template('home.html'))
@app.route('/confirmsave')
def _confirmsave():
    return(render_template('home.html'))

app.run(debug=True, host='localhost', port=80)