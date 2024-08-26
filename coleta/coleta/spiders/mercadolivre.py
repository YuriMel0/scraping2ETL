import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/tenis-de-corrida-masculino#D[A:tenis%20de%20corrida%20masculino]"]

    def parse(self, response):
        pass
