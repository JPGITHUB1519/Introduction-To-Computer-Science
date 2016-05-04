# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.

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

def  nextDay(year1, month1, day1):

    if(day1 < (daysInMonth(year1,month1))):
        day1 = day1 + 1
        return year1, month1, day1

    else:
        if(day1 == (daysInMonth(year1,month1)) and month1 == 12):
            year1 = year1 + 1
            month1 = 1
            day1 = 1
            return year1, month1, day1
        
        else: 
            month1 = month1 + 1
            day1 = 1
            return year1, month1, day1

def daysBetweenDates(year1,month1,day1,year2,month2,day2):

    assert dateIsBefore(year1,month1,day1,year2,month2,day2)
    days = 0

    while(dateIsBefore(year1,month1,day1,year2,month2,day2)):

        days = days + 1

        year1, month1, day1 = nextDay(year1,month1,day1)


    return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

print daysBetweenDates(2012,2,29,2016,1,1)
print daysBetweenDates(2011,1,1,2012,8,8)