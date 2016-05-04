def dateIsBefore(year1,month1,day1,year2,month2,day2 ):

	if year1 < year2 :

		return True

	if year1 == year2 :

		if month1 < month2 :

			return True

		if month1 == month2 :

			if day1 < day2 :

				return True

	return False
		

print dateIsBefore(2015,12,30,2015,12,31)






