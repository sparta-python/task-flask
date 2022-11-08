from flask import Flask
from flask import render_template
import image

app = Flask(__name__)


@app.route("/")
def method_name():
    return render_template("index.html")


@app.route("/img")
def kanta():
    image.make()
    return render_template("image.html")


app.run(debug=True)
