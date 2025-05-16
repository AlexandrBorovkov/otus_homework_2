from prompt_toolkit import prompt
from prompt_toolkit.validation import Validator

from game.bag import Bag
from game.card import Card


def start_game():
    print("Старт игры!!!)))")
    my_card = Card()
    computer_card = Card()
    current_bag = Bag()
    for _ in range(90):
        number = current_bag.get_number_from_bag()
        output_string = (
            f"\nНовый бочонок: {number} (осталось {len(current_bag)})\n"
            f"------ Ваша карточка -----\n"
            f"{my_card}\n"
            f"--------------------------\n"
            f"-- Карточка компьютера ---\n"
            f"{computer_card}\n"
            f"--------------------------"
        )
        print(output_string)
        answer = prompt(
            "Зачеркнуть цифру? y/n: ",
            validator=Validator.from_callable(
                lambda x: x in ['y', 'n']
            )
        )
        computer_card.delete_number(number)
        match answer:
            case "y":
                if my_card.delete_number(number):
                    if (computer_card.winner_card == computer_card.card
                            and my_card.winner_card == my_card.card):
                        print("Ничья!")
                        break
                    elif computer_card.winner_card == computer_card.card:
                        print("Вы проиграли!")
                        break
                    elif my_card.winner_card == my_card.card:
                        print("Вы выиграли!")
                        break
                else:
                    print("Такой цифры на карточке нет! Вы проиграли!")
                    break
            case "n":
                if my_card.delete_number(number):
                    print("Эту цифру нужно было зачеркнуть! Вы проиграли!")
                    break
                if computer_card.winner_card == computer_card.card:
                    print("Вы проиграли!")
                    break
