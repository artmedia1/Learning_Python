#1) Create a program that asks the user for his first name, his middle name and his last name. Then print:
#"Your initials are _ _ _ "


first_name = input("What is your first name?")
middle_name = input("What is your middle name?")
last_name = input("What is your last name?")

if(middle_name != ""):
    initials = first_name[0] + middle_name[0] + last_name[0]
else:
    initials = first_name[0] + last_name[0]
    
print("Your initials are:" + initials)