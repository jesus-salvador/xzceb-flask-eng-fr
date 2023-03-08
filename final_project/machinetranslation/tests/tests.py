import unittest
from translator import english_to_french
from translator import french_to_english


class TestEnglishToFrench(unittest.TestCase):
    def test_1_null(self):
        # check that english_to_french fails when text is null
        with self.assertRaises(ValueError):
            english_to_french(None)

    def test_2_translation(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')


class TestFrenchToEnglish(unittest.TestCase):
    def test_1_null(self):
        # check that french_to_english fails when text is null
        with self.assertRaises(ValueError):
            french_to_english(None)

    def test_2_translation(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')


if __name__ == '__main__':
    unittest.main()
