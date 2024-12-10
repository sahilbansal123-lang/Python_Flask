from flask import Flask 
### WSGI Application: which is used to communicate between 
### server and web application
app=Flask(__name__)

@app.route('/')
def welcome():
    return'Welcome to my Windows Screen my name is sahil'

@app.route('/members')
def Member():
    return'Welcome to my Members Screen'

if __name__=='__main__':
    app.run(debug=True)
