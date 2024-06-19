import streamlit as st
from src.scraper.scrapfly_util import ScrapFly

st.sidebar.markdown("Screenshot")
st.image(ScrapFly.screenshot_url)