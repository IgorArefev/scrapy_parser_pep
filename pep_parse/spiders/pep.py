import re
import scrapy
from pep_parse.items import PepParseItem
from pep_parse.settings import PATTERN


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        """Все ссылки на документы PEP."""
        peps = response.css('section#numerical-index td a::attr(href)')
        for pep_link in peps:
            yield response.follow(
                f'{pep_link.get()}/', callback=self.parse_pep
            )

    def parse_pep(self, response):
        """Собирает номер, название и статус PEP."""
        page_title = response.css('h1.page-title::text').get()
        number, name = re.search(PATTERN, page_title).groups()
        status = (
            response.css('dt:contains("Status") + dd abbr::text').get()
        )
        data = {
            'number': number,
            'name': name,
            'status': status,
        }
        yield PepParseItem(data)
