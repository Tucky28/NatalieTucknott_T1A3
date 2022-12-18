import pytest
from shop import shop

items = shop()

def store_items():
    del shop.store_items('1 - Squeezy Ball Toy', 2)
    assert len(store_items) == 2


