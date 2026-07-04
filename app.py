import os  # noqa: F401
from flask import Flask, render_template, request  # noqa: F401
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
#Routing
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/weblink")
def weblink():
    return "SUCCESS", 200

@app.route("/pricing")
def pricing():
    return render_template("pricing.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/order-services")
def orders():
    return render_template("orders.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)