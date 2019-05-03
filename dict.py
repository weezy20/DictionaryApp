import json
import difflib
data  = json.load(open("data.json","r"))
def wordMeaning(word):
    return data[word]
while True:
    word = input("\n\nEnter a word or press 0 to exit\n\n")
    if word != str(0):
        if word.lower() in data:
            print(wordMeaning(word))
        else:
            sWord = difflib.get_close_matches(word,data,1)
            inp = input(f'Did you mean: "{sWord[0]}" ?\n')
            if inp.lower() in ['y','yes','yeah','ye']:
                print(wordMeaning(sWord[0]))
            else:
                print("Word not in dictionary, please try again\n")

    else:
        for i in range(1,11): print("*" * i)
        print("Bye..........!")
        exit()
