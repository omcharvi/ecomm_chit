from flask import Flask 

app= Flask(__name__)



@app.route('/hello',methods=['GET','POST'])
def hello_world():
    print("Hello world")
    return "say hello to yourself as chitranjan"

@app.route ('/chitranjan',methods=['GET','POST'])
def printing_msg():
    return "print my matter urgently"

if __name__ == '__main__':
    app.run(debug=True)
