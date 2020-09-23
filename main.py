import json
from difflib import get_close_matches

# use to attach json file to your project and save it into any attribute
data = json.load(open("data/data.json"))
# defines new method
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        choice = input("did you mean %s instead? 'Y' for yes 'N' for no: " %get_close_matches(word, data.keys())[0])
    if choice == "Y" or choice == "y":
        return data[get_close_matches(word, data.keys())[0]]
    elif choice =="N" or choice == "n":
        choice = input("did you mean %s instead? 'Y' for yes 'N' for no: " % get_close_matches(word, data.keys())[1])
    else:
        return " we didn't understand your entry."
    if choice == "Y" or choice == "y":
        return data[get_close_matches(word, data.keys())[1]]
    elif choice =="N" or choice == "n":
        choice = input("did you mean %s instead? 'Y' for yes 'N' for no: " % get_close_matches(word, data.keys())[2])
    else:
        return "we didn't understand your entry."
    if choice == "Y" or choice == "y":
        return data[get_close_matches(word, data.keys())[2]]
    else:
        return "the word doesn't exists."
# save input from user to attribute
word = ""
while word != "quit":
    word = input("enter any word or quit to exit program: ")
    while not word.isalpha():
        word = input("please enter only letters: ")
    # prints the returned object from the method
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

