from src.services.content import Content

def getContent(url):
	content = Content(url)
	output = {"texts" : content.getText()}
	return output