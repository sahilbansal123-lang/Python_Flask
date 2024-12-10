### Building URL Dynamically
### Variables rules and URL building

from flask import Flask,redirect,url_for

app=Flask(__name__)
@app.route('/')    ### DECORATOR FOR URL
def Welcome():
    return 'WELCOME FAMMMMMMMM!!!'

@app.route('/success/<int:score>')
def success(score): 
    return "the person has passed and the marks is " + str(score)

@app.route('/fail/<int:score>')
def fail(score): 
    return "the person has Failed and the marks is " + str(score)

### result checker
@app.route('/results/<int:marks>')
def results(marks): 
    result=""
    if marks < 50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))

### URL_For

if __name__=='__main__':
    app.run(debug=True)