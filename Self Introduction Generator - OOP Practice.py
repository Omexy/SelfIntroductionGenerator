#Imports the time module
import time
#This section is just the introduction of the program with slight delays for highlighting each section
print("Self-Introduction Generator \n")
time.sleep(0.5)
print("A simple and easy-to-use program using OOP which generates a self-introduction for anyone. \n")
time.sleep(1)
print("Please use lower-case to respond apart from proper nouns to ensure correct compilation. \n")
time.sleep(0.5)

#These variables store the user's responses for each question
PName = input("What is your name? ")
PLocation = input("Where are you from? ")
PAge = input("How old are you in years? ")
PGender = input("What is your gender? ")
PHobbies = input("What are your hobbies? What things do you like doing? ")

#Creates a class for the person's attributes for the self-introduction
class Person:
  #Defines a function to add common attributes such as name, location etc.
  def __init__(self, name, location, age, gender, hobbies):
    self.name = name
    self.location = location
    self.age = age
    self.gender = gender
    self.hobbies = hobbies
  #Defines a function to add all attributes into a compiled SI with basic phrasing
  def __str__(self):
    return f"\nSelf-Introduction:\nHey, nice to meet you. My name is {self.name}. I am {self.age} years old and I am from {self.location}. I enjoy doing many different things, such as {self.hobbies}. If you didn't know already, I am {self.gender}.\n"

FinalSI = Person(PName, PLocation, PAge, PGender, PHobbies)

# Prints the string representation of the self-introduction object
print(str(FinalSI))