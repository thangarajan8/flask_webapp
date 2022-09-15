from flask import Flask, session, url_for, redirect, render_template, request, abort, flash



app = Flask(__name__)


 
@app.route("/")
def FUN_root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)