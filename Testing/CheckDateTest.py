import datetime


def checkDate(date):
    try:
        date = datetime.datetime.strptime(date, '%d/%m/%Y')
        return True

    except Exception as e:
        return False

#Normal Expected Date
print(checkDate("12/10/2020"))

#Normal Date But in Different format (one we dont want)
print(checkDate("12/10/20"))

#Overflow date
print(checkDate("12/15/2020"))

#Wrong way round (silly americans)
print(checkDate("12/24/2020"))

#Without Slashes
print(checkDate("24 12 2020"))

#Random String
print(checkDate("Hello World"))

#Empty String
print(checkDate(""))