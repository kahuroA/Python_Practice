
#prompts user to input value and converts it into an integer
user=int(input("Enter wavelength to check color:"))
#checks if the enterd value is between 380 and 450
if user>=380 and user<=450:
    print("The color is violet")
#checks if the entered value is between 450 and 495
elif user>=450 and user<=495:
    print("The color is blue")
#checks if the entered value is between 495 and 570
elif user>=495 and user<=570:
    print("The color is green")
#checks if the entered value is between 570 and 590
elif user>=570 and user<=590:
    print("The color is yellow")
#checks if the entered value is between 590 and 620
elif user>=590 and user<=620:
    print("The color is orange")
#checks if the entered value is between 620 and 750
elif user>=620 and user<=750:
    print ("color is red")
#If all the checks above fail, the program runs the else statement below
else:
    print("Unknown color wavelength")
