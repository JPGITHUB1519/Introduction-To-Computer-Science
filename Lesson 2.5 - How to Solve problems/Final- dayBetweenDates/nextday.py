
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


print nextDay(2015,5,29)