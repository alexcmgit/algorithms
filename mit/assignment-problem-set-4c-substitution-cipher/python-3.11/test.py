import unittest
import solution as s1

def make_test(solution):
    class BaseSolutionTest(unittest.TestCase):
        def setUp(self) -> None:
            pass

        def test_encryption_and_decryption(self):
            # Case 1
            message = solution.SubMessage('Hello World!')
            permutation = 'eaiuo'
            enc_dict = message.build_transpose_dict(permutation)
            self.assertEqual(message.apply_transpose(enc_dict), 'Hallu Wurld!')
            enc_message = solution.EncryptedSubMessage(message.apply_transpose(enc_dict))
            self.assertEqual(enc_message.decrypt_message(), 'Hello World!')

            # Case 2
            message = solution.SubMessage('Hello World!')
            permutation = 'uoeai'
            enc_dict = message.build_transpose_dict(permutation)
            self.assertEqual(message.apply_transpose(enc_dict), 'Holla Warld!')
            enc_message = solution.EncryptedSubMessage(message.apply_transpose(enc_dict))
            self.assertEqual(enc_message.decrypt_message(), 'Hello World!')

            # Case 3
            message = solution.SubMessage('It work? otherwise...')
            permutation = 'iuaeo'
            enc_dict = message.build_transpose_dict(permutation)
            self.assertEqual(message.apply_transpose(enc_dict), 'At werk? ethurwasu...')
            enc_message = solution.EncryptedSubMessage(message.apply_transpose(enc_dict))
            self.assertEqual(enc_message.decrypt_message(), 'It work? otherwise...')

            # Note: caution when writing new test cases:
            # Sometimes the decryption fails because there are words that has only a vowel of diff, e.g: must, mist.
    return BaseSolutionTest

class TestSolution1(make_test(s1)):
    pass

if __name__ == '__main__':
    unittest.main()
