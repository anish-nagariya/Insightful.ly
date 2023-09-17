import streamlit as st

# layout setup
st.set_page_config(page_title="Insightful.ly", page_icon=":wave:", layout="wide")

# ----Header Setup----
st.markdown("<h1 style='text-align: center; color: white;'>Insightful.ly</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: grey;'>Insightful.ly revolutionizes communication in academia while "
    "bridging the information gap to the public.</p>",
    unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Making the wonders of today the future of tomorrow.</p>",
            unsafe_allow_html=True)
f = open('../pages/summary-2.txt', 'r')
summary = f.read()
st.write(summary)
st.write('https://scitechdaily.com/dna-breakthrough-how-genetic-shedding-unveils-species-secrets/')
