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

    def rank(self, M, d: float = .85) -> None:
        """
        Implements the PageRank webpage ranking algorithm over an array of files or pages.
        More info: https://en.wikipedia.org/wiki/PageRank

        Parameters
        ----------
        M : numpy array
            adjacency matrix where M_i,j represents the link from 'j' to 'i', such that for all 'j'
            sum(i, M_i,j) = 1
        d : float, optional
            damping factor, by default 0.85

        Returns
        -------
        numpy array
            a vector of ranks such that v_i is the i-th rank from [0, 1],

        """

        N = M.shape[1]
        w = np.ones(N) / N
        M_hat = d * M
        v = M_hat @ w + (1 - d)
        while (np.linalg.norm(w - v) >= 1e-10):
            w = v
            v = M_hat @ w + (1 - d)
        return v
