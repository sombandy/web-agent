import streamlit as st
from src.scraper.scrapfly_util import ScrapFly

st.html(open(ScrapFly.html_page).read())
