import streamlit as st

from document import Document


def main():
    st.header("Inf. Retrieval")
    st.title("Simple Search engine")

    uploaded_files = st.file_uploader(
        "Upload simple TXT or HTML files",
        type=["txt", "html"],
        accept_multiple_files=True,
    )

    if uploaded_files is not None:

        file_tokens = {}

        for i, uploaded_file in enumerate(uploaded_files):
            dc = Document()
            tokens = Document.tokenize(dc, uploaded_file)
            file_tokens[uploaded_file.name] = tokens

        search_query = st.text_input("Search your files ...")
        if search_query:
            query_tokens = Document.tokenize(Document(), search_query)
            matching_files = {}

            for file_name, tokens in file_tokens.items():
                if any(query_token in tokens for query_token in query_tokens):
                    matching_files[file_name] = tokens

            if matching_files:
                st.write("Matching files: ")
                for file_name in matching_files:
                    st.write(file_name)
            else:
                st.write("No matches found :(")


if __name__ == "__main__":
    main()
