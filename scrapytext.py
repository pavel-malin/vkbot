# Scrapy будет использовать для поиск новых URL-адресов на каждой сканируемой странице

from scrapy.contrib.spides import CrawSpider, Rule
from wikiSpider.items import Article
from scrapy.contrib.linkextractor.sgml import SgmlLinkExtractor

class ArticleSpider(CrawSpider):
    name = "article"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["http://wikipedia.org/wiki/Python_%28programming_language%29"]
    rules = [Rule(SgmlLinkExtractor=('(/wiki/)((?!:).)*$'),callback="parse_item", follow=True)]
    def parse_item(self,response):
        item = Article()
        title = response.xpath('//h1/text()'[0].extract())
        print("Title is: "+title)
        item['title'] = title
        return item


