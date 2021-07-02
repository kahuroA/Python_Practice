"""#Assuming you have a list containing holidays
holidays=['february 14', 'may 1', 'june 1', 'october 20']
#initialized a list with holiday names that match the holidays list
holiday_name=['Valentines', 'Labour Day', 'Mashujaa']
#prompt user to enter month and date
month_date=input('enter month name and date')
#check if the entered string is in our list of holidays
if month_date in holidays:
    #get the index of the month date in holiday list
    idx=holidays.index(month_date)
    #use that index to get the holiday name from holiday_name list
    print(holiday_name[idx])
else:
    print('entered month and date do not correspond to a holiday')"""
holidays=['02-14','05-1','10-20']
holiday_name=['Valentines', 'Labour Day', 'Mashujaa']
#prompt user to enter month and date
month_date=input('enter month name and date')
#check if the entered string is in our list of holidays
if month_date in holidays:
    #get the index of the month date in holiday list
    idx=holidays.index(month_date)
    #use that index to get the holiday name from holiday_name list
    print(holiday_name[idx])
else:
    print('entered month and date do not correspond to a holiday')

