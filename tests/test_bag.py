import pytest

from game.bag import Bag


@pytest.fixture
def current_bag():
    return Bag()

def test_bag(current_bag):
    assert len(current_bag) == 90
    number = current_bag.get_number_from_bag()
    assert number not in current_bag._bag
    assert len(current_bag) == 89
