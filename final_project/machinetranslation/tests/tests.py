'''
This module will test code
'''

import unittest

from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    ''' This class will test the English to French function '''
    def test_null_input(self):
        ''' This function will test null input '''
        self.assertNotEqual(english_to_french('None'), '')

    def test_translation(self):
        ''' This function will test the translation '''
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    ''' This class will test he French to English function '''
    def test_null_input(self):
        ''' This function will test null input '''
        self.assertNotEqual(french_to_english('None'), '')

    def test_translation(self):
        ''' This function will test the translation '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
