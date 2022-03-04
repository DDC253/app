import streamlit as st

def main():
	st.title("Audio data time-alignment")
	st.subheader("retrieve transcription from Word documents")

if __name__ == '__main__':
	main()


uploaded_file = st.file_uploader("Upload your audio file")

st.download_button('Download CSV', uploaded_file, 'text/csv')
