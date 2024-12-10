### Integrate HTML with Flask
### HTTP verb GET and POST

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)
@app.route('/')    ### DECORATOR FOR URL
def Welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score): 
    res=""
    if score < 50:
        res="FAIL"
    else:
        res="PASS"
    return render_template('result.html',result=res)

# ### result checker
# @app.route('/results/<int:marks>')
# def results(marks): 
#     result=""
#     if marks < 50:
#         result='fail'
#     else:
#         result='success'
#     return redirect(url_for(result,score=marks))

### result checker submit HTML PAGE
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_Score = 0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        total_Score=(science+maths+c+data_science)/4
    res=""
    if total_Score >= 50:
        res="success"
    else:
        res="fail"
    return redirect(url_for(res, score=total_Score))




if __name__=='__main__':
    app.run(debug=True)