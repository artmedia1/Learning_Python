#   number = float (input("type of number: "))
#
# With the code above, if we type a string for the input there (e.g "test") and we see that we get the error:
#
#   Traceback (most recent call last):
#     File "c:\Users\randy\Documents\Python\Learning\10-ErrorHandling.py", line 1, in <module>
#       number = float (input("type of number"))
#   ValueError: could not convert string to float: 'test'

number = input("Type a number: ")

try:
    number = float(number)
    print("The number is: ", number)
except:
    print("Invalid Number")

