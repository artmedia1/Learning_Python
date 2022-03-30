# Create a program to help the user type faster. Give him a word and
# ask him to write it five times. Check how many seconds it took him to
# type the word at each round.
# In the end, tell the user how many mistakes were made and show a
# chart with the typing speed evolution during the 5 rounds.

import time as t
import matplotlib.pyplot as plt

desiredString = str(input("This program will help you type faster, you will be required to type it five times. please enter the string you wish to type: "))

print("Please enter the string")

def CheckMistakes(userInput, desiredString = desiredString):
    mistakeCounter = 0
    userInputList = userInput.split(" ")
    desiredStringList = desiredString.split(" ")
    for i in range(len(desiredStringList)):
        if (userInputList[i] != desiredStringList[i]):
            mistakeCounter+= 1
            
    return mistakeCounter    

x_axis = [1, 2, 3, 4, 5]
y_axis = []
totalMistakes = 0
total_Time = 0
for i in range(5):
    start_time = t.time()
    userInput = str(input("Attempt " + str(i+1) + ": "))
    end_time = t.time()
    elapsed_time = end_time - start_time
    total_Time += elapsed_time
    y_axis.append(elapsed_time)
    

    mistakes = CheckMistakes(userInput)
    totalMistakes += mistakes
    print("Mistakes made: ", mistakes)

average_Time = round(total_Time/5,2)

print("You've made a total of " + str(totalMistakes) + " mistakes")
print("Your average time is: " + str(average_Time) + " seconds")

plt.plot(x_axis,y_axis)
plt.ylabel("Attemp time in seconds")
plt.title("Your typing evolution")
plt.show()