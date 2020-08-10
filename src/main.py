from flask import Flask, render_template, jsonify, request
import os
import json
import datetime

from src.services.servicenews import collectNews
from src.services.servicecontent import getContent


class CustomFlask(Flask):
	jinja_options = Flask.jinja_options.copy()
	jinja_options.update(dict(
		variable_start_string='%%',
		variable_end_string='%%',
	))

app = CustomFlask(__name__)

@app.route("/", methods=["GET"])
def index():
	if request.method == "GET":
		return render_template("main/index.html")
			
@app.route("/news", methods=["GET"])
def news():
	if request.method == "GET":
		with open('data.txt') as json_file:
			news = json.load(json_file)
			return jsonify(news)

@app.route("/aggregator", methods=["GET"])
def aggregator():
	if request.method == "GET":
		portals = ["kompas.com", "tempo.co", "detik.com", "suara.com"]
		output = collectNews(portals)
		return jsonify(output)

@app.route("/news/content", methods=["POST"])
def content():
	if request.method == "POST":
		data = request.get_json()
		url = data.get('url')
		output = getContent(url)
		return jsonify(output)

if __name__ == "__main__":
	app.run(debug=True)
