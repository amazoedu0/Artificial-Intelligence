from flask import Flask,render_template
app=Flask(__name__)

@app.route("/")
def task1():
    data = ["Bahria","University","Islamabad"]
    return render_template('index.html',data=data)
app.run(debug=True)
    