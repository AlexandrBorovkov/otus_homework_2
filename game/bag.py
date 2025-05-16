from random import choice


class Bag:
    def __init__(self):
        self._bag = list(range(1, 91))

    def get_number_from_bag(self):
        number = choice(self._bag)
        self._bag.remove(number)
        return number

    def __len__(self):
        return len(self._bag)
