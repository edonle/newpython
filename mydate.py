import datetime
currentDate = datetime.date.today()
print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)
print(currentDate.strftime('%d %b, %Y'))
print(currentDate.strftime('%A, %B %d do ano de  %Y'))

