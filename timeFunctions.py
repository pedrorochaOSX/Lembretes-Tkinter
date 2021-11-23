from datetime import datetime


def getTime():
	now = datetime.now()
 
	dt_string = now.strftime("%d/%m/%Y   %H:%M")
	return dt_string



