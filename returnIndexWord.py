


def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
        result = "".join(result)
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS


# Palindrome

def is_palindrome(input_string):
	input_string = input_string.replace(" ", "")
	print(input_string.lower()[::-1])
	return (input_string.lower() == input_string.lower()[::-1]) 

#format statemnts

def convert_distance(miles):
	km = miles * 1.6 
	result = "{} miles equals {:.1f} km".format(miles, km)
	return result
print(convert_distance(12)) # Should be: 12 miles equals 19.2 km


def nametag(first_name, last_name):
	return("{}, {}.".format(first_name, last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 



# Replace word endings python code( checking if the end of the sentence is same as "old" and replacing with "new")
def replace_ending(sentence, old, new):
	# Check if the old string is at the end of the sentence 
	sentence = sentence.split()
	old = old.split()
	new = new.split()
	new_sentence = " "
	for word in old:
		for words in new:
			if (sentence[-1] == word):
				new_sentence = new_sentence.join(sentence[0:-1] + new)
			else:
				new_sentence = new_sentence.join(sentence)
			return new_sentence
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

# Converting a list to a string
start_list = ["using", "list", "comprehension"]
string = " ".join(start_list)
print(string)

# List comprehension allows the creation of a new list in just one line of code as shown below
multiples = [x*10 for x in range(1, 11)]
print(multiples)


# A code that replace ".hpp" extensions with ".h"
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]

newfilenames = []
for names in filenames:
    if ".hpp" in names:
        filename = names.replace(".hpp", ".h") 
        newfilenames.append(filename)
    else:
        newfilenames.append(names)
        
    

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]


# Code for convrting octal to string to define permissions in linux systems file groups

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for digits in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if digits >= value:
                result += letter
                digits -= value
            else:
                result += "-"
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------



def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)



# Updating a dictionary such that the first dictionary takes precedence over the second one
def combine_guests(guests1, guests2):
  
  dict3 = {**guests2, **guests1}
  return dict3

Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
print(combine_guests(Rorys_guests, Taylors_guests))




def format_address(address_string):
  # Declare variables
  address = address_string.split()
  

  # Separate the address string into parts

  # Traverse through the address parts
  for parts in address:
    
    # Determine if the address part is the
    # house number or part of the street name

  # Does anything else need to be done 
  # before returning the result?
  
  # Return the formatted string  
    return "house number {} on street named {}".format(address[0], " ".join(address[1:]))

print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"


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

