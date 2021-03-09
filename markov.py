"""Generate Markov text from text files."""

from random import choice

# can change to import random to import anything out of random, not just choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    new_file = open(file_path)
    read_file = new_file.read()
    print(read_file)  
    new_file.close()                # need to add a closing statement for file: variable.close()
    return read_file                # return file so we can use it in later function



# thought process:

# str.rstrip() to remove a trailing newline (/n)
# OR print("Hello", end=" ")

# read_file = []
# read_file2 = read_file.append(text_file)
    
    # def open_and_read(file_path):
    #    text_file = open(file_path).read()             # opens file and reads it/makes it a string
    #    read_file = list(text_file)
    #    
    

def make_chains(text_string):


# taking our input text and turning it into tuples:

# for i in range(len(text) - 1):
# print(text[i], text[i + 1])

    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

# thought process:

# chains = {} to create a dictionary
# do we have to make a dictionary of tuples?
# so turn our text (multi-lined string) into tuples first?
# code turns text input into markov chains like bigrams

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # return bigrams as output

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
