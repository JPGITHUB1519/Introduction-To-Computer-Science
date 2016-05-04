def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
assert isLeapYear(2000) == True
assert isLeapYear(2100) == False
assert isLeapYear(2012) == True
assert isLeapYear(2013) == False

def dateIsBefore (year1, month1, day1, year2, month2, day2):
    '''Returns True if year1-month1-day1 is before year2-month2-day2.
       Otherwise, returns False.'''
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

# modified daysInMonth
def daysInMonth(year, month):
    if month == 2:
        if isLeapYear(year):
            return 29
        return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    else:
        return 31 

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    '''Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar.'''
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    assert nextDay(2013, 4, 30) == (2013, 5, 1)
    assert nextDay(2012, 12, 31) == (2013, 1, 1)
    assert nextDay(2013, 2, 28) == (2013, 3, 1)
    assert daysBetweenDates(2013, 1, 1, 2014, 1, 1) == 365  

    # added tests for leap years
    assert nextDay (2012, 2, 28) == (2012, 2, 29)
    assert daysBetweenDates(2012, 1, 1, 2013, 1, 1) == 366      
    print 'Tests Completed'

test()


print daysBetweenDates(2015,3,3,2015,5,10)