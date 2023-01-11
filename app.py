from flask import Flask, Response,app

app= Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return "It is working Just Fine."

if __name__=="__main__":
    app.run(debug=True)