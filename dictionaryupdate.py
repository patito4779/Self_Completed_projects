
class Person:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age
    def printName(p):
        print("This is the way " + p.fname + str(p.age))

p1 = Person("Patrick", "Okwe", 34)
print(p1.printName())

class Student(Person):
    def __init__(self, fname, lname, age,  year):
        super().__init__(fname, lname, age)
        self.graduationYear = year

    def welcome(self):
        print("Welcome", self.fname, self.lname, " to the class of",
         self.graduationYear)

y = Student("Mike", "Ogbakpah", 45, 2019)

print(y.welcome())


string = "patrick"


# a simple code to return the number of letters in a string to a dictionary as key value pair

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result
print(count_letters("alfkdjfdfjjfdkaaa"))



# Counting the number of letters in a dictionary excluding symbols and reading capital letters as small letters
def count_letters(text):
  result = {}
  # Go through each letter in the text
  for letter in text:
    if letter.isalpha() == False:
      exit
    

    else:
      if letter.isupper():
        letter = letter.replace(letter, letter.lower())
    
      if letter not in result:
        result[letter] = 0
      result[letter] += 1                
    # Check if the letter needs to be counted or not
    #
    # Add or increment the value in the dictionary
    
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

