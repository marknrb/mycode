#!/usr/bin/env python3

# Initialize a dictionary of phone numbers / names
# Here the person's name is the key
phone_dict = {
    'Don Hill': ['4042736081', 'GA'],
    'Amy Allen': ['2144068689', 'TX'],
    'Dan Martin': ['6825147059','FL'],
    'Eric Forbes': ['8668998998','NJ'],
    'Mark Bennett':['8009220204','CA'],
}

print()
print("The Phone Dictionary. . .")
print(phone_dict)

##################################################################### 
# Acesss one individual item in the dictionary
#NOTE that user_name is the used as the "key" to look in the dictionary
##################################################################### 
user_name = "Eric Forbes"
print("The phone number for ", user_name, "is" , phone_dict[user_name][0])
print("The state for ", user_name, "is", phone_dict[user_name][1])
print()


###################################
# Ask the user for a person's name
###################################
input_name = input("Please enter a person's name:")
print("The phone number for", input_name, "is", phone_dict[input_name][0])
print()

##################################################################### 
# Access each item in the dictionary
# NOTE that you can select meaningful names to describer your key/value pairs
##################################################################### 
#for full_name, phone_info in phone_dict.items():
#    print("The phone number for", full_name, "is", phone_info[0])
#    print("The phone location is ", phone_info[1])
#    print()
