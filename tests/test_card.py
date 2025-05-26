import pytest

from game.card import Card


@pytest.fixture
def my_card():
    return Card()

def test_create_card(my_card):
    assert len(my_card.card) == 3
    for row in my_card.card:
        assert len(row) == 9
        assert row.count(" ") == 4

def test_create_winner_card(my_card):
    for i in range(3):
        for j in range(9):
            if isinstance(my_card.card[i][j], int):
                assert my_card.winner_card[i][j] == "-"
            else:
                assert my_card.winner_card[i][j] == " "

def test_delete_number(my_card):
    test_number = 91
    my_card.card[0][0] = test_number
    assert my_card.delete_number(test_number) is True
    assert my_card.card[0][0] == "-"