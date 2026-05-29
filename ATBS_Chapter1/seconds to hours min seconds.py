sec=float(input("Enter number of seconds: "))
hour=sec//3600
remainingsec=sec%3600
min=remainingsec//60
remainingsec=remainingsec%60
time=str(hour)+" hrs "+str(min)+" mins "+str(remainingsec)+" secs"
print(time)