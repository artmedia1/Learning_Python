students = ["John", "Mary", "Steve"]
type(students)
len(students)
print(students[0])
print(students[-1])
print(students[:2])
students[0] = "Jordan"
students.append("Kate")
print("ln 9: " + str(students))
students.insert(1,"Peter")
print(students)
students.pop()
print(students)

students.pop(1)
print(students)
students.append("Mary")
print(students)
students.remove("Mary") #If there are two people named Mary in the list, only the first one will be removed
print(students)

students2 = ["Paul", "George"]
students + students2
print(students)
print(students2)
print(students + students2) #You can merge tuples as well, but you cannot merge a list and tuple

#Tuples are like strings but are immutable, for e.g a list of months, it never changes so we should use a tuple
months = ("January", "February", "March")
print(months[0])
print(months[-1])
print(months[:2])