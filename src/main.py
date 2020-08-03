from flask import Flask, render_template, jsonify, request
import os
import json
import datetime

from src.services.content import Content

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
			print(news)
			return jsonify(news)

@app.route("/aggregator", methods=["GET"])
def aggregator():
	if request.method == "GET":
		portals = ["kompas.com", "tempo.co", "detik.com", "suara.com"]
		date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
		contents = []
		for i in portals:
			t = Content(i)
			contents.append({"source" : i, "news" : t.getContent(10)})
		
		output = {"date": date, "contents" : contents}
		with open("data.txt", "w") as outfile:
			json.dump(output, outfile)

		return jsonify(output)


if __name__ == "__main__":
	app.run(debug=True)
