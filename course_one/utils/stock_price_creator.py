"""create fake stock price data"""
from string import ascii_lowercase
import csv
from numpy.random import default_rng

rng = default_rng(seed=505)
def ticker_maker() -> tuple[str, int, float]:
    """creates random records of stock ticker, volume, price"""
    ticker:str =''.join(rng.choice(list(ascii_lowercase.upper()),replace=True,size=(3,)))
    volume:int = rng.integers(1, 10)
    price:float = rng.uniform(low=0.25,high=125.0)
    return (ticker, volume, price)

with open('stock_price.csv','w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for i in range(5):
        writer.writerow(ticker_maker())
