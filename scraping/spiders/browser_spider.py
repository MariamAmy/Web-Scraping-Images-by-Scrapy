import scrapy

class BrowserSpider(scrapy.Spider):
    name = "browser"
    start_urls = ["https://www.istockphoto.com/photos/cute-dog"]

    def parse(self, response):
        links = response.xpath("//img/@src")
        html = ""

        for link in links:
            url = link.get()

            
            if any(extn in url for extn in [".jpg", ".gif", ".jpeg", ".png"]):
                html += """<a href="{url} "target="_blank">
                <img src="{url}" height="25%" width="25%">
                </a>""".format(url=url)

                with open("output-4.html", "a") as page:
                    page.write(html)
                    