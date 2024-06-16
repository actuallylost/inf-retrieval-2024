import string

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from word2number import w2n


class TextPreprocess:
    """
    Text Preprocessing class.
    """

    def __init__(self):
        nltk.download("punkt")

    def convert_numbers_to_words(self, text: str):
        """
        Converts numbers to words (ex. 5 -> "five").

        Parameters
        ----------
        text : str
                text to check for numbers to convert.
        """
        temp_text: list[str] = text.split(sep=" ")
        new_string = []

        for i in range(len(temp_text)):
            if temp_text[i].isdigit():
                temp = w2n.word_to_num(temp_text[i])
                new_string.append(temp)
            else:
                new_string.append(temp_text[i])

        temp_text = new_string
        return " ".join(temp_text)

    def remove_punctuation(self, text: str):
        """
        Removes punctuation from given text.

        Parameters
        ----------
        text : str
                text to remove punctuation from.
        """
        punctuation_to_remove = string.punctuation.replace(",", "")
        translator = str.maketrans("", "", punctuation_to_remove)
        return text.translate(translator)

    def remove_whitespace(self, text: str):
        """
        Removes whitespace from given text.

        Parameters
        ----------
        text : str
                text to remove whitespace from.
        """
        return " ".join(text.split())

    def text_preprocess(
        self,
        text: str,
    ):
        p_text = self.convert_numbers_to_words(text=text)
        p_text = self.remove_punctuation(text=text)
        p_text = self.remove_whitespace(text=text)
        return p_text.split()
