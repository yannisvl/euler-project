weekdays = [0, "Monday", "Tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
weekcounter = 0
total = 0
monthdays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
year = 1900
while year < 2001:
    if year%400 == 0 or (year%4==0 and year%100!=0):
        monthdays[1] = 29
    else :
        monthdays[1] = 28
    for i in range(12):
        for monthcounter in range(1, monthdays[i]+1):
            if weekcounter == 7:
                weekcounter = 1
            else:
                weekcounter = weekcounter + 1
            if monthcounter==1 and weekcounter == 7 and year>1900:
                total += 1
            #print(weekdays[weekcounter], monthcounter, "/", i+1, "/", year)
    year += 1
print(total)
