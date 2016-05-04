""" Days Between days in the same year"""

def leapYear(year1):

    if year1 % 4 == 0 and year1 % 100 != 0  or year1 % 400 == 0:

        return True
    else :

        return False

def daysInMonth(year1,month1) :

    if (month1 == 1 or month1 == 3 or month1 == 5 or month1 == 7 or month1 == 8 or month1 == 10 or month1 == 12 ):

        return 31

    if(month1 == 4  or month1 == 6 or month1 == 9 or month1 == 11):
        return 30

    if month1 == 2 :
        if leapYear(year1) == True :
            return 29
        else :
            return 28

def daysBetweenDates(year1,month1,day1,year2,month2,day2) :

	days = 0
	auxMonth1 = month1 + 1

	days = days + (daysInMonth(year1,month1) - day1)

	while(auxMonth1 < month2) :

		days = days + daysInMonth(year1,auxMonth1)
		auxMonth1 = auxMonth1 + 1

	days = days + day2

	return days

print daysBetweenDates(2012,2,29,2016,12,1)





