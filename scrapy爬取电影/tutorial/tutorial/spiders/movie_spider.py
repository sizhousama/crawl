import scrapy

from tutorial.items import MovieItem


class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["meijutt.com"]
    start_urls = ['http://www.meijutt.com/new100.html']


     
    def parse(self,response):
        sel = scrapy.selector.Selector(response)
        sites = sel.xpath('//ul/li/h5')
        item = MovieItem()
        for site in sites:
            
            item['title'] = site.xpath('a/text()').extract()[0]
            item['link'] = 'http://www.meijutt.com/' + site.xpath('a/@href').extract()[0]
            

            yield item
            

            
            
           
            
