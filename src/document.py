import re

import numpy as np
import pandas as pd

from text_preprocess import TextPreprocess


class Document:
    """
    This class represents a document that is instantiated with a list of files and a dictionary of tokens.
    """

    def __init__(self) -> None:
        self.file = ""
        self.tokens: dict[str, int] = {}

    def tokenize(self, file) -> dict[str, int]:
        """
        Takes a file and turns each word of the file into a token and pushes it into the tokens dictionary.
        """
        data_file = str(self.read_file(file))
        words = re.findall(r"\b\w+\b", data_file.lower())
        for token in words:
            p_token = str(token).strip().lower()
            if p_token in self.tokens:
                self.tokens[p_token] += 1
            else:
                self.tokens[p_token] = 1
        return self.tokens

    def rank(self, M, d: float = 0.85) -> None:
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
        while np.linalg.norm(w - v) >= 1e-10:
            w = v
            v = M_hat @ w + (1 - d)
        return v

    def read_file(self, file):
        tp = TextPreprocess()
        if file.type.split("/")[-1].lower() == "html":
            data_frames = pd.read_html(file)
            data = data_frames[0]
            return TextPreprocess.text_preprocess(tp, text=data.frames[0])

        else:
            content = file.read().decode("utf-8")
            return TextPreprocess.text_preprocess(tp, text=content)
