import schedule
import time

from src.main import app
from src.services.servicenews import collectNews

def job():
	portals = ["kompas.com", "tempo.co", "detik.com", "suara.com"]
	output = collectNews(portals)
	print('Job done')

schedule.every(30).minutes.do(job)    

if __name__ == "__main__": 
	app.run(debug=True)
	while 1:
		schedule.run_pending()
		time.sleep(1)