# import necessary libraries
from flask import Flask, render_template,redirect
from flask_pymongo import PyMongo
import mission_to_mars

# create instance of Flask app

app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

@app.route("/")
def index():
    mars_info = mongo.db.mars_info.find_one()
    return render_template("index.html", mars_info=mars_info)


@app.route("/scrape")
def scraper():
    mars_info = mongo.db.mars_info
    mars_data = mission_to_mars.scrape_fn()
    mars_info.update({}, mars_data, upsert=True)
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)

