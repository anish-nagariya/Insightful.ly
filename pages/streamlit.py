import streamlit as st
from PIL import Image
from summarize import analyze
from streamlit_option_menu import option_menu

# layout setup
st.set_page_config(page_title="Insightful.ly", page_icon=":wave:", layout="wide")

# ----Header Setup----
st.markdown("<h1 style='text-align: center; color: white;'>Insightful.ly</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: grey;'>Insightful.ly revolutionizes communication in academia while "
    "bringing information to the public.</p>",
    unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Making the wonders of today the future of tomorrow.</p>",
            unsafe_allow_html=True)

# navbar setup
selected = option_menu(
    menu_title = None,
    options=["You", "Hot", "Explore"],
    icons=["bell", "fire", "search-heart"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

K = set(range(5))
keys = ['da', 'daf','fdaf', 'fadad', 'dasfoia', 'dafjda']
if selected == "You":
    # Feed section:
    headlines, summarys, locs = [], [], []
    for i in range(len(K)):
        headline, summary, loc = analyze(i + 1)
        headlines.append(headline)
        summarys.append(summary)
        f = open(f"summary-{i}.txt", 'w')
        f.write(summary)
        f.close()
        locs.append(loc)
    i = 0
    while K:
        # with st.container():
        # st.write("---")
        left_column, mid, right_column = st.columns(3)
        with left_column:
            i = min(K)
            while i in K:
                st.image(Image.open(locs[i]), use_column_width=True)
                st.subheader(f'**{headlines[i]}**')

                label = st.checkbox("❤", key=keys[i])

                st.write("[Read More...>](http://localhost:8501/article1)")
                K.remove(i)
                i += 3
        with mid:
            i = min(K)
            while i in K:
                st.image(Image.open(locs[i]), use_column_width=True)
                st.subheader(f'**{headlines[i]}**')

                #check
                st.checkbox("❤", key=keys[i])


                st.write("[Read More...>](http://localhost:8501/article2)")

                K.remove(i)
                i += 3
        with right_column:
            i = min(K)
            while i in K:
                st.image(Image.open(locs[i]), use_column_width=True)
                st.subheader(f'**{headlines[i]}**')

                #check
                st.checkbox("❤", key=keys[i])

                st.write("[Read More...>](http://localhost:8501/article3)")
                K.remove(i)
                i += 3
if selected == "Hot":
    # Feed section:
    headlines, summarys, locs = [], [], []
    for i in range(len(K)):
        headline, summary, loc = analyze(i + 1)
        headlines.append(headline)
        summarys.append(summary)
        locs.append(loc)
    headlines.reverse()
    summarys.reverse()
    locs.reverse()
    i = 0
    while i in K:
        with st.container():
            st.write("---")
            left_column, mid, right_column = st.columns(3)
            with left_column:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)

                    check = st.checkbox("27 ❤", key=keys[i])

                    st.write("[Read More...>](http://localhost:8501/article1)")
                    i += 3
            with mid:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)

                    st.checkbox("20 ❤", key=keys[i])

                    st.write("[Read More...>](http://localhost:8501/article2)")
                    i += 3
            with right_column:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)
                    st.checkbox("9 ❤", key=keys[i])

                    st.write("[Read More...>](http://localhost:8501/article3)")
                    i += 3
if selected == "Explore":
    # Feed section:
    headlines, summarys, locs = [], [], []
    for i in range(K):
        headline, summary, loc = analyze(i + 1)
        headlines.append(headline)
        summarys.append(summary)
        locs.append(loc)
    i = 0
    while K:
        with st.container():
            st.write("---")
            left_column, mid, right_column = st.columns(3)
            with left_column:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)
                    st.checkbox("❤")
                    st.write("[Read More...>](http://localhost:8501/article1)")
                    i += 3
            with mid:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)
                    st.checkbox("❤", key="a")
                    st.write("[Read More...>](http://localhost:8501/article2)")
                    i += 3
            with right_column:
                i = min(K)
                while i in K:
                    st.subheader(f'**{headlines[i]}**')
                    st.image(Image.open(locs[i]), use_column_width=True)
                    st.checkbox("❤", key="b")
                    st.write("[Read More...>](http://localhost:8501/article3)")
                    i += 3


