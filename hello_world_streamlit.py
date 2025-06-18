import streamlit as st

translations = {
    "English": "Hello world",
    "German": "Hallo Welt",
    "French": "Bonjour le monde",
    "Spanish": "Hola mundo",
    "Italian": "Ciao mondo",
    "Portuguese": "Olá mundo",
    "Russian": "Привет мир",
    "Chinese": "你好，世界",
    "Japanese": "こんにちは世界",
    "Arabic": "مرحبا بالعالم"
}

st.title("Hello World Translator")

language = st.selectbox("Choose a language", list(translations.keys()))

if st.button("Translate"):
    st.write(translations[language])
