from flask import Flask, redirect, url_for, render_template, request
from common import success_responce, error_responce
from logger import LOGGER


app = Flask(__name__)

@app.route("/<num>")
def home(num):
    return render_template('index.html', num= num)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        _user = request.form['nm']
        return redirect(url_for('user', usr = _user))
    else:
        return render_template('login.html')

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

# @app.route("/health", methods = ['GET'])
# def health():
#     LOGGER.info(f"health route started...")
#     try:
#         return success_responce(message='home call successfully')
#     except Exception as e:
#         LOGGER.info(f"error occured : {str(e)},", exc_info=True)
#         raise e

# @app.route("/home/<name>", methods = ['GET'])
# def user(name):
#     return f"Hello! {name}"

# @app.route("/admin", methods = ['GET'])
# def admin():
#     return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8080,
        debug=True
    )

