import streamlit as st


class SearchEngine:
    def __init__(self) -> None:
        self.array = []
        self.tokens = []
        self.files = []

    def file_upload(self):
        self.files = st.file_uploader(
            "Please upload up to 100 simple text or HTML files.",
            type=["txt", "html"],
            accept_multiple_files=True,
        )
        
    def 
                
