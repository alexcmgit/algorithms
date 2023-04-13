import os
import unittest
import solution as s1

ROOT = os.path.dirname(os.path.realpath(__file__))

class TestSolution1(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_is_word_guessed(self):
        self.assertFalse(s1.is_word_guessed(secret='abcd', guessed=['a', 'b', 'c']))
        self.assertFalse(s1.is_word_guessed(secret='abcd', guessed=list(reversed(['a', 'b', 'c']))))

        self.assertTrue(s1.is_word_guessed(secret='abcd', guessed=['a', 'b', 'c', 'd']))
        self.assertTrue(s1.is_word_guessed(secret='abcd', guessed=list(reversed(['a', 'b', 'c', 'd']))))

    def test_get_masked_word(self):
        masked = s1.get_masked_word(secret='abcd', guessed=['a', 'b', 'c'])

        self.assertEqual(len(masked), len('abcd'))
        
        self.assertEqual(masked[0], 'a')
        self.assertEqual(masked[1], 'b')
        self.assertEqual(masked[2], 'c')
        self.assertEqual(masked[3], None)

    def test_get_available_letters(self):
        available_letters = s1.get_available_letters(guessed=['a', 'b', 'c'])
        self.assertTrue('a' not in available_letters)
        self.assertTrue('b' not in available_letters)
        self.assertTrue('c' not in available_letters)
        self.assertTrue(len(available_letters) - len('abc'))

    def test_get_random_word(self):
        # [words.txt] has 55900 words, the individual probability is 1 / 55900 -> 0.00001788908 -> 0.001788908%.
        # The probability of computing 10 equal random words is [0.001788908%^10] -> 3.3564491e-48 or 0.00000000000000000000000000000000000000000000033564491% so if you are able to fail this test, you are either:
        # - messing up with the implementation.
        # - the most lucky/unlucky guy you'll ever met, consider it a one-time life event.
        random_words = set([s1.get_random_word() for i in range(0, 10)])
        self.assertFalse(len(random_words) == 1)
        if len(random_words) < 10:
            print(f'Warning: [get_random_word] function produced duplicated outputs in 10 calls, which is unlikely to happen though not improbable. Words: {random_words}')

    def test_example1(self):
        hangman = s1.Hangman(secret='tact', words=s1.get_words())

        hangman.guess('a')
        hangman.guess('s')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('t')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('c')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertTrue(hangman.is_game_over())
        self.assertTrue(hangman.won())
        self.assertEqual(hangman.get_score(), 9)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', 'c', 't'])

    def test_example2(self):
        hangman = s1.Hangman(secret='dolphin', words=s1.get_words())

        hangman.guess('b')
        hangman.guess('c')
        hangman.guess('f')

        hangman.guess('d')
        hangman.guess('o')
        hangman.guess('l')
        hangman.guess('p')
        hangman.guess('h')
        hangman.guess('i')
        hangman.guess('n')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertTrue(hangman.is_game_over())
        self.assertTrue(hangman.won())
        self.assertEqual(hangman.get_score(), 21)
        self.assertEqual(hangman.get_masked_word(), ['d', 'o', 'l', 'p', 'h', 'i', 'n'])

    def test_winning_game(self):
        hangman = s1.Hangman(secret='tact', words=s1.get_words())

        hangman.guess('a')

        self.assertEqual(hangman.chances_left, 6)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('a')

        self.assertEqual(hangman.chances_left, 6)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('s')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertEqual(hangman.get_masked_word(), [None, 'a', None, None])

        hangman.guess('t')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 2)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', None, 't'])

        hangman.guess('c')

        self.assertEqual(hangman.chances_left, 2)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertTrue(hangman.is_game_over())
        self.assertTrue(hangman.won())
        self.assertEqual(hangman.get_score(), 6)
        self.assertEqual(hangman.get_masked_word(), ['t', 'a', 'c', 't'])

    def test_losing_game(self):
        hangman = s1.Hangman(secret='else', words=s1.get_words())

        hangman.guess('a')

        self.assertEqual(hangman.chances_left, 4)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), [None, None, None, None])

        hangman.guess('b')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), [None, None, None, None])

        hangman.guess('c')

        self.assertEqual(hangman.chances_left, 2)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), [None, None, None, None])

        hangman.guess('d')

        self.assertEqual(hangman.chances_left, 1)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), [None, None, None, None])

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 1)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertEqual(hangman.get_masked_word(), ['e', None, None, 'e'])

        hangman.guess('f')

        self.assertEqual(hangman.chances_left, 0)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertTrue(hangman.is_game_over())
        self.assertFalse(hangman.won())
        self.assertEqual(hangman.get_masked_word(), ['e', None, None, 'e'])

    def test_has_partial_match(self):
        self.assertFalse(s1.has_partial_match(masked_secret=['t', 'e', None, 't'], word='tact'))
        self.assertFalse(s1.has_partial_match(masked_secret=['a', None, None, 'l', 'e'], word='banana'))
        self.assertTrue(s1.has_partial_match(masked_secret=['a', None, None, 'l', 'e'], word='apple'))
        self.assertFalse(s1.has_partial_match(masked_secret=['a', None, 'p', 'l', 'e'], word='apple'))

    def test_generate_hints(self):
        self.assertEqual(s1.generate_hints(masked_secret=['t', None, None, 't'], words=s1.get_words()), 'tact tart taut teat tent test text that tilt tint toot tort tout trot tuft twit'.split(' '))
        self.assertEqual(s1.generate_hints(masked_secret=['a', 'b', 'b', 'b', 'b', None], words=s1.get_words()), [])
        self.assertEqual(s1.generate_hints(masked_secret=['a', None, 'p', 'l', None], words=s1.get_words()), 'ample amply'.split(' '))

    def test_generate_hints_within_the_game(self):
        hangman = s1.Hangman(secret='apple', words=s1.get_words())

        hangman.guess('a')
        hangman.guess('l')

        self.assertEqual(hangman.generate_hints(), 'addle adult agile aisle amble ample amply amyls angle ankle apple apply aptly arils atilt'.split(' '))

    def test_basic_flow(self):
        hangman = s1.Hangman(secret='abc', words=['abc', 'acd', 'adc', 'aab', 'bba'])

        self.assertEqual(hangman.chances_left, 6)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 26)
        self.assertEqual(len(hangman.get_missed_guesses()), 0)

        hangman.guess('d')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 25)
        self.assertEqual(len(hangman.get_missed_guesses()), 1)

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 24)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 24)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('a')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('$')
        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 2)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('u')

        self.assertEqual(hangman.chances_left, 0)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertTrue(hangman.is_game_over())
        self.assertFalse(hangman.won())
        self.assertEqual(len(hangman.available_letters()), 22)
        self.assertEqual(len(hangman.get_missed_guesses()), 3)

    def test_basic_flow_with_capital_letters(self):
        hangman = s1.Hangman(secret='abc', words=['abc', 'acd', 'adc', 'aab', 'bba'])

        self.assertEqual(hangman.chances_left, 6)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 26)
        self.assertEqual(len(hangman.get_missed_guesses()), 0)

        hangman.guess('D')

        self.assertEqual(hangman.chances_left, 5)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 25)
        self.assertEqual(len(hangman.get_missed_guesses()), 1)

        hangman.guess('E')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 3)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 24)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('e')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 24)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('A')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 2)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 3)
        self.assertEqual(hangman.warnings_left, 1)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('$')
        hangman.guess('$')

        self.assertEqual(hangman.chances_left, 2)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertFalse(hangman.is_game_over())
        self.assertEqual(len(hangman.available_letters()), 23)
        self.assertEqual(len(hangman.get_missed_guesses()), 2)

        hangman.guess('U')

        self.assertEqual(hangman.chances_left, 0)
        self.assertEqual(hangman.warnings_left, 0)
        self.assertTrue(hangman.is_game_over())
        self.assertFalse(hangman.won())
        self.assertEqual(len(hangman.available_letters()), 22)
        self.assertEqual(len(hangman.get_missed_guesses()), 3)

if __name__ == '__main__':
    unittest.main()
