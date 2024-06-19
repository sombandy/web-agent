import streamlit as st
from src.scraper.scrapfly_util import ScrapFly

st.sidebar.markdown("Text")
st.write(open(ScrapFly.text_page).read())