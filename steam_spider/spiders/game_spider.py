import scrapy
# id = genre-flyout

class Games(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    price = scrapy.Field()


#class SteamMinePrices(scrapy.Spider):
#    name = 'steam_spider'
#    start_urls = ['https://store.steampowered.com/games'] 
#
#    def parse(self, response):
#        pages = response.xpath("//div[@id='genre_flyout']/div/a/@href")
#        for page in pages:
#            link = page.extract()
#            self.log('going to page %s' %link) 
#            scrapy.http.Request(link, self.handle_games)
#            self.log('hello there')
#
#
#    def handle_games(self, response):
#        games = response.xpath("//div[@id='tab_NewReleases_content']//a//div[@class='discount_prices']")
#        self.log('hello bananas')
#
#        
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
            #self.log('game%s'%game.extract())
            yield {
                    'price': game.xpath("div[@class='discount_block tab_item_discount no_discount']/div[@class='discount_prices']//text()").extract(),
                    }  













