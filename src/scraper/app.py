import streamlit as st

from src.scraper.scrapfly_util import ScrapFly

url = st.text_input("Website", "https://clear.ventures/")
task = st.text_area("Task", "For future use only!")
scrape = st.button("Scrape")

if scrape and url:
    scraply = ScrapFly()

    st.markdown("### Text Content")
    response = scraply.scrape(url, format="text")
    st.text_area("", response["content"], height=400)
    st.markdown("Number of tokens:  __%d__" % (len(response["content"]) / 4))

    st.markdown("### Markdown Content")
    response = scraply.scrape(url, format="markdown")
    st.text_area("", response["content"], height=400)
    st.markdown("Number of tokens:  __%d__" % (len(response["content"]) / 4))

    st.markdown("### HTML Content")
    response = scraply.scrape(url, format="clean_html")
    st.text_area("", response["content"], height=400)
    st.markdown("Number of tokens:  __%d__" % (len(response["content"]) / 4))

    st.markdown("### JSON Response")
    st.json(response, expanded=False)
