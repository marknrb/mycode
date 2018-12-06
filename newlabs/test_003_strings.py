#!/usr/bin/env python3

#initialize you prompt string
prompt_name_msg = "please enter your full name: "


#####################################################
#Use the input function to get the user's name
#####################################################
user_name = input(prompt_name_msg)

#####################################################
# ERROR CHECKING: Check that the user_name is not empty
#####################################################
while (user_name == ''):
	# Prompt the user again for their name
	user_name = input(prompt_name_msg)
#END of the whole loop, for the USER-NAME initialization


#####################################################
#Print out of statement using the user_name variable
#####################################################
print()
print("Welcome to the wornderful world of python, " , user_name)
print()