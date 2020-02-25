#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    from collections import deque
    from copy import deepcopy


    dic = open(dictionary_file)
    dictionary = dic.read().split("\n")

    s = []                                          #create an empty stack
    s.append(start_word)                            #add the start_word to the stack

    q = deque()                                     #create a queue
    q.append(s)                                     #push the stack onto the queue

    if start_word == end_word:                      #if start_word is the end_word
        return s                                    #return the stack

    while len(q) > 0:                                       #if the there still are stack on the queue
        topstack = q.pop()                                  #take the right stack as topstack

        newdic=deepcopy(dictionary)

        for word in newdic:                             #for each word in the dictionary
            if _adjacent(word,topstack[-1]) is True:       #if it is the adjacent word with the first term from the right side of the stak
                copystack = deepcopy(topstack)              #make a copy of the stack
                copystack.append(word)                      #add that word to the copied stack

                if word == end_word:                        #if this word is the end_word
                    return copystack                        #return the rest of the stack

                q.appendleft(copystack)                     #add this stack to the left of the queue
                dictionary.remove(word)                     #remove the word from dictionary
    return None




def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.
    '''

    if len(ladder) == 0:
        return False
    for i in range(len(ladder)-1):
        if not _adjacent(ladder[i],ladder[i+1]):
            return False
    return True



def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) != len(word2):
        return False
    x=0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            x = x + 1
    if x==1:
        return True
    else:
        return False







