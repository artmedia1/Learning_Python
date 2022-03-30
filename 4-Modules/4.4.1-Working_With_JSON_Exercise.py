# Create a quizzing game. Make an HTTP request to the Open Trivia API at each round of the game to get a new question and present it to theuser to answer. 
# At the end of each round ask the user if he wants to play again. Keep playing forever until the user types "quit".
# * Don't forget to tell if the answer is correct or not at each round and keep the user's score.
from email.utils import localtime
import requests
import json
import pprint
import random
import html
import time as t

quit = False
score = 0
while quit == False:

    r = requests.get("https://opentdb.com/api.php?amount=1")
    query = json.loads(r.text)
    # pprint.pprint(query)

    incorrectAnswer = query['results'][0]['incorrect_answers']
    correctAnswer = query['results'][0]['correct_answer']
    answersToDisplay = incorrectAnswer
    answerIndex = int(random.uniform(0, 3))
    answersToDisplay.insert(answerIndex,correctAnswer)
    question = query['results'][0]['question']

    print(html.unescape(question))

    for i in range(len(answersToDisplay)):
        print(str(i+1) + "-" + html.unescape(answersToDisplay[i]))

    data_valid = False
    while data_valid == False:
        answer = input("Please enter your answer between 1 and " + str(len(answersToDisplay)) + "\n" )
        print("")

        try:
            answer = int(answer)
        except:
            print("Invalid input. Only numbers are accepted.")
            continue #Continues the while loop

        if answer < 1 or answer > len(answersToDisplay):
            print("Answer should be between 1 and " + str(len(answersToDisplay)))
        elif (answer - 1) == answerIndex:
            print("")
            print("Correct!")
            score += 1
            print("Your score is: " + str(score))
            print("") 
            data_valid = True
        else:
            print("")
            print("Incorrect")
            print("The correct answer was: " + html.unescape(correctAnswer))
            print("Your score is: " + str(score))
            print("")
            data_valid = True



    if (input("Would you like to quit? Please enter 'quit' to play quit the game, otherwise enter anything else to restart the game \n") == "quit"):
        quit = True
        print("")
        print("Your final score was: " + str(score))
        print("The game will close in 3 seconds")
        timeEnd = t.time() + 3
        countDown = 3
        while (int(t.time()) != int(timeEnd)):
            print(countDown)
            countDown -= 1
            t.sleep(1)
        