import os
from dotenv import load_dotenv
from scrapfly import ScrapeConfig, ScrapflyClient, ScrapeApiResponse

load_dotenv()

class ScrapFly:
    data_dir = "crawl_data"
    text_page = os.path.join(data_dir, "text.txt")
    html_page = os.path.join(data_dir, "html.html")
    markdown_page = os.path.join(data_dir, "markdown.md")
    screenshot_url = ""

    def __init__(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)

        self.scrapfly = ScrapflyClient(key=os.getenv("SCRAPFLY_API_KEY"))

    def scrape(self, url, **kwargs):
        format = kwargs.get("format", "text")
        config = ScrapeConfig(
            url=url,
            cache=True,
            country="US",
            format=format,
            render_js=True,
            screenshots={"main": "fullpage"},
        )

        api_response: ScrapeApiResponse = self.scrapfly.scrape(config)
        scrape_result = api_response.scrape_result

        ScrapFly.screenshot_url = (
            scrape_result["screenshots"]["main"]["url"] + "?key=" + os.getenv("SCRAPFLY_API_KEY")
        )
        self.content = scrape_result["content"]

        out_file = self.text_page
        if format == "clean_html":
            out_file = self.html_page
        elif format == "markdown":
            out_file = self.markdown_page

        print(f"Writing content to {out_file}")
        with open(out_file, "w") as f:
            f.write(self.content)

        return api_response.scrape_result
