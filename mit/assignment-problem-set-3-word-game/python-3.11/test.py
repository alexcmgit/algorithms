import os
import unittest
import string
import solution as s1

ROOT = os.path.dirname(os.path.realpath(__file__))

def make_test(solution) -> type[unittest.TestCase]:
    class BaseSolutionTest(unittest.TestCase):
        def setUp(self) -> None:
            pass

        def test_get_word_score(self):
            '''
            Unit test for get_word_score
            '''
            # dictionary of words and scores
            words: dict[tuple[str, int], int] = {('', 7):0, ('it', 7):2, ('was', 7):54, ('weed', 6):176,
                    ('scored', 7):351, ('WaYbILl', 7):735, ('Outgnaw', 7):539,
                    ('fork', 7):209, ('FORK', 4):308}
            for word, n in words.keys():
                score = solution.get_word_score(word, n)
                self.assertEqual(score, words[(word, n)], msg=f"Expected {words[(word, n)]} points but got '{score}' for word '{word}', n={n}")

        def _test_update_hand(self, id, handorig: dict[str, int], word: str, expected_hand1: dict[str, int], expected_hand2: dict[str, int], update_hand):
            '''
            Unit test for update_hand
            '''
            # test 1
            handcopy = handorig.copy()

            hand2 = update_hand(handcopy, word)

            msg_if_error = f'[ID: {id}] Returned: {hand2}\nbut expected: {expected_hand1} or {expected_hand2}'

            if hand2 != expected_hand1 and hand2 != expected_hand2:
                self.fail(msg_if_error)

            msg_if_error = f'''
                Failure: test_update_hand('{word}', '{handorig}')
                Original hand was {handorig}. But implementation of [update_hand] mutated the original hand! Now the hand looks like this: {handcopy}
            '''

            self.assertDictEqual(handcopy, handorig, msg=msg_if_error)

        def test_update_hand(self):
            '''
            Unit test for update_hand
            '''
            self._test_update_hand(1, handorig={'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}, word='quail', expected_hand1={'l':1, 'm':1}, expected_hand2={'a':0, 'q':0, 'l':1, 'm':1, 'u':0, 'i':0}, update_hand=solution.update_hand)

            self._test_update_hand(2, handorig={'e':1, 'v':2, 'n':1, 'i':1, 'l':2}, word='Evil', expected_hand1={'v':1, 'n':1, 'l':1}, expected_hand2={'e':0, 'v':1, 'n':1, 'i':0, 'l':1}, update_hand=solution.update_hand)

            self._test_update_hand(3, handorig={'h': 1, 'e': 1, 'l': 2, 'o': 1}, word='HELLO', expected_hand1={}, expected_hand2={'h': 0, 'e': 0, 'l': 0, 'o': 0}, update_hand=solution.update_hand)

        def test_frequency_dict(self):
            self.assertDictEqual(solution.get_frequency_dict('asdf'), {'a': 1, 's': 1, 'd': 1, 'f': 1})
            self.assertDictEqual(solution.get_frequency_dict('myword'), {'m': 1, 'y': 1, 'w': 1, 'o': 1, 'r': 1, 'd': 1})
            self.assertDictEqual(solution.get_frequency_dict('repeated'), {'r': 1, 'e': 3, 'p': 1, 'a': 1, 't': 1, 'd': 1})
            self.assertDictEqual(solution.get_frequency_dict('again'), {'a': 2, 'g': 1, 'i': 1, 'n': 1})
            self.assertDictEqual(solution.get_frequency_dict('a' * 5 + 'b' * 10 + 'c' * 20), {'a': 5, 'b': 10, 'c': 20})
            self.assertDictEqual(solution.get_frequency_dict(string.ascii_lowercase), {c: 1 for c in string.ascii_lowercase})

        def _test_is_valid_word(self, word_list: list[str], word: str, hand: dict[str, int], is_valid_word, expect: bool):
            handorig = hand
            handcopy = handorig.copy()

            expected_error_msg = f'Expected [{expect}], but got [{not expect}] for word: {word} and hand: {handorig}'

            msg_if_error = f'''
                FAILURE: test_is_valid_word()
                {expected_error_msg}
            '''

            self.assertTrue(is_valid_word(word, handcopy, word_list) == expect, msg=msg_if_error)

            msg_if_error = f'''
                FAILURE: test_is_valid_word()
                {expected_error_msg}
            '''

            if handcopy != handorig:
                msg_if_error += f'''
                    Testing word {word} for a second time - be sure you're not modifying hand.
                    At this point, hand ought to be {handorig}, but it is {handcopy}
                '''
            else:
                word_in_wl = word in word_list
                msg_if_error += f'''
                    Testing word {word}, for a second time - have you modified word_list?
                    The word {word} should be in {word_list} - is it? {word_in_wl}.
                '''

            msg_if_error += expected_error_msg

            # Test a second time to see if word_list or hand has been modified
            self.assertTrue(is_valid_word(word, handcopy, word_list) == expect, msg=msg_if_error)

        def test_is_valid_word(self):
            '''
            Unit test for is_valid_word
            '''

            word_list = solution.load_words()

            # test 1
            word = 'hello'
            hand = solution.get_frequency_dict(word)
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=True)

            # test 2
            hand = {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u':1}
            word = 'Rapture'
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=False)

            # test 3
            hand = {'n': 1, 'h': 1, 'o': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
            word = 'honey'
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=True)

            # test 4
            hand = {'r': 1, 'a': 3, 'p': 2, 't': 1, 'u':2}
            word = 'honey'
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=False)

            # test 5
            hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
            word = 'EVIL'
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=True)

            # test 6
            word = 'Even'
            hand = {'e':1, 'v':2, 'n':1, 'i':1, 'l':2}
            self._test_is_valid_word(word_list=word_list, word=word, hand=hand, is_valid_word=solution.is_valid_word, expect=False)

        def _test_wildcard(self, hand: dict[str, int], word: str, word_list: list[str], is_valid_word, expected: bool):
            msg_if_error = f'''
                FAILURE: test_is_valid_word() with wildcards
                Expected [{expected}], but got f{not expected} for word: '{word}' and hand: {hand}
            '''
            self.assertTrue(is_valid_word(word, hand, word_list) == expected, msg=msg_if_error)

        def _test_wildcard_score(self, word: str, n: int, get_word_score, expected: int):
            score = get_word_score(word, n)
            msg_if_error = f'''
                FAILURE: test_get_word_score() with wildcards
                Expected {expected} points but got '{score}' for word '{word}', n={n}
            '''
            self.assertEqual(score, expected, msg=msg_if_error)

        def test_wildcard(self):
            '''
            Unit test for is_valid_word
            '''

            word_list = solution.load_words()

            # test 1
            hand = {'a': 1, 'r': 1, 'e': 1, 'j': 2, 'm': 1, '*': 1}
            word = "e*m"
            self._test_wildcard(hand=hand, word=word, word_list=word_list, is_valid_word=solution.is_valid_word, expected=False)

            # test 2
            hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
            word = "honey"
            self._test_wildcard(hand=hand, word=word, word_list=word_list, is_valid_word=solution.is_valid_word, expected=False)

            # test 3
            hand = {'n': 1, 'h': 1, '*': 1, 'y': 1, 'd':1, 'w':1, 'e': 2}
            word = "h*ney"
            self._test_wildcard(hand=hand, word=word, word_list=word_list, is_valid_word=solution.is_valid_word, expected=True)

            # test 4
            hand = {'c': 1, 'o': 1, '*': 1, 'w': 1, 's':1, 'z':1, 'y': 2}
            word = "c*wz"
            self._test_wildcard(hand=hand, word=word, word_list=word_list, is_valid_word=solution.is_valid_word, expected=False)

            # dictionary of words and scores WITH wildcards
            words: dict[tuple[str, int], int] = {("h*ney", 7): 290, ("c*ws", 6): 176, ("wa*ls", 7): 203}

            for (word, n) in words.keys():
                self._test_wildcard_score(expected=words[(word, n)], word=word, n=n, get_word_score=solution.get_word_score)

        def test_calculate_handlen(self):
            hand = solution.get_frequency_dict('dd*aout')
            self.assertEqual(solution.calculate_handlen(hand), 7)

            hand = solution.get_frequency_dict('a' * 3 + 'b' * 5 + 'c' * 10)
            self.assertEqual(solution.calculate_handlen(hand), 18)

        def test_deal_hand(self):
            HAND_SIZE = 20
            HAND_COUNT = 100

            def is_same_hand(hand: dict[str, int], other: dict[str, int]) -> bool:
                if len(hand) != len(other): return False
                for key in hand.keys():
                    if key not in other.keys():
                        return False
                    if hand[key] != other[key]:
                        return False
                return True

            hands = [solution.deal_hand(HAND_SIZE) for i in range(0, HAND_COUNT)]
            conflicts = 0

            for i, hand in enumerate(hands):
                for j, other in enumerate(hands):
                    if i == j: continue
                    if is_same_hand(hand, other):
                        conflicts += 1

            if conflicts >= HAND_COUNT / 2:
                self.fail('FAILED [deal_hand]: More than 50% of the generated hands were equal.')

        def test_game_hand_match(self):
            word_list = solution.load_words()
            hand = {'b': 1, 'e': 2}
            n = solution.calculate_handlen(hand)
            game = solution.HandMatch(hand=hand, word_list=word_list)
            self.assertFalse(game.is_game_over())
            self.assertTrue(game.has_letters())
            self.assertEqual(game.score, 0)
            word = list(filter(lambda e: e == 'bee', word_list))[0]
            game.enter_word(word)
            self.assertTrue(game.is_game_over())
            self.assertEqual(game.score, solution.get_word_score(word, n))
            self.assertFalse(game.has_letters(), solution.get_word_score(word, n))

    return BaseSolutionTest

class TestSolution1(make_test(s1)):
    pass

if __name__ == '__main__':
    unittest.main()
