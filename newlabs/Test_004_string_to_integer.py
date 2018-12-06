#!/usr/bin/env python3

#initialize you prompt string
prompt_age_msg = "Please enter your age"

##########################################
# Prompt the user for their age
#... Because teh input funcation returns a string value
#... We are converting the string value to an integer value
##########################################
user_age = int(input(prompt_age_msg))

##########################################
#NOTE that if the user enters a STRING value, the int funcation above returns an error!
##########################################

#ERROR CHECKING:	Checking that the user_age is over 0
while (user_age <= 0):
	#Prompt the user again for their age
	user_age = input(prompt_age_msg)
#END of while loop, for the USER-AGE initialization

##########################################
#Print out a statement using the user_age variable 
##########################################
print()
print("your age is: " , user_age , "years old.")
print()
