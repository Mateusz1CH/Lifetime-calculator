import datetime
#todays_day = datetime.datetime.now()
todays_day = datetime.date.today()

birth_day = int(input("what is the day you were born?"))
birth_month = int(input("what is the number of the month in which you were born?"))
birth_year = int(input("what is the year you were born?"))

from datetime import date
your_birth_day = date(birth_year, birth_month, birth_day)

#how many days you lived
days_you_lived = todays_day - your_birth_day
days_you_lived = days_you_lived.days

#when you will have 100th birthday
birthday100 = date(birth_year+100, birth_month, birth_day)

#days untill 100th birthday
days_until_100 = birthday100 - todays_day
days_until_100 = days_until_100.days

percent_of_days_you_lived_if100 = (days_you_lived/(birthday100 - your_birth_day).days)*100
percent_of_days_you_lived_if100 = round(percent_of_days_you_lived_if100,2)
print("You lived {} days already. \nThere is {} days left to your 100 birthday.\
      \nYou lived already {}% out of this time".format(days_you_lived, days_until_100, \
          percent_of_days_you_lived_if100))