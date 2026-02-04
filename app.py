import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="UAS Rekayasa Fitur", layout="centered")
st.title("Analisis Sentimen Teks")
st.write("UAS Rekayasa Fitur – Analisis Sentimen menggunakan API")

teks = st.text_area("Masukkan teks yang ingin dianalisis:")

if st.button("Analisis Sentimen"):
    if teks.strip() == "":
        st.warning("Teks tidak boleh kosong!")
    else:
        blob = TextBlob(teks)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentimen = "Positive"
        elif polarity < 0:
            sentimen = "Negative"
        else:
            sentimen = "Neutral"

        st.success(f"Hasil Sentimen: {sentimen}")
        st.info(f"Nilai Polaritas: {polarity:.2f}")
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="UAS Rekayasa Fitur", layout="centered")
st.title("Analisis Sentimen Teks")
st.write("UAS Rekayasa Fitur – Analisis Sentimen menggunakan API")

teks = st.text_area("Masukkan teks yang ingin dianalisis:")

if st.button("Analisis Sentimen"):
    if teks.strip() == "":
        st.warning("Teks tidak boleh kosong!")
    else:
        blob = TextBlob(teks)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentimen = "Positive"
        elif polarity < 0:
            sentimen = "Negative"
        else:
            sentimen = "Neutral"

        st.success(f"Hasil Sentimen: {sentimen}")
        st.info(f"Nilai Polaritas: {polarity:.2f}")
import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="UAS Rekayasa Fitur", layout="centered")
st.title("Analisis Sentimen Teks")
st.write("UAS Rekayasa Fitur – Analisis Sentimen menggunakan API")

teks = st.text_area("Masukkan teks yang ingin dianalisis:")

if st.button("Analisis Sentimen"):
    if teks.strip() == "":
        st.warning("Teks tidak boleh kosong!")
    else:
        blob = TextBlob(teks)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentimen = "Positive"
        elif polarity < 0:
            sentimen = "Negative"
        else:
            sentimen = "Neutral"

        st.success(f"Hasil Sentimen: {sentimen}")
        st.info(f"Nilai Polaritas: {polarity:.2f}")
