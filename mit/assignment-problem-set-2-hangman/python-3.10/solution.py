import os, random
from threading import Timer, Thread
import types
from inspect import getsourcefile
from os.path import abspath
import abc

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def colored(r: int, g: int, b: int, text: str) -> str:
    return f'\033[38;2;{r};{g};{b}m{text}\033[0m'

def red(text: str) -> str:
    return colored(238, 82, 83, text)

def green(text: str) -> str:
    return colored(16, 172, 132, text)

def orange(text: str) -> str:
    return colored(255, 159, 67, text)

def blue(text: str) -> str:
    return colored(46, 134, 222, text)

def get_words() -> list[str]:
    with open(os.path.realpath(os.path.join(os.path.dirname(abspath(getsourcefile(lambda: 0) or '')), '..', 'words.txt'))) as f:
        return f.readline().split(' ')

def get_random_word() -> str:
    words = get_words()
    return words[random.randint(0, len(words) - 1)]

def is_word_guessed(secret: str, guessed: list[str] | set[str]) -> bool:
    guessed = guessed if isinstance(guessed, set) else set(guessed)
    if len(secret) == 0: return True
    return secret[0] in guessed and is_word_guessed(secret=secret[1:], guessed=guessed)

def get_masked_word(secret: str, guessed: list[str] | set[str]) -> list[str | None]:
    guessed = guessed if isinstance(guessed, set) else set(guessed)
    if len(secret) == 0: return []
    return [(secret[0] if secret[0] in guessed else None)] + get_masked_word(secret=secret[1:], guessed=guessed)

def get_available_letters(guessed: list[str] | set[str]) -> list[str]:
    return list(filter(lambda c: c not in guessed, [chr(c) for c in range(97, 122 + 1)]))

def has_partial_match(word: str, masked_secret: list[str | None], excluded: list[str] = []) -> bool:
    if len(word) != len(masked_secret): return False
    if len(word) <= 0 or len(masked_secret) <= 0: return False

    for i in range(0, len(word)):
        if word[i] in excluded:
            return False
        if word[i] in masked_secret:
            if masked_secret[i] is None:
                return False
        if word[i] != masked_secret[i]:
            if masked_secret[i] is not None:
                return False

    return True

def generate_hints(masked_secret: list[str | None], excluded: list[str] = [], words: list[str] | None = None) -> list[str]:
    return list(filter(lambda word: has_partial_match(word, masked_secret, excluded), words or get_words()))

def get_missed_guesses(secret: str, guessed: list[str]) -> list[str]:
    return list(filter(lambda guess: guess not in secret, guessed))

class Hangman:
    _timer = None
    _temp_msg = None

    def __init__(self, secret: str, words: list[str], warnings: int = 3, chances: int = 6, guessed: list[str] = []) -> None:
        assert secret in words, '''The secret word must be within the word data set. Otherwise we will not be able to generate helpful hints.'''
        self.warnings = warnings
        self.chances = chances
        self.flags = 0
        self.misses = 0
        self.secret = secret
        # Do not copy the list ref otherwise the caller may alter the list from outside of [this] instance.
        self._guessed = list(guessed)

    @property
    def guessed(self):
        return self._guessed

    @property
    def warnings_left(self) -> int:
        return max(self.warnings - self.flags, 0)

    @property
    def chances_left(self) -> int:
        return max(self.chances - self.misses, 0)

    def is_word_guessed(self):
        return is_word_guessed(secret=self.secret, guessed=self.guessed)

    def won(self) -> bool:
        return self.is_word_guessed()

    def there_are_no_more_guesses_left(self):
        return self.chances_left <= 0

    def is_game_over(self) -> bool:
        return self.won() or self.there_are_no_more_guesses_left()

    def is_valid_guess(self, guess: str) -> bool:
        return self._get_char_error(guess) is None

    def generate_hints(self) -> list[str]:
        '''
        Compute available hints from the state of the current instance.
        '''
        return generate_hints(self.get_masked_word(), self.get_missed_guesses())

    def get_masked_word(self) -> list[str | None]:
        return get_masked_word(self.secret, self.guessed)

    def available_letters(self) -> list[str]:
        '''
        Return the current available letters (not guessed yet).
        '''
        return get_available_letters(self.guessed)

    def get_score(self):
        return self.chances_left * len(set(self.secret))

    def get_missed_guesses(self) -> list[str]:
        '''
        Return the letters already guessed (correct or not).
        For only correct guessed letters use []
        '''
        return get_missed_guesses(self.secret, self.guessed)

    def guess(self, char: str) -> None:
        '''
        Push a new guess to the current game state.
        '''

        char = char.lower()

        valid_guess = self.is_valid_guess(char)

        if not valid_guess:
            if self.warnings_left <= 0:
                if char not in self.secret:
                    self.misses += 1
            else:
                self.flags += 1
        else:
            self.guessed.append(char)
            nice_guess = char in self.secret

            if not nice_guess:
                self.misses += 2 if char in 'aeiou' else 1

    def drive(self) -> None:
        '''
        Starts the interactive CLI.
        '''
        self._print_interactive_cli()
        self._input_interactive_cli()

    def _get_char_error(self, guess: str):
        if len(guess) != 1:
            return orange('Please, type a single letter.')
        if not guess.isalpha():
            return orange('Please, type a letter within [a] and [z].')
        if guess in self.guessed:
            if guess in self.secret:
                return orange('This letter has already been guessed!')
            return orange('This letter has already used!')
        return None

    def _print_interactive_cli(self) -> None:
        guessed = self.guessed
        secret = self.secret
        left = self.chances_left
        wleft = self.warnings_left

        cls()

        print('Welcome to the game Hangman!')
        print(f'I\'m thinking of a word that is {len(secret)} letters long.')
        print(blue(' '.join(map(lambda e: '_' if e is None else e, get_masked_word(secret=secret, guessed=guessed)))))
        print(f'You have {red(f"{left}") if left <= 1 else orange(f"{left}") if left <= 3 else blue(f"{left}")} guess(es) left.')
        print(f'You have {red(f"{wleft}") if wleft == 0 else orange(f"{wleft}") if wleft == 1 else blue(f"{wleft}")} warning(s) left.')
        print(f'Available letters: {", ".join(get_available_letters(guessed))}.')
        print(f'Letters already used: {", ".join(guessed) if len(guessed) > 0 else "None yet.."}.')
        print('Type your next guess (a-z letter or \'*\' for hints):')

        if self.is_game_over():
            if self.won():
                print(green(f'\nCongrats! You score is {self.get_score()}'))
            else:
                print(red(f'\nSecret word was: {secret}'))
        else:
            if self._temp_msg is not None:
                print(self._temp_msg)

    def _set_temp_msg(self, msg: str, sec: int = 5):
        if self._timer is not None:
            self._timer.cancel()
        self._temp_msg = msg

        self._timer = Timer(sec, self._clear_temp_msg)
        self._timer.start()

        if self.is_game_over():
            self._timer.cancel()

    def _print_hints(self) -> None:
        possible_guess_header = '\n - '

        hints = blue(f"{possible_guess_header}{possible_guess_header.join(self.generate_hints()[:20])}")

        self._set_temp_msg(f'\nYou said... HINTS?!{hints}', 20)

    def _input_interactive_cli(self):
        while not self.is_game_over():
            char = input().lower()

            if char == '*':
                self._print_hints()
            else:
                error = self._get_char_error(char)

                self.guess(char)

                if error is not None:
                    self._set_temp_msg(error)
                else:
                    nice_guess = char in self.secret
                    self._set_temp_msg(green('Good guess!') if nice_guess else red('Bad guess...'))

            self._schedule_reprint()

    def _schedule_reprint(self, fn: types.FunctionType | None = None):
        if fn is not None: fn()
        self._print_interactive_cli()

    def _clear_temp_msg(self) -> None:
        self._temp_msg = None
        self._schedule_reprint()

def hangman(secret: str, chances: int = 6, warnings: int = 3) -> None:
    hangman = Hangman(secret=secret, chances=chances, warnings=warnings, words=get_words())
    hangman.drive()

if __name__ == '__main__':
    hangman(get_random_word())
