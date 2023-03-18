import os
import string

def convert_to_leet(word):
    leet_word = ""
    for character in word:
        if character.lower() == "a":
            leet_word += "4"
        elif character.lower() == "b":
            leet_word += "8"
        elif character.lower() == "e":
            leet_word += "3"
        elif character.lower() == "g":
            leet_word += "9"
        elif character.lower() == "i":
            leet_word += "1"
        elif character.lower() == "l":
            leet_word += "1"
        elif character.lower() == "o":
            leet_word += "0"
        elif character.lower() == "s":
            leet_word += "5"
        elif character.lower() == "t":
            leet_word += "7"
        elif character.lower() == "z":
            leet_word += "2"
        else:
            leet_word += character
    return leet_word

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name")
dog_name = input("Please enter the name of your dog: ")
dob = input("Please enter your date of birth in dd/mm/yyyy format: ")
partner_name = input("Please enter your partner's name: ")

wordlist = list()
wordlist.append(first_name + dog_name)
wordlist.append(first_name + partner_name)
wordlist.append(dog_name + partner_name)
wordlist.append(last_name + "@123")
wordlist.append(first_name + "@123")

day = dob.split("/")[0]
month = dob.split("/")[1]
year = dob.split("/")[2]

month_strings = ["january", "february", "march", "april", "may", "june",
                 "july", "august", "september", "october",
                 "november", "december"]

wordlist.append(first_name + "@" + day + month )
wordlist.append(first_name + day + month_strings[int(month)-1] + year)
wordlist.append(last_name + day + month_strings[int(month)-1] + year)
wordlist.append(dog_name + day + month_strings[int(month)-1] + year)
wordlist.append(partner_name + day + month_strings[int(month)-1] + year)

capital_words = list(map(lambda s: s.capitalize(), [word for word in wordlist]))
wordlist.extend(capital_words)

leet_words = list()
for word in wordlist:
    leet_words.append(convert_to_leet(word))

wordlist.extend(leet_words)

name, ext = os.path.splitext(os.path.basename(dob))
wordlist_file = open(name + "_wordlist.txt", "w")
for word in wordlist:
    wordlist_file.write(word + "\n")
wordlist_file.close()

print("Wordlist saved as: " + name + "_wordlist.txt")
