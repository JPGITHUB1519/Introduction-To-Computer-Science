
def  nextDay(year1, month1, day1):

    if(day1 < 30):
        day1 = day1 + 1
        return year1, month1, day1
    else:
        if(day1 == 30 and month1 == 12):
            year1 = year1 + 1
            month1 = 1
            day1 = 1
            return year1, month1, day1
        
        else: 
            month1 = month1 + 1
            day1 = 1
            return year1, month1, day1

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

def daysBetweenDates(year1,month1,day1,year2,month2,day2):

    days = 0

    while(dateIsBefore(year1,month1,day1,year2,month2,day2)):

        days = days + 1

        year1, month1, day1 = nextDay(year1,month1,day1)


    return days


print daysBetweenDates(2015,12,15,2015,12,16)

