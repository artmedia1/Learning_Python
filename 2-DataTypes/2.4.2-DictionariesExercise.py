#Create a program with a predefined dictionary for a person. Include the following information: name, gender, age, address and phone. 
#Ask the user what information he wants to know about the person (example: "name"), then print the value associated to that key or display a message in case the key is not found.
#I just decided to do a list of dictionaries for fun

personList = []

person = {"first_name": "John", "last_name": "Green", "birth_year": 1980, "country_of_birth": "Canada"}
personList.append(person)
person = {"first_name": "Joseph", "last_name": "Blue", "birth_year": 1990, "country_of_birth of birth": "Canada"}
personList.append(person)
person = {"first_name": "Jane", "last_name": "Red", "birth_year": 2000, "country_of_birth": "Canada"}
personList.append(person)
person = {"first_name": "Joe", "last_name": "White", "birth_year": 2010, "country_of_birth": "Canada"}
personList.append(person)
person = {"first_name": "Johnson", "last_name": "Brow", "birth_year": 2020, "country_of_birth": "Canada"}
personList.append(person)

#for i in personList:
#    print(i["first_name"])
def getDetails(selector):
    for i in personList:
        if (i["first_name"].lower() == selector["first_name"].lower()):
            if(selector["detail_requested"] == 1):
                return i["first_name"]
            elif(selector["detail_requested"] == 2):
                return i["last_name"]
            elif(selector["detail_requested"] == 3):
                return i["birth_year"]
            elif(selector["detail_requested"] == 4):
                return i["country_of_birth"]
            else:
                return "Please enter a valid selection"  
    return "This person is not in the database"      

personRequested = input("What is the first name of this person?: ")
detailRequested = int(input("What information do you want to know?\nEnter:\n1: First Name\n2: Last Name\n3: Birth Year\n4: Country of Birth\n"))

selector = {"first_name": personRequested, "detail_requested": detailRequested}

print(getDetails(selector))



    


