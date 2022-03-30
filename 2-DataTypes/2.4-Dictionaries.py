person = {"first_name": "John", "last_name": "Green", "birth_year": 1980, "country of birth": "Canada"}
print(person)
print(type(person))

print(person["first_name"])
print(person["birth_year"])

person["children"] = ["Natalie", "Ethan"]
person["children"].append("Anna")

print(person.get("children", "invalid property"))  #If there is no property called age, it will return "invalid property"

print(person.get("age", "invalid property"))

Key = "first_name"

print(person[Key])

person.clear()#Clears dictionary

print(person)

