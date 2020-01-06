import scrapy
from scrapy.http import FormRequest


class RentSpider(scrapy.Spider):
    name = 'testingspider'

    place_list = ['place1', 'place2']
    for place in place_list:
        def start_requests(self):
            city = place

            yield FormRequest(
                url='url',
                method='POST',

                formdata={ "place": city},
                callback=self.parse
            )

    def parse(self, response):

        for renthouse in response.xpath("//div[@class='flight-item']"):
            price = response.xpath('.//div/span/text()').get()
            ZIP_Code = renthouse.xpath('.//span/div/span/text()').get()
            
            yield {
                'price' : price,
                'code': ZIP_Code,
            }
