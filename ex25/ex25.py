def break_words(stuff):
    """This functio will break or make space between words"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    'sorts the words'
    return sorted(words)

def print_first_word(words):
    'Prints the first word after popping off.'
    words = words.pop(0)
    print(words)

def print_last_word(words):
    ' print the last word after popping on'
    words = words.pop(-1)
    print(words)

def sort_sentence(sentence):
    'Takes a full sentence and returns the sorted words'
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    'Print s ths first and and the last words'
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    'sorts the words anf prints the first'
    #print_first_word(words)
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
