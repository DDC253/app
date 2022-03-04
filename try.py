import streamlit as st
!pip install pydub --quiet

def main():
	st.title("Audio data time-alignment")
	st.subheader("retrieve transcription from Word documents")

if __name__ == '__main__':
	main()


uploaded_file = st.file_uploader("Upload your audio file")

