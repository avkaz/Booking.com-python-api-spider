from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


class Hotel(DeclarativeBase):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    stars = Column(Float)
    rating = Column(Float)
    review_count = Column(Integer)
    distance_from_center = Column(Float)
    url = Column(String)

    price_items = relationship('PriceItem', back_populates='hotel')


class Dates(DeclarativeBase):
    __tablename__ = 'dates'

    date_code = Column(Integer, primary_key=True)
    snapshot_date = Column(Date)
    check_in_date = Column(Date)
    check_out_date = Column(Date)

    price_items = relationship('PriceItem', back_populates='dates')


class PriceItem(DeclarativeBase):
    __tablename__ = 'prices'

    hotel_id = Column(Integer, ForeignKey('hotels.id'), primary_key=True)
    date_code = Column(Integer, ForeignKey('dates.date_code'), primary_key=True)
    min_price = Column(Float)
    currency = Column(String)

    hotel = relationship('Hotel', back_populates='price_items')
    dates = relationship('Dates', back_populates='price_items')


