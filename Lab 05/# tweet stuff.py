# tweet stuff
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