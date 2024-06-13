import string

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem.porter import PorterStemmer
from nltk.tokenize import word_tokenize
from word2number import w2n


class TextPreprocess:
    """
    Text Preprocessing class.
    """

    # def __init__(self):

    def to_lowercase(self, text: list[str]):
        """
        Parameters
        ----------
        text : str
                text to lower.
        """
        return [x.lower() for x in text]

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
        return temp_text

    def remove_punctuation(self, text):
        """
        Removes punctuation from given text.

        Parameters
        ----------
        text : str
                text to remove punctuation from.
        """
        translator = str.maketrans("", "", string.punctuation)
        return text.translate(translator)

    def remove_whitespace(self, text):
        """
        Removes whitespace from given text.

        Parameters
        ----------
        text : str
                text to remove whitespace from.
        """
        return " ".join(text.split())

    def remove_default_stopwords(self, text):
        """
        Remove default stopwords from given text.

        Parameters
        ----------
        text : str
                text to remove default stopwords from.
        """
        stop_words = set(stopwords.words("english"))
        word_tokens = word_tokenize(text)
        filtered_text = [word for word in word_tokens if word not in stop_words]
        return filtered_text

    def stem_words(self, text):
        """
        Gets the root forms for the words from given text.

        Parameters
        ----------
        text : str
                text to replace each word with its stem.

        Example
        -------
        books      --->    book\n
        looked     --->    look\n
        denied     --->    deni\n
        flies      --->    fli\n
        """
        stemmer = PorterStemmer()
        word_tokens = word_tokenize(text)
        stems = [stemmer.stem(word) for word in word_tokens]
        return stems

    def lemmanize_words(self, text):
        """
        Converts words to their root from, while ensuring they belong to the language.

        Parameters
        ----------
        text : str
                text to convert each word with its root form.

        Example
        -------
        Input: 'data science uses scientific methods algorithms and many types of processes'\n
        Output: ['data', 'science', 'use', 'scientific', 'methods', 'algorithms', 'and', 'many', 'type', 'of', 'process']
        """
        lemmatizer = WordNetLemmatizer()
        word_tokens = word_tokenize(text)
        lemmas = [lemmatizer.lemmatize(word) for word in word_tokens]
        return lemmas

    def text_preprocess(
        self, text, stem_words: bool = False, lemmanize_words: bool = False
    ):
        text = self.to_lowercase(text=text)
        text = self.convert_numbers_to_words(text=text)
        text = self.remove_punctuation(text=text)
        text = self.remove_whitespace(text=text)
        text = self.remove_default_stopwords(text=text)
        if stem_words:
            text = self.stem_words(text=text)
        if lemmanize_words:
            text = self.lemmanize_words(text=text)
        return text
