# send variable to html using jinja2 templates
"""
{%...%} for stmt
{{}} expression to print output
{#.. #} comment

"""
from flask import Flask,redirect,url_for, render_template, request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/score/<int:score>')
def score(score):
    return render_template('a1.html',result = score)

@app.route('/score1')
def score1():
    score = [12,14,15,16,18]
    return render_template('a2.html',result = score)

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',result = res)


### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    avg_score = 0
    if request.method=='POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        avg_score = (science+maths+c+data_science)/4
    return redirect(url_for('success',score=avg_score))

if __name__=='__main__':
    app.run(debug=True)

