def say_hello(person1, person2="The director"): #"The director is the default"
    print("Hello " + person1 + ", how are you doing? " + person2 + " is waiting for you.")
def fahr2celsius(fahr):
    celsius = (5 * (fahr - 32)) / 9
    return celsius

say_hello("Jane")
#Hello Jane, how are you doing? The director is waiting for you.

say_hello("Jane", "Tim")
#Hello Jane, how are you doing? Tim is waiting for you.