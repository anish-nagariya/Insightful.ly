import streamlit as st
from PIL import Image
from summarize import analyze
from streamlit_option_menu import option_menu

# layout setup
st.set_page_config(page_title="Research Times", page_icon=":wave:", layout="wide")

# ----Header Setup----
st.markdown("<h1 style='text-align: center; color: grey;'>Research Times</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: grey;'>Research Times revolutionizes communication in academia while "
    "bridging the information gap to the public.</p>",
    unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Making the wonders of today the future of tomorrow.</p>",
            unsafe_allow_html=True)

# navbar setup
selected = option_menu(
    menu_title = None,
    options=["You", "Hot", "Explore"],
    icons=["bell", "fire", "search-heart"],
    menu_icon="cast",
    default_index=1,
    orientation="horizontal",
)

# Feed section:
K = 3
headlines, summarys, locs = [], [], []
for i in range(K):
    headline, summary, loc = analyze(i + 1)
    headlines.append(headline)
    summarys.append(summary)
    locs.append(loc)
headlines.reverse()
summarys.reverse()
locs.reverse()
i = 0
while i < K:
    with st.container():
        st.write("---")
        left_column, mid, right_column = st.columns(3)
        with left_column:
            if i < K:
                st.subheader(f'**{headlines[i]}**')
                st.image(Image.open(locs[i]), use_column_width=True)

                check = st.checkbox(":heart: 27",)

                # if(check):
                #     check.label= "❤ 28"


                st.write("[Read More...>]()")
                i += 1
        with mid:
            if i < K:
                st.subheader(f'**{headlines[i]}**')
                st.image(Image.open(locs[i]), use_column_width=True)

                st.checkbox("❤", label=20, key="a")


                st.write("[Read More...>]()")
                i += 1
        with right_column:
            if i < K:
                st.subheader(f'**{headlines[i]}**')
                st.image(Image.open(locs[i]), use_column_width=True)
                st.checkbox("❤", label=9, key="b")

                st.write("[Read More...>]()")
                i += 1
