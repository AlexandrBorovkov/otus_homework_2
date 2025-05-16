from random import sample


class Card:
    def __init__(self):
        self.card = self._create_card()
        self.winner_card = self._create_winner_card()

    def _create_card(self):
        numbers = sample(range(1, 91), 27)
        matrix = [sorted(numbers[i*9:(i+1)*9]) for i in range(3)]
        for row in matrix:
            indexes = sample(range(9), 4)
            for index in indexes:
                row[index] = " "
        return matrix

    def _create_winner_card(self):
        return [
            ["-" if isinstance(char, int) else char
            for char in row]
            for row in self.card
        ]

    def delete_number(self, number):
        for row in self.card:
            if number in row:
                index = row.index(number)
                row[index] = "-"
                return True
        return False

    def __str__(self):
        return "\n".join(
            " ".join(str(char).rjust(2) for char in line)
            for line in self.card
        )
