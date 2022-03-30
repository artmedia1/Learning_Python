data_valid = False

while data_valid == False:
    grade1 = input("Type the grade of the first test: ")

    try:
        grade1 = float(grade1)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue #Continues the while loop

    if grade1 < 0 or grade1 > 100:
        print("Grade should be between 0 and 100")
        continue
    else:
       data_valid = True

data_valid = False 

while data_valid == False:
    grade2 = input("Type the grade of the second test: ")
   
    try:
        grade2 = float(grade2)
    except:
        print("Invalid input. Only numbers are accepted. Decimals should be separated with a dot.")
        continue
    
    if grade2 < 0 or grade2 > 100:
        print("Grade should be between 0 and 100")
        continue
    else:
       data_valid = True

data_valid = False 

while data_valid == False:
    total_classes = input("Type the total number of classes: ")
    
    try:
        total_classes = int(total_classes)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue

    if total_classes <= 0:
        print("The number of classes can't be zero or less")
        continue
    else:
       data_valid = True

data_valid = False   

while data_valid == False:
    absences = input("Type the total number of absences: ")
    
    try:
        absences = int(absences)
    except:
        print("Invalid input. Only numbers are accepted.")
        continue

    
    if absences < 0 or absences > total_classes:
        print("The number of absences can't be less than zero or greater than the number of total classes.")
        continue
    else:
       data_valid = True

avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes
print("Average grade: ", round(avg_grade, 2))
print("Attendance rate: ", str(round((attendance * 100),2))+'%')

if (avg_grade >= 60 and attendance >= 0.8):
    print("The student has been approved.")
elif(avg_grade < 60 and attendance < 0.8):
    print("The student has failed due to an average grade lower than 60% and an attendance rate lower than 80%.")
elif(attendance >= 0.8):
    print("The student has failed due to an average grade lower than 60%.")
else:
    print("The student has failed due to an attendance rate lower than 80%.")

if (avg_grade < 60 or attendance < 0.8):
    print("STUDENT HAS FAILED")

# type of number: 30
# The number is:  30.0
# PS C:\Users\randy\Documents\Python> & C:/Python/python.exe c:/Users/randy/Documents/Python/Learning/10-ErrorHandling.py
# type of number: test
# Traceback (most recent call last):
# PS C:\Users\randy\Documents\Python> & C:/Python/python.exe c:/Users/randy/Documents/Python/Learning/10-ErrorHandlingExercise.py
# Type the grade of the first test: -10
# Grade should be between 0 and 100 
# Type the grade of the first test: 110
# Grade should be between 0 and 100 
# PS C:\Users\randy\Documents\Python> & C:/Python/python.exe c:/Users/randy/Documents/Python/Learning/10-ErrorHandlingExercise.py
# Type the grade of the first test: -10
# Grade should be between 0 and 100 
# PS C:\Users\randy\Documents\Python> & C:/Python/python.exe c:/Users/randy/Documents/Python/Learning/10-ErrorHandlingExercise.py
# Type the grade of the first test: -10
# Grade should be between 0 and 100 
# Type the grade of the first test: 110
# Grade should be between 0 and 100 
# Type the grade of the first test: test
# Invalid input. Only numbers are accepted. Decimals should be separated with a dot.
# Type the grade of the first test: 50
# Type the grade of the second test: -10
# Grade should be between 0 and 100  
# Type the grade of the second test: 552
# Grade should be between 0 and 100  
# Type the grade of the second test: test
# Invalid input. Only numbers are accepted. Decimals should be separated with a dot.
# Type the grade of the second test: 75
# Type the total number of classes: -11
# The number of classes can't be zero or less
# Type the total number of classes: test
# Invalid input. Only numbers are accepted.
# Type the total number of classes: 30     
# Type the total number of absences: -30
# The number of absences can't be less than zero or greater than the number of total classes.
# Type the total number of absences: 40
# The number of absences can't be less than zero or greater than the number of total classes.
# Type the total number of absences: test
# Invalid input. Only numbers are accepted.
# Type the total number of absences: 2
# Average grade:  62.5
# Attendance rate:  93.33%
# The student has been approved.