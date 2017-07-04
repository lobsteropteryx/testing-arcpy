from unittest import TestCase
from my_project.updater import init_cap

class TestCapper(TestCase):

    def test_returns_empty_string_if_field_is_empty(self):
        expected = ''
        actual = init_cap('')
        self.assertEqual(actual, expected)
        
    def test_captalizes_first_letter_of_single_word(self):
        expected = 'Foo'
        actual = init_cap('foo')
        self.assertEqual(actual, expected)
        
    def test_captalizes_first_letter_of_multiple_words(self):
        expected = 'Foo Bar'
        actual = init_cap('foo bar')
        self.assertEqual(actual, expected)        


    def test_does_not_captalize_words_that_start_with_numbers(self):
        expected = '3g'
        actual = init_cap('3g')
        self.assertEqual(actual, expected)
