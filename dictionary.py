import json #import the dictionary definitions and words
from difflib import get_close_matches #module used to find close matches

data = json.load(open("data.json"))

def meaning(w):
    """The main function used to return the meaning of the word entered by the user"""
    w = w.lower()
    if w in data:
        return data[w] #return meaning if it exists in the json file
    elif len(get_close_matches(w, data.keys())) > 0: #if close matches are found
        yn = input("Did you mean %s instead? Enter yes or no: " % get_close_matches(w, data.keys())[0]) #display closest result and ask user if that was their word
        response = yn.lower()
        if response == "yes":
            return data[get_close_matches(w, data.keys())[0]]
        elif response == "no":
            return "The word does not exist, please try again."
        else:
            return "Invalid response."
    else:
        return "The word does not exist, please try again."

word = input("Enter the word whose definition you want \n")
result = meaning(word)
if type(result) == list: #if the definition is to be displayed
    for item in result:
        print(item)
else:
    print(result) #if some user message is to be displayed