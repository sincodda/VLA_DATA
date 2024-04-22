from w3lib.html import replace_escape_chars
import scrapy, json
from ..utils import cookie_parse

class InstaSpider(scrapy.Spider):
    name = 'insta'
    allowed_domains = ['www.instagram.com']
    #init the headers
    headers = {
        "x-asbd-id": 198387,
        "x-csrftoken": "gqeYY9dr1dCwfvtyZCgy88tcMn1A2N85",
        "x-ig-app-id": 936619743392459,
        "x-requested-with": "XMLHttpRequest"
    }
    
    hash = 'bahiabrava'

    def start_requests(self):
        yield scrapy.Request(
            url=f'https://www.instagram.com/api/v1/tags/web_info/?tag_name={self.hash}',
            cookies = cookie_parse(),
            headers=self.headers,
            callback=self.parse
        )
    
    def parse(self, response):
        # respuesta del  get
        resp = json.loads(response.body)
        # buscamos las secciones
        data = resp['data']['top']['sections']
        yield {
            "data": data,
        }
    
