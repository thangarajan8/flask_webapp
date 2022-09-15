from flask import Flask, session, url_for, redirect, render_template, request, abort, flash



app = Flask(__name__)


 
@app.route('/get_ml', methods=['POST'])
def products():
    veri = request.form['query']
    print(veri)
    return f'here is veri: {veri}'



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)