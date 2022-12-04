
## Lab 5: Required Questions - Dictionaries  ##

# PLEASE NOTE: THE SHAKESPEARE TWEET GENERATOR NEEDS INTERNET TO RUN, WILL THROW ERROR OTHERWISEs

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    newDict = {}

    newDict = {**dict1, **dict2}
    
    return newDict


# RQ2
def counter(message):
    """ Returns a dictionary where the keys are the words in the message, and each
    key is mapped (has associated value) equal 
    to the number of times the word appears in the message.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    
    words = message.split()
    wordCount = {}
    
    for word in words:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1
    
    return wordCount

# RQ3
def replace_all(d, x, y):
    """ Returns a dictionary where the key/value pairs are the same as d, 
    except when a value is equal to x, then it should be replaced by y.
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    
    for key in d:
            if d[key] == x:
                d[key] = y
    

# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys/value pairs found in list. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value mapped for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    for i in range(len(lst)):
        if i == 0:
            newDict = lst[i]
        else:
            for key in lst[i]:
                if key in newDict:
                    newDict[key] += lst[i][key]
                else:
                    newDict[key] = lst[i][key]
           
    
    #print(newDict)
    return newDict
    
   
# tweet stuff // RQ5
def build_successors_table(tokens):
    """Takes in a list of words or tokens. Return a dictionary: keys are words; values are lists of successor words. By default, we set the first word in tokens to be a successor to "."

    >>> text = ['We', 'came', 'to', 'investigate', ',', 'catch', 'bad', 'guys', 'and', 'to', 'eat', 'pie', '.']
    >>> table = build_successors_table(text)
    >>> sorted(table)
    [',', '.', 'We', 'and', 'bad', 'came', 'catch', 'eat', 'guys', 'investigate', 'pie', 'to']
    >>> table['to']
    ['investigate', 'eat']
    >>> table['pie']
    ['.']
    >>> table['.']
    ['We']
    """
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table

def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    """Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()

def random_tweet(table):
    import random
    return construct_tweet(random.choice(table['.']), table)

def construct_tweet(word, table):
    """Returns a string that is a random sentence starting with word, and choosing successors from table.
    """
    import random
    result = ' '
    while word not in ['.', '!', '?']:
        result += word + ' '
        word = random.choice(table[word])
    return result + word



#RQ5
def middle_tweet(table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string which has length in middle value of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    
    import statistics
    
    tweets = []
    lengths = [];
    for i in range(5):
        tweets.append(random_tweet(table))
        lengths.append(len(tweets[i]))
    
    midlength = statistics.median(lengths)
    
    for i in range(5):
        if len(tweets[i]) == midlength:
            return tweets[i]
    
shakestokens = shakespeare_tokens()
shakestable = build_successors_table(shakestokens)

middle_tweet(shakestable)

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)


