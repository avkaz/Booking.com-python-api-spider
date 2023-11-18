import scrapy
import json
from Booking_scrapper.api_request import APIRequest
from Booking_scrapper.items import BookingScrapperItem
from datetime import datetime, timedelta

language = 'cs'

class HotelSpider(scrapy.Spider):
    name = 'hotelspider'
    def start_requests(self):
        api = APIRequest()
        url = "https://www.booking.com/dml/graphql"

        # Iterate through days
        start_date = datetime(2023, 11, 20)
        end_date = datetime(2023, 11, 21)

        for current_date in range((end_date - start_date).days + 1):

            # Iterate through offsets
            for offset in range(0, 2000, 100):
                headers = api.get_headers(offset)
                payload = api.get_payload(offset, start_date + timedelta(days=current_date))
                querystring = api.get_querystring(start_date + timedelta(days=current_date))

                # Construct the URL with query parameters
                full_url = f"{url}?{'&'.join(f'{key}={value}' for key, value in querystring.items())}"

                yield scrapy.Request(
                    url=full_url,
                    method='POST',
                    body=json.dumps(payload),  # Convert payload to JSON string
                    headers=headers,
                    callback=self.parse,
                    meta={'dont_redirect': True, 'handle_httpstatus_list': [301, 302]},
                    dont_filter=True
                )


    def parse(self, response):
        data = json.loads(response.text)
        results = data.get('data', {}).get('searchQueries', {}).get('search', {}).get('results', [])
        check_in = data.get('data', {}).get('searchQueries', {}).get('search', {}).get('searchMeta', {}).get('dates',
                                                                                                             {}).get(
            'checkin')
        check_out = data.get('data', {}).get('searchQueries', {}).get('search', {}).get('searchMeta', {}).get('dates',
                                                                                                              {}).get(
            'checkout')

        # Iterate through the results
        for result in results:
            try:
                # Accessing the relevant information with exception handling
                hotel_item = BookingScrapperItem()
                hotel_item['name'] = result.get('displayName', {}).get('text')
                hotel_item['stars'] = result.get('basicPropertyData', {}).get('starRating', {}).get('value')
                hotel_item['rating'] = result.get('basicPropertyData', {}).get('reviewScore', {}).get('score')
                hotel_item['review_count'] = result.get('basicPropertyData', {}).get('reviewScore', {}).get('reviewCount')
                hotel_item['distance_from_center'] = result.get('location', {}).get("mainDistance")
                hotel_item['min_price'] = result.get('priceDisplayInfoIrene', {}).get('displayPrice', {}).get(
                    'amountPerStay', {}).get('amountUnformatted')
                hotel_item['currency'] = result.get('priceDisplayInfoIrene', {}).get('displayPrice', {}).get(
                    'amountPerStay', {}).get('currency')
                hotel_item['check_in_date'] = check_in
                hotel_item['check_out_date'] = check_out
                pagename = result.get('basicPropertyData', {}).get('pageName')
                hotel_item['url'] = "https://www.booking.com/hotel/cz/{}.{}.html?aid=397594&label=gog235jc-1BCAEoggI46AdIM1gDaDqIAQGYAQW4AQfIAQzYAQHoAQGIAgGoAgO4ArOak6oGwAIB0gIkY2M5MGNmZTYtNzM0Mi00OGY1LTlkZTgtYjA1ZTRiM2JkZGEx2AIF4AIB&sid=c0b14234663a36fc66ae8b417d55092c&all_sr_blocks=7726221_348186498_2_1_0;dest_id=-553173;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=52;highlighted_blocks=7726221_348186498_2_1_0;hpos=2;matching_block_id=7726221_348186498_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=7726221_348186498_2_1_0__9000;srepoch=1700172776;srpvid=d4b2952c16e7007d;type=total;ucfs=1&#hotelTmpl"\
                    .format(pagename, language)

                # Check if any numeric value in hotel_item is 0, and skip the iteration if true
                if any(isinstance(value, (int, float)) and value == 0 for value in hotel_item.values()):
                    continue

                # Yielding the item
                yield hotel_item
            except AttributeError as e:
                # Handle the AttributeError (e.g., print a message, log it, or handle it in another way)
                print(f"AttributeError: {e}")
                # Optionally, you can continue to the next iteration or take another action as needed
                continue

