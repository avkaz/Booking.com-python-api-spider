import scrapy

class BookingspiderSpider(scrapy.Spider):
    name = "bookingspider"
    allowed_domains = ["booking.com"]
    start_urls = [
        'https://www.booking.com/searchresults.cs.html?label=gog235jc-1DCAEoggI46AdIBVgDaDqIAQGYAQW4AQfIAQ_YAQPoAQH4AQKIAgGoAgO4Av-uzKoGwAIB0gIkZGQ4NTc2NDMtOGM1Yy00MTk4LWEzZTQtYWU0NTBiOWFiMTI22AIE4AIB&aid=397594&ss=Praha%2C+%C4%8Cesk%C3%A1+republika&lang=cs&sb=1&src_elem=sb&src=index&dest_id=-553173&dest_type=city&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=25'
    ]

    def parse(self, response):
        # hotel_xpath = '/html/body'  # Adjust the XPath based on your HTML structure
        # hotel_html = response.xpath(hotel_xpath).extract()
        #     def parse(self, response):
        #         hotel_selector = response.css('div[data-et-view="OATBaQJbVTbZXWSYHCSdUWAUC:1"] div.sr__card')
        #         hotel_html = hotel_selector
        #         yield {'html': len(hotel_html)}
        hotels = response.css('div[data-capla-component-boundary="b-lp-web-mfe/TargetedHotels"]')
        hotel = hotels.css('h3')

        yield {'html': len(hotel)}

        # https: // www.booking.com / searchresults.cs.html?ss = Praha & ssne = Praha & ssne_untouched = Praha & label = gog235jc - 1
        #
        # DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB & sid = a326d50f4f5fac494b51155a82a4508a & aid = 397594 & lang = cs & sb = 1 & src_elem = sb & src = searchresults & dest_id = -553173 & dest_type = city & checkin = 2023 - 11 - 14 & checkout = 2023 - 11 - 15 & group_adults = 1 & no_rooms = 1 & group_children = 0
        # https: // www.booking.com / searchresults.cs.html?label = gog235jc - 1
        # DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB & sid = a326d50f4f5fac494b51155a82a4508a & aid = 397594 & ss = Praha & ssne = Praha & ssne_untouched = Praha & lang = cs & sb = 1 & src_elem = sb & src = searchresults & dest_id = -553173 & dest_type = city & checkin = 2023 - 11 - 14 & checkout = 2023 - 11 - 15 & group_adults = 1 & no_rooms = 1 & group_children = 0 & offset = 25
        # https: // www.booking.com / searchresults.cs.html?label = gog235jc - 1
        # DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB & sid = a326d50f4f5fac494b51155a82a4508a & aid = 397594 & ss = Praha & ssne = Praha & ssne_untouched = Praha & lang = cs & sb = 1 & src_elem = sb & src = searchresults & dest_id = -553173 & dest_type = city & checkin = 2023 - 11 - 14 & checkout = 2023 - 11 - 15 & group_adults = 1 & no_rooms = 1 & group_children = 0 & offset = 50
        # https: // www.booking.com / searchresults.cs.html?label = gog235jc - 1
        # DCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQPoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIE4AIB & sid = a326d50f4f5fac494b51155a82a4508a & aid = 397594 & ss = Praha & ssne = Praha & ssne_untouched = Praha & lang = cs & sb = 1 & src_elem = sb & src = searchresults & dest_id = -553173 & dest_type = city & checkin = 2023 - 11 - 14 & checkout = 2023 - 11 - 15 & group_adults = 1 & no_rooms = 1 & group_children = 0 & offset = 0
        #