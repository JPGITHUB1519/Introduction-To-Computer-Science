# Write a procedure download_time which takes as inputs a file size, the
# units that file size is given in, bandwidth and the units for
# bandwidth (excluding per second) and returns the time taken to download 
# the file.
# Your answer should be a string in the form
# "<number> hours, <number> minutes, <number> seconds"

# Some information you might find useful is the number of bits
# in kilobits (kb), kilobytes (kB), megabits (Mb), megabytes (MB),
# gigabits (Gb), gigabytes (GB) and terabits (Tb), terabytes (TB).

#print 2 ** 10      # one kilobit, kb
#print 2 ** 10 * 8  # one kilobyte, kB

#print 2 ** 20      # one megabit, Mb
#print 2 ** 20 * 8  # one megabyte, MB

#print 2 ** 30      # one gigabit, Gb
#print 2 ** 30 * 8  # one gigabyte, GB

#print 2 ** 40      # one terabit, Tb
#print 2 ** 40 * 8  # one terabyte, TB

# Often bandwidth is given in megabits (Mb) per second whereas file size 
# is given in megabytes (MB).

#function to convert seconds in hour, minute, seconds
def convert_seconds(time):
    
    #converting to hours, minutes and seconds
    hour =  int(time / 3600)
    time = time % 3600
    minute = int(time / 60)
    time = time % 60
    seconds = time
    
    #checking to write in letters
    if hour == 1 :
        
        string_hora = str(hour) + " hour"     
    else :
        
        string_hora = str(hour) + " hours"
    
    if minute == 1 :
        
        string_minuto = str(minute) + " minute"
    
    else :
        
        string_minuto = str(minute) + " minutes"
    
    if seconds == 1 :
        
        string_segundo = str(seconds) + " second"
    
    else :
        
        string_segundo = str(seconds) + " seconds"
    
 

    string_tiempo = string_hora +  ", " + string_minuto + ", " + string_segundo
    
    return string_tiempo

#convets into bints
def convertsInBits(size,unit) :

	if unit == "kb" :

		return size * (2**10)

	if unit == "kB" :

		return size * (2**10) * 8

	if unit == "Mb" :

		return size * (2**20)

	if unit == "MB" :

		return size * (2 ** 20) * 8

	if unit == "Gb" :

		return size * (2**30)

	if unit == "GB" :

		return size * (2 ** 30) * 8

	if unit == "Tb" :

		return size * (2**40)

	if unit == "TB" :

		return size * (2**40) * 8

#main function
def download_time(filesize,unit1,bandwidth,unit2):

	tam_file = convertsInBits(filesize,unit1)
	tam_band = convertsInBits(float(bandwidth), unit2)

	time = tam_file / tam_band

	return convert_seconds(time)
	




print download_time(11,"GB",5,"MB")

print download_time(1024,'kB', 1, 'MB')
#>>> 0 hours, 0 minutes, 1 second

print download_time(1024,'kB', 1, 'Mb')
#>>> 0 hours, 0 minutes, 8 seconds  # 8.0 seconds is also acceptable

print download_time(13,'GB', 5.6, 'MB')
#>>> 0 hours, 39 minutes, 37.1428571429 seconds

print download_time(13,'GB', 5.6, 'Mb')
#>>> 5 hours, 16 minutes, 57.1428571429 seconds

print download_time(10,'MB', 2, 'kB')
#>>> 1 hour, 25 minutes, 20 seconds  # 20.0 seconds is also acceptable

print download_time(10,'MB', 2, 'kb')
#>>> 11 hours, 22 minutes, 40 seconds  # 40.0 seconds is also acceptable


