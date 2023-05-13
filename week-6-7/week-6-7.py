from flask import Flask, render_template

app = Flask(__name__)

# basic routing
@app.route("/")
def index():
    return render_template("home.html")

@app.route("/tambah-elemen")
def add_els():
    return render_template("add-els.html")


@app.route("/about")
def about_page():
    return "This is about page!"

# routing with variable
@app.route("/account/<string:name>/<int:age>")
def user_page(name, age):
    status = "allowed" if age > 18 else "not allowed"
    return f"hello {name}, you are {status}"

# render templates
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/dynamic")
def dynamic_html():
    return render_template("dynamic.html", title="dynamic title", message="dynamic message")

# url building

# HTTP methods
# GET: meminta data dari server
# POST: mengirimkan data ke server untuk diproses
#
#


# static files

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)