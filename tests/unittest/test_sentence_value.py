import unittest

from app.core.SentenceValue import SentenceValue


class TestSentenceValue(unittest.TestCase):

    def setUp(self):
        pass

    def test_sentence_parse(self):
        sentence = SentenceValue()
        sentence.parse("this is a demo")
        self.assertEqual(4, len(sentence.words))


def main():
    unittest.main()


if __name__ == '__main__':
    main()
