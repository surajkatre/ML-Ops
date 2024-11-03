# building url dynamically 
# jinja2 teamplate engine 
# variable rule  
# from flask import Flask, render_template, request
# import requests
 

# app = Flask(__name__)

# @app.route("/")
# def welcome():
#     return "Welcome to the Simple Flask App!"
# @app.route("/index",methods=["GET"])
# def index():
#     return render_template("index.html")


# @app.route("/new")
# def about():
#     return render_template("about.html")

# @app.route("/form",methods= ["GET","POST"])
# def aboutq():
#     return render_template("form.html")

 



# if __name__ == '__main__':
#     app.run(debug=True)




# jinja template engine 

'''
{{}} expressins to print output in html 

{%....%} conditional statement , for loops

{#...#} comments 

'''

from flask import Flask,render_template,request, redirect,url_for
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><H1>Welcome to thed  askdasflask course</H1></html>"

@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}!'
    return render_template('form.html')

# variable rule 
@app.route("/success/<int:score>")
def success(score):
    # return f"Your score is {score}" 
    # return f"Your score is " + str(score)
    result= ""
    if score >50:
        result= "PASS"
    else:
        result =  "FAIL"
    
    return render_template("result.html", result=result)






@app.route("/successres/<int:score>")
def success1(score):
    # return f"Your score is {score}" 
    # return f"Your score is " + str(score)
    result= ""
    if score >50:
        result= "PASS"
    else:
        result =  "FAIL"

    exp={'score':score, 'result':result}
    
    return render_template("result1.html", result=exp )


@app.route("/example/<int:score>")
def example(score):
    # return f"Your score is {score}" 
    # return f"Your score is " + str(score)
    
    
    return render_template("result2.html", result=score)




@app.route("/submit1",methods=["GET", "POST"])
def submit1():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres',score=total_score))



if __name__=="__main__":
    app.run(debug=True)