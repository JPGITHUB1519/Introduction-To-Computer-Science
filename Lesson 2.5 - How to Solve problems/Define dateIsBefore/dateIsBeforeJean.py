def dateIsBefore(year1,month1,day1,year2,month2,day2):
    
    date1_value = year1 * 365 + month1 * 30 + day1 * 1
    
    date2_value = year2 * 365 + month2 * 30 + day2 * 1
    
    if(date1_value < date2_value):
        
        return True
    else :
        
        return False
    

print dateIsBefore(2015,8,4,2015,8,5)