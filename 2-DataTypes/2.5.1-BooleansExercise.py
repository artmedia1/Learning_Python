#Create a program and store your age in a variable. Then, ask the user for his age and print whether:
#   - He's older than you
#   - He's younger than you
#   - You two have the same age

my_age = 32
user_age = int(input("Type your age: "))

if (user_age > my_age):
    print("You're older than me")
elif (user_age == my_age):
    print("We are the same age")
else: 
    print("You're younger than me")