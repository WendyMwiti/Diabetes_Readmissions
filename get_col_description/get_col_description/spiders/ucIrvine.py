import scrapy


class UcirvineSpider(scrapy.Spider):
    name = "ucIrvine"
    allowed_domains = ["archive.ics.uci.edu"]
    start_urls = ["https://archive.ics.uci.edu/dataset/296/diabetes+130-us+hospitals+for+years+1999-2008"]

    def parse(self, response):
        pass