import string

import nltk
from nltk.tokenize import word_tokenize


class TextPreprocess:
    """
    Text Preprocessing class.
    """

    def __init__(self):
        nltk.download("punkt")

    def remove_punctuation(self, text: str):
        """
        Removes punctuation from given text.
        """
        punctuation_to_remove = string.punctuation.replace(",", "")
        translator = str.maketrans("", "", punctuation_to_remove)
        return text.translate(translator)

    def remove_whitespace(self, text: str):
        """
        Removes whitespace from given text.
        """
        return " ".join(text.split())

    def text_preprocess(
        self,
        text: str,
    ):
        p_text = self.remove_punctuation(text=text)
        p_text = self.remove_whitespace(text=text)
        return p_text.split()
