
time = 7261.7

hour =  int(time / 3600)

time = time % 3600


minute = int(time / 60)
print minute

time = time % 60

seconds = time

string_tiempo = str(hour) +  ":" + str(minute) + ":" + str(seconds) 

print string_tiempo
