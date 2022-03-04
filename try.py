import streamlit as st

PAGE_CONFIG = {"page_title":"Align audio data to transcription","page_icon":":smiley:","layout":"centered"}
st.beta_set_page_config(**PAGE_CONFIG)
def main():
	st.title("Audio data time-alignment")
	st.subheader("retrieve transcription from Word documents")

if __name__ == '__main__':
	main()
