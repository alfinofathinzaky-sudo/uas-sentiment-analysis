import streamlit as st
import requests
import os

API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
API_TOKEN = os.getenv("HF_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def analisis_sentimen(teks):
    response = requests.post(
        API_URL,
        headers=HEADERS,
        json={"inputs": teks}
    )
    return response.json()

st.set_page_config(page_title="UAS Rekayasa Fitur", layout="centered")
st.title("Analisis Sentimen Teks")
st.write("UAS Rekayasa Fitur – Analisis Sentimen menggunakan API")

teks = st.text_area("Masukkan teks yang ingin dianalisis:")

if st.button("Analisis Sentimen"):
    if teks.strip() == "":
        st.warning("Teks tidak boleh kosong!")
    else:
        hasil = analisis_sentimen(teks)

        # CEK JIKA API ERROR / MODEL LOADING
        if isinstance(hasil, dict) and "error" in hasil:
            st.error("Model sedang loading atau API error. Silakan coba lagi beberapa saat.")
        else:
            try:
                label = hasil[0][0]["label"]
                skor = hasil[0][0]["score"]

                st.success(f"Hasil Sentimen: {label}")
                st.info(f"Tingkat Kepercayaan: {skor:.2f}")
            except Exception as e:
                st.error("Terjadi kesalahan saat memproses hasil analisis.")
