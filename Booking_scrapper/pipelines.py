from itemadapter import ItemAdapter
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import create_table, Hotel, PriceItem

class BookingScrapperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        # Dates -> convert to date
        date_keys = ['check_in_date', 'check_out_date']
        for date_key in date_keys:
            value = adapter.get(date_key, None)

            if value is not None:
                # Assuming that the date format is 'YYYY-MM-DD'
                # If it's a different format, adjust the strptime format accordingly
                date_value = datetime.strptime(value, '%Y-%m-%d').date()

                # Update the item with the datetime value
                adapter[date_key] = date_value

        # Distance from center -> to float
        distance_str = adapter.get('distance_from_center')
        if distance_str is not None:
            distance_float = float(distance_str.replace(',', '.').split(' ')[0])
            adapter['distance_from_center'] = distance_float

        # stars -> to int
        stars_key = adapter.get('stars')
        if stars_key is not None:
            stars = int(float(stars_key))
            adapter['stars'] = stars

        # rating -> to float
        rating_key = adapter.get('rating')
        if rating_key is not None:
            rating = float(rating_key)
            adapter['rating'] = rating

        # review_count -> to int
        review_count_key = adapter.get('review_count')
        if review_count_key is not None:
            review_count = int(review_count_key)
            adapter['review_count'] = review_count

        # min_price -> to float
        min_price_key = adapter.get('min_price')
        if min_price_key is not None:
            min_price = round(float(min_price_key), 2)
            adapter['min_price'] = min_price

        return item

class SaveHotelsToSQLite:
    def __init__(self):
        self.engine = create_engine('sqlite:///hotels.db')
        self.Session = sessionmaker(bind=self.engine)

    def open_spider(self, spider):
        create_table(self.engine)

    def process_item(self, item, spider):
        session = self.Session()

        # Check if hotel with the same information already exists
        existing_hotel = session.query(Hotel).filter_by(
            name=item['name'],
            stars=item['stars'],
            rating=item['rating'],
            review_count=item['review_count'],
            distance_from_center=item['distance_from_center'],
            url=item['url']
        ).first()

        if existing_hotel:
            hotel_id = existing_hotel.id
        else:
            # Create and add Hotel item
            hotel_item = Hotel(
                name=item['name'],
                stars=item['stars'],
                rating=item['rating'],
                review_count=item['review_count'],
                distance_from_center=item['distance_from_center'],
                url=item['url']
            )
            session.add(hotel_item)
            session.flush()  # flush to get the hotel_item.id
            hotel_id = hotel_item.id

        # Check if price with the same value, date, and hotel ID already exists
        existing_price = session.query(PriceItem).filter_by(
            hotel_id=hotel_id,
            check_in_date=item['check_in_date'],
            check_out_date=item['check_out_date'],
            min_price=item['min_price'],
            currency=item['currency']
        ).first()

        if not existing_price:
            # Create and add FactItem
            price_item = PriceItem(
                hotel_id=hotel_id,
                check_in_date=item['check_in_date'],
                check_out_date=item['check_out_date'],
                min_price=item['min_price'],
                currency=item['currency']
            )
            session.add(price_item)

        try:
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

        return item

    def close_spider(self, spider):
        self.Session.close()
