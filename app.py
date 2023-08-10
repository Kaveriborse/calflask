from flask import Flask,request,render_template,jsonify
import json

app=Flask(__name__)  #initialization of app i.e main module


#create an URL
@app.route('/')
def welcome():
    return "Welcome to the Flask"

@app.route('/cal',methods=['GET'])
def math_operator():
    #we get the nos from html or postman
    operation=request.json["operation"]
    num1=request.json["num1"]
    num2=request.json["num2"]

    if operation=="add":
        result=int(num1)+int(num2)
    elif operation=="multiply":
        result=int(num1)*int(num2)
    elif operation=="division":
        result=int(num1)/int(num2)
    else:
        result=int(num1)-int(num2)
    return jsonify(result)

#jsonify converting input into json 
#for input using html we use request bcz it is client server application
#client is browser


print(__name__)

if __name__=='__main__':
    app.run()


