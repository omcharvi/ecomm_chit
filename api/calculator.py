from flask import Flask, request, Response, jsonify

app= Flask (__name__)
@app.route('/')
def home():
    return "Welcome to home of flask"

@app.route('/cal', method =['POST'] )
def calculator():
    data=request. get_json()
    operation = data.get('operation')
    num1 =data.get('num1')
    num2 =data.get('num2')

    if operation == 'add':
        return num1+num2
    elif operation =='subtract':
        return num1-num2
    elif operation =='multiply':
        return num1*num2
    elif operation =='divide':
        return num1 / num2
    else:
        return 'Cannot divide by zero'
    
if __name__=='__main__':
    app.run(debug=True,port = 5001)

@app.route('/cal_browser', method =['GET'] )
def calculator_browser():

    operation = request.args.get('operation')
    num1 =request.data.args.get('num1')
    num2 =request.args.get('num2')

    if operation == 'add':
        return num1+num2
    elif operation =='subtract':
        return num1-num2
    elif operation =='multiply':
        return num1*num2
    elif operation =='divide':
        return num1 / num2
    else:
        return 'Cannot divide by zero'
    