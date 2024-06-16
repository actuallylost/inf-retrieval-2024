import streamlit as st

from document import Document
from rank import Rank


def main():
    st.header("Inf. Retrieval")
    st.title("Simple Search engine")

    uploaded_files = st.file_uploader(
        "Upload one or multiple text or html files",
        type=["txt", "html"],
        accept_multiple_files=True,
    )

    if uploaded_files is not None:
        file_tokens = {}
        all_tokens = []

        for i, uploaded_file in enumerate(uploaded_files):
            dc = Document()
            tokens = Document.tokenize(dc, uploaded_file)
            file_tokens[uploaded_file.name] = tokens
            all_tokens.extend(tokens)

        search_query = st.text_input("Search a term...")
        if search_query:
            ranker = Rank()
            query_tokens = Document.tokenize(Document(), search_query)
            matching_files = {}

            for file_name, tokens in file_tokens.items():
                total_score = 0
                for query_token in query_tokens:
                    if query_token in tokens:
                        total_score += ranker.tf_idf(query_token, tokens, all_tokens)
                matching_files[file_name] = total_score

            sorted_files = sorted(
                matching_files.items(), key=lambda item: item[1], reverse=True
            )

            if sorted_files:
                st.write("Your term appears in the following files: ")
                for file_name, score in sorted_files:
                    st.write(f"{file_name} (Relevancy Score: {score})")
            else:
                st.write("No matches found :(")


if __name__ == "__main__":
    main()
