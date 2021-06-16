from flask import Flask

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my First Flask App'

@app.route('/about')
def about():
    return 'About Page'

if __name__=='__main__':
    app.run(debug=True)

