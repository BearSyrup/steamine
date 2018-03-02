import scrapy
# id = genre-flyout

class Games(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()
      
class SteamSpider(scrapy.Spider):
    name = 'steam_spider'

    start_urls = ['https://store.steampowered.com/games']
    
    def parse(self, response):
        urls = response.xpath("//div[@id='genre_flyout']/div/a/@href")
        for url in urls.extract():
            yield response.follow(url, self.get_games) 


    def get_games(self, response):
        games = response.xpath("//div[@id='NewReleasesRows']//a")
        for game in games:
            yield {
                    'price': game.xpath("div[@class='discount_block tab_item_discount no_discount']/div[@class='discount_prices']//text()").extract(),
                    }  













