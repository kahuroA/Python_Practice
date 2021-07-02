""" Write a program that stores the values in a dictionary and 
 finds the average of values entered by a user. 
The user will enter 0 to indicate that no further values will be provided. """

#initialize a dictionary to store the values
#The dictionary will have a key named value and the value part will be a list

value_dict={"values":[]}

#from above the list in the value part is empty,
#whatever the user enters will be stored in the list

user=int(input("Enter the value to store:"))

while user!=0:
    #adds the number entered by user in the list
    value_dict["values"].append(user)
    user=int(input("Enter the next value or 0 to finish"))

#After the user finishes entering the numbers, use the list to claculate the average

#calculate average
avg=sum(value_dict["values"])/len(value_dict["values"])

print("The average of entered values is ", avg)
