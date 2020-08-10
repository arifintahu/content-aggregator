from src.services.news import News
import json
import datetime

def collectNews(portals):
	date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
	contents = []
	for i in portals:
		t = News(i)
		contents.append({
			"source" : i, 
			"news" : t.getNews(10)
		})
	
	output = {"date": date, "contents" : contents}
	with open("data.txt", "w") as outfile:
		json.dump(output, outfile)

	return output