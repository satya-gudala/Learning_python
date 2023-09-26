'''import datetime
s=datetime.datetime.now()
res=datetime.datetime(2023,8,10,10,16,23,560086)
a=res.strftime("%y")#year short
print(a)
a=res.strftime("%Y")#year log
print(a)
a=res.strftime("%w")#month half number
print(a)
a=res.strftime("%W")
print(a)
a=res.strftime("%a")#day short
print(a)
a=res.strftime("%A")#day full
print(a)
a=res.strftime("%H")#hours long
print(a)
a=res.strftime("%I")#hours short
print(a)
a=res.strftime("%p")#pm/am
print(a)
a=res.strftime("%M")#min
print(a)
a=res.strftime("%S")#sec
print(a)
a=res.strftime("%f")#milli sec
print(a)
a=res.strftime("%b")#month name short
print(a)
a=res.strftime("%B")#month name long
print(a)
a=res.strftime("%d")
print(a)
a=res.strftime("%j")#day of years
print(a)
a=res.strftime("%%")
print(a)
a=res.strftime("%c")#century(all dates weeks months year)
print(a)
a=res.strftime("%x")#present date
print(a)
a=res.strftime("%X")#present time
print(a)
a=res.strftime("%G")#present year
print(a)
a=res.strftime("%u")
print(a)
a=res.strftime("%V")#day of weeks number
print(a)'''

#creating present date():
import datetime
a=datetime.datetime.now()
print(a)
a=datetime.date.today()
print(a)
a=datetime.time()
print(a)
a=datetime.time(20,3,4)
print(a)
print('hr:',20)
print('minut:',3)
print('sec:',4)
#date
a=datetime.date(2002,6,8)
print(a)
print("year:",2002)
print("month:",6)
print("days:",8)

#strftime():
from datetime import date
a=date.today()
print(a)
x=date(22,3,5)
print(x)
from datetime import time
a=time(2,34,56)
print(a)
a=time(2,34,56)
print("hr:",2)
print("min:",34)
print("sec:",56)

#strftime():.................>
#year():>
a=datetime.datetime.today()
s=a.strftime("%y")
print("year:",s)
a=datetime.datetime.today()
s=a.strftime("%Y")
print("year:",s)
#month():...........>
a=datetime.datetime.today()
s=a.strftime("%w")
print("month:",s)
a=datetime.datetime.today()
s=a.strftime("%W")
print("month:",s)
a=datetime.datetime.today()
s=a.strftime("%m")
print("month:",s)
#days():............>
a=datetime.datetime.today()
s=a.strftime("%A")
print("days:",s)
a=datetime.datetime.today()
s=a.strftime("%a")
print("days:",s)
a=datetime.datetime.today()
s=a.strftime("%d")
print("days:",s)
a=datetime.datetime.today()
s=a.strftime("%D")
print("days:",s)
a=datetime.datetime.today()
s=a.strftime("%h")
print("hours:",s)


#hours():........>
a=datetime.datetime.today()
s=a.strftime("%H")
print("hours:",s)
a=datetime.datetime.today()
s=a.strftime("%I")
print("hours:",s)
a=datetime.datetime.today()
s=a.strftime("%p")
print("hours:",s)
#minutes():..........>
a=datetime.datetime.today()
s=a.strftime("%M")
print("minutes:",s)
#seconds():.....>
a=datetime.datetime.today()
s=a.strftime("%S")
print("sec:",s)
a=datetime.datetime.today()
s=a.strftime("%f")
print("SEC:",s)
a=datetime.datetime.today()
s=a.strftime("%c")
print("yeras:",s)
a=datetime.datetime.today()
s=a.strftime("%x")#...........date ony
print("yeras:",s)
a=datetime.datetime.today()
s=a.strftime("%X")#........time ony
print("yeras:",s)
a=datetime.datetime.today()
s=a.strftime("%u")
print("yeras:",s)
a=datetime.datetime.today()
s=a.strftime("%G")#..........year ony
print("yeras:",s)

a=datetime.datetime.today()
s=a.strftime("%V")
print("yeras:",s)
a=datetime.datetime.today()
s=a.strftime("%j")#.........>days number of yeras(000-365)
print("yeras:",s)


































































