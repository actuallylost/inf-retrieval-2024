import numpy as np


class Document:
    """
    This class represents a document that is instantiated with a list of files and a dictionary of tokens.
    """

    def __init__(self, file, tokens) -> None:
        self.file = ""
        self.tokens: dict[str, int] = {}

    def tokenize(self, file) -> dict[str, int]:
        """
        Takes a file and turns each word of the file into a token and pushes it into the tokens dictionary.
        """
        with open(file, "r") as f:
            for line in f:
                for token in line.split():
                    if token in self.tokens:
                        self.tokens[token] += 1
                    else:
                        self.tokens[token] = 1
        return self.tokens

    # TODO Change the arguments and return value
    def rank(self) -> None:
        """
        Implements the PageRank webpage ranking algorithm over an array of files or pages.
        """
        pass  # TODO Implement pagerank (https://en.wikipedia.org/wiki/PageRank#Python)
