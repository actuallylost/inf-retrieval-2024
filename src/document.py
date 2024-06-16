import re

import numpy as np
import pandas as pd
from bs4 import BeautifulSoup as bfs

from text_preprocess import TextPreprocess


class Document:
    """
    This class represents a document that is instantiated with a list of files and a dictionary of tokens.
    """

    def __init__(self) -> None:
        self.file = ""
        self.tokens: dict[str, int] = {}

    def tokenize(self, input_data) -> dict[str, int]:
        """
        Takes a file and turns each word of the file into a token and pushes it into the tokens dictionary.

        Parameters
        ----------
        input_data: str | file-like object
            Data to tokenize.

        Returns
        -------
        dict[str, int]
            Returns a dictionary with each token and its corresponding counter.
        """
        if isinstance(input_data, str):
            data = input_data
        else:
            data = str(self.read_file(input_data))
        words = re.findall(r"\b\w+\b", data.lower())
        for token in words:
            p_token = str(token).strip().lower()
            if p_token in self.tokens:
                self.tokens[p_token] += 1
            else:
                self.tokens[p_token] = 1
        return self.tokens

    def rank(self, files) -> None:
        pass

    def read_file(self, file) -> list[str]:
        """
        Reads an HTML or TXT File.

        Parameters
        ----------
        file: file-like object
            File to read.

        Returns
        -------
        list[str]
            a list of the file's lines that have been preprocessed using TextPreprocess class.
        """
        tp = TextPreprocess()
        if file.type.split("/")[-1].lower() == "html":
            table = bfs(file).text
            print(table)
            return TextPreprocess.text_preprocess(tp, text=str(table))

        else:
            content = file.read().decode("utf-8")
            return TextPreprocess.text_preprocess(tp, text=content)
