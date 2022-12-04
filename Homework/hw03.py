# Get Sentence Stuff
url = "http://raw.githubusercontent.com/eneko/data-repository/master/data/words.txt"
import os
from urllib.request import urlopen
wordfile = urlopen(url)
words = wordfile.read().decode('utf-8').upper().split()

# PROG STARTS HERE
# I attempted to speed up the following program, by using try and except statements, as well
# as the pass statement. I also used a global variable to store the list of words, and
# a dictionary to store the letters in the alphabet. The use of these structures is
# more efficient then processing each value individually, as these structures are well
# optimized for data manipulation and parsing. 

# Step Function
def step(word): # start step function
    
    # import globals
    global aList, aDict, findWords
    
    # create a list of letters in word
    word = word.upper()
    sortedWord = [*word]
    sortedWord.sort()
    print(sortedWord)
    
    output = []
    
    # loop through each letter in word and find anagrams for it
    for i in aList:
        new = ""
        value = 0
        
        # loop through each letter in word
        for j in range(0, len(word)):
            if value == 0 and (aDict[sortedWord[j]] > aDict[i]):
                new = new + i
                value = 1
            new = new + sortedWord[j]
        
        # if the letter is the last letter in the word
        if value == 0:
            new = new + i
        
        # if the word is in the dictionary
        try:
            output = output + findWords[new]
        except KeyError:
            pass
    
    # return the list of anagrams
    return output
        
# Main Function
def main():
    #word = str(input("Enter a Word: ")) # ask for a word to find anagrams for
    
    word = "apple"
    
    # import globals
    global aList, aDict, findWords
    
    # create a list of letters in all words listed in words
    for w in words:
        try:
            findWords["".join(sorted(w))].append(w)
        except KeyError:
            findWords["".join(sorted(w))] = [w]
    
    # create list of letters in alphabet
    for i in range(65,91):
        aDict[chr(i)]=i
        aList.append(chr(i))
    
    # print the list of anagrams
    result = step(word)
    print(result)

# PROG ENDS HERE

# Globals
aList = []
aDict = {}
findWords = {}


main() # run main function