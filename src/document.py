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
        Takes a file and returns a dictionary indicating each token and how many times it's been found within the given data.
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

    def read_file(self, file) -> list[str]:
        """
        Reads an HTML or TXT File and returns a list of the file's lines.
        """
        tp = TextPreprocess()
        if file.type.split("/")[-1].lower() == "html":
            table = bfs(file).text
            print(table)
            return TextPreprocess.text_preprocess(tp, text=str(table))

        else:
            content = file.read().decode("utf-8")
            return TextPreprocess.text_preprocess(tp, text=content)
