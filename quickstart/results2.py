from flask import Flask, url_for, render_template
app = Flask(__name__)

@app.route('/results2')
def result():
    dict = {'phy' : 50, 'che' : 60, 'maths' : 70}
    return render_template('results2.htm', result = dict)