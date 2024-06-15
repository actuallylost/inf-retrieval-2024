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

        tokens = {}

        for i in range(len(uploaded_files)):
            dc = Document(uploaded_files[i], tokens=tokens)

            tokens = Document.tokenize(dc, file=uploaded_files[i])
            st.write(tokens)


if __name__ == "__main__":
    main()
