import streamlit as st
from src.scraper.scrapfly_util import ScrapFly

st.markdown(open(ScrapFly.markdown_page).read(), unsafe_allow_html=True)
