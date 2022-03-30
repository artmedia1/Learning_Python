#1) Create a program that asks the user for his birthday in the format
#"DD-MM-YYYY". Then print:
#"You were born in [month]"
#example: "You were born in January"

months = ("January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
          "August",
          "September",
          "October",
          "November",
          "December")

birthday = input("Please enter your birthday in the format: MM-DD-YYYY: ")

print(birthday)
print(birthday[0:2])

month = int(birthday[0:2]) - 1
print(month)

print("You were born in: " + months[month])