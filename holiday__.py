# Create a dictionary of kenyan holiday names & corressponding dates 
Kenyan_holidays = {'Labour_Day' : '01/05', 
                 'Madaraka_Day' : '01/06', 
                 'Moi_Day' : '10/10', 
                 'Kenyatta_Day' : '20/10', 
                 'Jamuhuri_Day' : '12/12'}
                 
# Ask for an input from user
date = input('Enter a date in the DD/MM format: ')
for key, value in Kenyan_holidays.items(): # iterates through dict items
  if date in value:
      print(key)
      break
  else:
      continue
print(date)
    # evaluates if user input matches any value in dict
    
