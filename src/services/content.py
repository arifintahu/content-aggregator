import requests

from bs4 import BeautifulSoup
import re

class Content():
	def __init__(self, url):
		self.url = url
		r = requests.get(self.url)
		self.soup = BeautifulSoup(r.content, "html5lib")

	def getText(self):
		paragraphs = self.soup.find_all("p")
		texts = []
		for i in paragraphs:
			text = i.get_text()
			text = text.replace(u'\xa0', u'')
			text = re.sub("\s+", " ", text.strip())
			if len(text)>1:
				texts.append(text)

		return texts