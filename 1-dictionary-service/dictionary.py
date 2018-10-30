# import json for handling the data.json file which is the dictionary
import json
# difflib is for suggesting similar words entered giving room for human error i.e. Dogg - Did you mean 'Dog'?
from difflib import SequenceMatcher as sm, get_close_matches as gcm

# this prints out the ratio or how similar the words are, 1 meaning they are identical
# print(sm(None, 'Dogg', 'Dog').ratio())

# returns the closes word to the first argument 'dogg' based off of the 3 words given
# gcm(word entered, possible words, number of possible words = 3, similarity cut off point=0.8)
# print(gcm('dogg',['cat', 'mouse', 'dog']))

# open the json file in read mode and store it in a dictionary - key: value
data = json.load(open('data.json', 'r'))

# test the dictionary by checking the key 'rain'
# print(data["rain"])

def main():

    # enter the word - after entered print what's returned from the word being passed into 'translate'
    word = input('Enter word: ')
    output = translate(word)

    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)
def translate(word):

    word = word.lower()
    if word in data:
        # if the word exists in data, return the value of the key or 'word' entered
        return data[word]
    # if the length of data.keys is greater than 0, then they entered a typo because it has some similarity to a word
    elif len(gcm(word, data.keys())) > 0:
        # allow the user to correct themselves if they enter a typo by suggesting a word
        typo =  input('Word does not exist. Did you mean %s? (Y/N): ' % gcm(word, data.keys())[0])
        typo = typo.lower()
        if typo == 'y':
            return data[gcm(word, data.keys())[0]]
            # return ('Word does not exist. Did you mean ' +  gcm(word, data.keys())[0] + '?')
        elif typo == 'n':
            return 'Word does not exist.'
        else:
            return 'You did not enter Y or N. Exiting.'
    else:
        # otherwise, this error will pop up and the word at the first index [0] will pop up as a suggestion
        return ('Word does not exist.')        


if __name__ == '__main__':
    main()