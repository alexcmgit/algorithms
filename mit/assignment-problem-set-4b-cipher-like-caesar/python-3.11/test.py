import unittest
import solution as s1

def make_test(solution):
    class BaseSolutionTest(unittest.TestCase):
        def setUp(self) -> None:
            pass

        def test_encryption_and_decryption(self):
            # Case 1
            plain = solution.PlaintextMessage('hello', 2)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'jgnnq')
            self.assertTupleEqual(cipher.decrypt_message(), (24, 'hello'))

            # Case 2
            plain = solution.PlaintextMessage('hello', 1)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'ifmmp')
            self.assertTupleEqual(cipher.decrypt_message(), (25, 'hello'))

            # Case 3
            plain = solution.PlaintextMessage('hello', 25)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'gdkkn')
            self.assertTupleEqual(cipher.decrypt_message(), (1, 'hello'))

            # Case 4
            plain = solution.PlaintextMessage('Hello World, I am trying.', 3)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'Khoor Zruog, L dp wublqj.')
            self.assertTupleEqual(cipher.decrypt_message(), (23, 'Hello World, I am trying.'))

            # Case 5
            plain = solution.PlaintextMessage('Hello World, I am trying.', 0)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'Hello World, I am trying.')
            self.assertTupleEqual(cipher.decrypt_message(), (0, 'Hello World, I am trying.'))

            # Case 6
            plain = solution.PlaintextMessage('Hello World!!! Literally anything lorem.', 12)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'Tqxxa Iadxp!!! Xufqdmxxk mzkftuzs xadqy.')
            self.assertTupleEqual(cipher.decrypt_message(), (14, 'Hello World!!! Literally anything lorem.'))

            # Case 7
            plain = solution.PlaintextMessage('Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.', 14)
            cipher = solution.CiphertextMessage(plain.message_text_encrypted)

            self.assertEqual(plain.message_text_encrypted, 'Xoqy Tzcfsm wg o amhvwqoz qvofoqhsf qfsohsr cb hvs gdif ct o acasbh hc vszd qcjsf ob wbgittwqwsbhzm dzobbsr voqy. Vs vog pssb fsuwghsfsr tcf qzoggsg oh AWH hkwqs pstcfs, pih vog fsdcfhsrzm bsjsf doggsr oqzogg. Wh vog pssb hvs hforwhwcb ct hvs fsgwrsbhg ct Sogh Qoadig hc psqcas Xoqy Tzcfsm tcf o tsk bwuvhg soqv msof hc sriqohs wbqcawbu ghirsbhg wb hvs komg, asobg, obr shvwqg ct voqywbu.')
            self.assertTupleEqual(cipher.decrypt_message(), (12, 'Jack Florey is a mythical character created on the spur of a moment to help cover an insufficiently planned hack. He has been registered for classes at MIT twice before, but has reportedly never passed aclass. It has been the tradition of the residents of East Campus to become Jack Florey for a few nights each year to educate incoming students in the ways, means, and ethics of hacking.'))
    return BaseSolutionTest

class TestSolution1(make_test(s1)):
    pass

if __name__ == '__main__':
    unittest.main()


