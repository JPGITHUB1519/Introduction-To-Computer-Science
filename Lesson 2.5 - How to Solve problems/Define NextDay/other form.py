def nextDay(year, month, day):

	if day < 30 :

		return year, month, day + 1

	else :

		if month < 12 :

			return year, month + 1, 1

		else :


			return year + 1, 1, 1



print nextDay(1999, 12, 30) 
print nextDay(2013, 1, 30)
print nextDay(2012, 12, 30) 
print nextDay(2015,1,16)


