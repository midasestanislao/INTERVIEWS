'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

"""Your task is to write a function that, given a list of words and a string, finds and returns the word in the list that is scrambled up inside the string, if any exists. There will be at most one matching word. The letters don't need to be in order or next to each other. The letters cannot be reused.

Example:
words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'

find_embedded_word(words, string1) -> cat (the letters do not have to be in order)

string2 = 'tbcanihjs'
find_embedded_word(words, string2) -> cat (the letters do not have to be together)

string3 = 'baykkjl'
find_embedded_word(words, string3) -> None (the letters cannot be reused)

string4 = 'bbabylkkj'
find_embedded_word(words, string4) -> baby

string5 = 'ccc'
find_embedded_word(words, string5) -> None

string6 = 'breadmaking'
find_embedded_word(words, string6) -> bird

Complexity analysis variables:

W = number of words in `words`
S = maximal length of each word or string"""

words = ['cat', 'baby', 'dog', 'bird', 'car', 'ax']
string1 = 'tcabnihjs'
string2 = 'tbcanihjs'
string3 = 'baykkjl'
string4 = 'bbabylkkj'
string5 = 'ccc'
string6 = 'breadmaking'

def chechar(string, words):

    cont_String = []
    
    for i in range(len(string)):
        cont_String.append(string[i])
    
    print(cont_String)
        
    for word in words:
        newString = cont_String.copy()
        collection = []
        for char in word:
            if char in newString:
                newString.remove(char)
                collection.append(char)
            else:
                break
        
        letter = "".join(collection)
        print(collection)
        if letter in words:
            return letter
        
    return "None"
        
print(chechar(string3, words))