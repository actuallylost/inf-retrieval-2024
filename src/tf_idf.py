import numpy as np


class Rank:
    def term_frequency(self, word, file) -> float:
        word_count = file.get(word, 0)
        return np.log10(1 + word_count)

    def inverse_document_frequency(self, word, num_of_files) -> float:
        count_of_files = len(num_of_files) + 1
        count_of_fils_with_word = sum([1 for doc in num_of_files if word in doc]) + 1
        return np.log10(count_of_files / count_of_fils_with_word) + 1

    def tf_idf(self, word, file, num_of_files) -> float:
        tf = self.term_frequency
        idf = self.inverse_document_frequency

        return tf(word, file) * idf(word, num_of_files)
