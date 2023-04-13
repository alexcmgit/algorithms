import os
from functools import reduce

ROOT = os.path.dirname(os.path.realpath(__file__))

### HELPER CODE ###
def load_words(filename: str = 'words.txt'):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    with open(os.path.realpath(os.path.join(ROOT, '..', filename)), 'r') as f:
        wordlist: list[str] = []

        for line in f:
            wordlist.extend([word.lower() for word in line.split(' ')])
        return wordlist

def is_word(word_list: list[str], word: str):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    with open("story.txt", "r") as f:
        story = str(f.read())
        return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text: str):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.valid_words = load_words()
        self.message_text = text
    
    def get_message_text(self) -> str:
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self) -> list[str]:
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_transpose_dict(self, vowels_permutation: str):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)

        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''

        return {**{v: vowels_permutation[i].lower() for i, v in enumerate(VOWELS_LOWER)}, **{v: vowels_permutation[i].upper() for i, v in enumerate(VOWELS_UPPER)}}

    def apply_transpose(self, transpose_dict: dict[str, str]) -> str:
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        return ''.join([transpose_dict[char] if char in transpose_dict else char for char in self.get_message_text()])

class EncryptedSubMessage(SubMessage):
    def __init__(self, text: str):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)


    def _get_permutations(self, sequence: str = 'aeiou') -> list[str]:
        if len(sequence) <= 1: return [sequence]

        subsequences = self._get_permutations(sequence[1:])
        fixed = sequence[0]
        sequences: list[str] = []

        for subseq in subsequences:
            for i in range(0, len(subseq) + 1):
                sequences.append(subseq[0:i] + fixed + subseq[i:])

        return sequences

    def _decrypt(self, permutation: str) -> str:
        transpose = self.build_transpose_dict(permutation)
        rtranspose = {transpose[k]: k for k in transpose.keys()}
        message = self.apply_transpose(rtranspose)
        return message

    def _get_alpha_from_message(self, message: str) -> str:
        '''
        If [shift] = "Hello, Word"
        Returns "hello world"
        '''
        return ''.join([c if c == ' ' or c.isalpha() else '' for c in message]).lower()

    def _valid_words_count(self, message: str) -> int:
        '''
        If [message] = "hello word kopsd"
        Returns 2
        '''
        return reduce(lambda acc, e: acc + e, map(lambda word: 1 if word in self.valid_words else 0, message.split(' ')), 0)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    

        Hint: use your function from Part 4A
        '''
        permutations = self._get_permutations()
        words = 0
        message = None

        for permutation in permutations:
            output = self._decrypt(permutation)
            plain = self._get_alpha_from_message(output)
            count = self._valid_words_count(plain)
            if count > words:
                words = count
                message = output

        return message or self.get_message_text()
