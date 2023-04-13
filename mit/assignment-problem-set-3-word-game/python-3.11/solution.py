# def rand_char() -> str:
#     alpha = string.ascii_lowercase
#     return alpha[random.randint(0, len(alpha) - 1)]

# def gen_hand(size: int) -> list[str]:
#     return [rand_char() for _ in range(0, size)]

# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string
import os
from functools import reduce
import re

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10, '*': 0
}

# Allows test the random functions with the values provided in the book.
def _mock(*mock):
    calls = 0
    def decorator(fn):
        def wrapper(*args, **kwargs):
            nonlocal calls
            r = mock[calls]
            calls += 1
            return r
        return wrapper
    return decorator

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "words.txt")

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")

    with open(WORDLIST_FILENAME, 'r') as file:
        # wordlist: list of strings
        wordlist = []
        for line in file:
            wordlist.append(line.strip().lower())
        print("  ", len(wordlist), "words loaded.")
        return wordlist

def get_frequency_dict(sequence: str) -> dict[str, int]:
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq: dict[str, int] = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word: str, n: int) -> int:
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower()
    points = reduce(lambda a, c: a + c, map(lambda c: SCRABBLE_LETTER_VALUES[c], word), 0)
    return points * max(1, 7 * len(word) - 3 * (n - len(word)))

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand: dict[str, int]):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
# @_mock(get_frequency_dict('aci*prt'), get_frequency_dict('dd*lout'))
def deal_hand(n: int) -> dict[str, int]:
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {'*': 1}
    num_vowels = int(math.ceil(n / 3))
    num_consonant = n - num_vowels

    for i in range(num_vowels - 1):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for i in range(num_consonant):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand: dict[str, int], word: str) -> dict[str, int]:
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    word = word.lower()
    hand = hand.copy()

    for c in word:
        if c not in hand.keys(): continue

        hand[c] = hand[c] - 1

        if hand[c] <= 0: del hand[c]

    return hand

def _is_vowel(char: str):
    return char in VOWELS

def _has_word_match(word: str, another: str) -> bool:
    if len(word) != len(another): return False
    if len(word) == 0 or len(another) == 0: return True
    return (word[0] == another[0] or (word[0] == '*' and _is_vowel(another[0]))) and _has_word_match(word[1:], another[1:])

def _has_any_word_match(word: str, word_list: list[str]) -> bool:
    return _first_word_match(word, word_list) is not None

def _first_word_match(word: str, word_list: list[str]) -> str | None:
    matches = _word_matches(word, word_list, count=1)
    if len(matches) == 0: return None
    return matches[0]

def _word_matches(word: str, word_list: list[str], count: int | None = 0) -> list[str]:
    return list(filter(lambda another: _has_word_match(word, another), word_list))[0:count]

#
# Problem #3: Test word validity
#
def is_valid_word(word: str, hand: dict[str, int], word_list: list[str]):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """

    only_alpha_or_wildcard_char = re.compile(r'^([a-z]|[A-Z]|\*)*$')

    if re.search(only_alpha_or_wildcard_char, word) is None:
        return False

    word = word.lower()

    if not _has_any_word_match(word, word_list):
        return False

    for c in word:
        if c not in hand.keys():
            return False
        hand = update_hand(hand, c)

    return True

#
# Problem #5: Playing a hand
#
def calculate_handlen(hand: dict[str, int]) -> int:
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return reduce(lambda t, e: t + e, hand.values(), 0)

class HandMatch:
    def __init__(self, hand: dict[str, int], word_list: list[str], score: int = 0, stopped: bool = False) -> None:
        self.hand = hand
        self.word_list = word_list
        self.score = score
        self.stopped = stopped

    def copy(self):
        return HandMatch(hand=self.hand.copy(), word_list=self.word_list.copy(), score=self.score, stopped=self.stopped)

    def is_game_over(self) -> bool:
        return not self.has_letters() or self.stopped

    def has_letters(self) -> bool:
        return self.calculate_handlen() > 0

    def calculate_handlen(self) -> int:
        return calculate_handlen(self.hand)

    def enter_word(self, word: str) -> int:
        if word == '!!':
            self.stopped = True
            return 0

        if is_valid_word(word=word, hand=self.hand, word_list=self.word_list):
            earned = get_word_score(word=word, n=calculate_handlen(self.hand))
            self.score += earned
            self.hand = update_hand(self.hand, word)
            return earned
        else:
            self.hand = update_hand(self.hand, word)
            return -1

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    game = HandMatch(hand=hand, word_list=word_list)

    while not game.is_game_over():
        print(f'Current Hand: ', end='')

        display_hand(game.hand)

        word = input('Enter word, or "!!" to indicate that you are finished: ')

        earned = game.enter_word(word)

        if earned == -1:
            print('That is not a valid word. Please choose another word.')
        else:
            print(f'"{word}" earned {earned} points. Total: {game.score} points ')

        if game.is_game_over():
            print('\nRan out of letters. ', end='')

    print(f'Total score: {game.score} points')

    return game.score


#
# Problem #6: Playing a game
# 

#
# procedure you will use to substitute a letter in a hand
#
# @_mock(get_frequency_dict('dd*aout'))
def substitute_hand(hand: dict[str, int], letter: str) -> dict[str, int]:
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """

    copy = hand.copy()

    if letter not in hand.keys(): return copy

    available = (VOWELS + CONSONANTS).replace(letter, '')

    replacer = random.choice(available)

    copy[replacer] = copy[letter]
    del copy[letter]

    return copy

def _display_border():
    print('-' * 30)

def play_game(word_list: list[str]):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """

    total_score = 0
    hands_number = None
    while hands_number is None:
        try:
            hands_number = int(input('Enter total number of hands: '))
        except:
            print('Invalid input, enter a the number of hands you wanna play.')

    for i in range(hands_number):
        hand = deal_hand(HAND_SIZE)
        print('Current hand: ', end='')
        display_hand(hand)

        substitute = input('Would you like to substitute a letter? ')

        if substitute.startswith('y'):
            letter = input('Which letter would you like to replace: ')
            hand = substitute_hand(hand=hand, letter=letter)

        score = play_hand(hand=hand, word_list=word_list)
        _display_border()

        if input('Would you like to replay the hand? ').startswith('y'):
            score = play_hand(hand=hand, word_list=word_list)

        total_score += score

    _display_border()

    print(f'Total score over all hands: {total_score}')

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
