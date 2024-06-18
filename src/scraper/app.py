import streamlit as st

from src.scraper.scrapfly_util import ScrapFly

url = st.text_input("Website", "https://clear.ventures/")
task = st.text_area("Task", "Who are the general partners?")
scrape = st.button("Scrape")

if scrape and url:
    scraply = ScrapFly()
    response = scraply.scrape(url, format="text")
    st.sidebar.page_link(scraply.screenshot_url, label="Screenshot")

    st.markdown("### Text Content")
    st.text_area("", response["content"], height=400)

    response = scraply.scrape(url, format="markdown")
    st.markdown("### Markdown Content")
    st.text_area("", response["content"], height=400)

    response = scraply.scrape(url, format="clean_html")
    st.markdown("### HTML Content")
    st.text_area("", response["content"], height=400)

    st.markdown("### JSON Response")
    st.json(response, expanded=False)
