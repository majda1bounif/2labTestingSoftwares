from unittest import TestCase
from string import split


class PossibleToSplit(TestCase):
    def test_split(self):
        actual = split(text="This.Savage.Tiger.", char1='.', char2='*')
        expected = "This*Savage*Tiger*"
        self.assertEqual(actual, expected)


class ImpossibleToSplit(TestCase):
    def test_split(self):
        actual = split(text="This.Savage.Tiger.", char1=' ', char2='\n')
        expected = "This.Savage.Tiger."
        self.assertEqual(actual, expected)
