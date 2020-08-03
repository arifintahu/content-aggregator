import requests

from bs4 import BeautifulSoup
import re

class Content():
	def __init__(self, url):
		self.url = "https://www." + url
		self.match_url = "("+url+"/)*[a-z]+"
		r = requests.get(self.url)
		self.soup = BeautifulSoup(r.content, "html5lib")

	def getContent(self, limit):
		contents = self.soup.find_all("a", href=True)
		news = []
		for item in contents:
			url_match = re.match(self.match_url, item['href'])
			clean_text = re.sub("\s+", " ", item.get_text()).strip()
			text_len = len(clean_text)

			if(url_match and text_len>25):
				news.append({ "title": clean_text, "url": item['href']})

		return news[0:limit]