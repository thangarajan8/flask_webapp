from flask import Flask, session, url_for, redirect, render_template, request, abort, flash
import requests


app = Flask(__name__)


 
@app.route("/")
def FUN_root():
    return render_template("index.html")

@app.route('/get_ml', methods=['POST'])
def get_ml():
    query = request.form['query']
    url = "http://localhost:5002/get_ml"

    payload = f"query={query}"
    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'postman-token': "65ec1bc1-c81c-cb96-59a0-736698eb85a7"
        }
    response = requests.request("POST", url, data=payload, headers=headers)

    return response.text


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)