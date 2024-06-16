import numpy as np


class Rank:
    """
    Represents the Rank class. \n
    All algorithm implementations have been taken from - https://medium.com/@coldstart_coder/understanding-and-implementing-tf-idf-in-python-a325d1301484
    """

    def term_frequency(self, word, file) -> float:
        """
        Returns the term frequency for a given word, in a given file.
        """
        word_count = file.get(word, 0)
        return np.log10(1 + word_count)

    def inverse_document_frequency(self, word, num_of_files) -> float:
        """
        Returns the inverse document frequency for a given word, given a file corpus.
        """
        count_of_files = len(num_of_files) + 1
        count_of_fils_with_word = sum([1 for doc in num_of_files if word in doc]) + 1
        return np.log10(count_of_files / count_of_fils_with_word) + 1

    def tf_idf(self, word, file, num_of_files) -> float:
        """
        Returns the product of the term frequency and the inverse document frequency functions.
        """
        tf = self.term_frequency
        idf = self.inverse_document_frequency

        return tf(word, file) * idf(word, num_of_files)
