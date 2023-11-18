# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookingScrapperItem(scrapy.Item):
    name = scrapy.Field()
    stars = scrapy.Field()
    rating = scrapy.Field()
    review_count = scrapy.Field()
    distance_from_center = scrapy.Field()
    check_in_date = scrapy.Field()
    check_out_date = scrapy.Field()
    min_price = scrapy.Field()
    currency = scrapy.Field()
    url = scrapy.Field()