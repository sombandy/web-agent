import streamlit as st
from src.scraper.scrapfly_util import ScrapFly

st.sidebar.markdown("Scrape Data")

st.markdown("### Text")
with open(ScrapFly.text_page) as f:
    content = f.read()
    st.text_area("", content, height=400)
    st.markdown("Number of tokens:  __%d__" % (len(content) / 4))

st.markdown("### Markdown")
with open(ScrapFly.markdown_page) as f:
    content = f.read()
    st.text_area("", content, height=400)
    st.markdown("Number of tokens:  __%d__" % (len(content) / 4))

st.markdown("### HTML")
with open(ScrapFly.html_page) as f:
    content = f.read()
    st.text_area("",content, height=400)
    st.markdown("Number of tokens:  __%d__" % (len(content) / 4))
