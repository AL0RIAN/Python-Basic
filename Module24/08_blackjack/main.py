from random import randint


class Card:
    def __init__(self, index):
        self.index = index

    ace = 11
    king, lady, jack = 10, 10, 10
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, king, lady, jack, ace]

    def take_random_card(self):
        return self.cards[randint(0, len(self.cards) - 1)]


if __name__ == "__main__":
    victory = False
    global_deck = [Card(number).take_random_card() for number in range(52)]
    computer_deck = [card for card in global_deck[0:2]]
    global_deck.pop(0)
    global_deck.pop(1)
    print('Крупье получил две карты\n')

    player_deck = [card for card in global_deck[0:2]]
    global_deck.pop(0)
    global_deck.pop(1)
    while (sum(computer_deck) < 21) or (sum(player_deck) < 21):
        print(f'Ваши карты: {player_deck}. Их сумма: {sum(player_deck)}')
        print('Взять ещё карту или остановиться - 1/0: ', end='')
        choice = int(input())
        if choice == 1:
            player_deck.append(global_deck[0])
            if sum(player_deck) >= 21:
                break
            global_deck.pop(0)
            computer_deck.append(global_deck[1])
            global_deck.pop(1)
            if sum(computer_deck) >= 21:
                break
        else:
            break
    if sum(player_deck) > 21:
        print(f'Поражение игрока! Игрок: {sum(player_deck)}. Крупье: {sum(computer_deck)}')
    elif sum(computer_deck) > sum(player_deck):
        print(f'Поражение игрока! Игрок: {sum(player_deck)}. Крупье: {sum(computer_deck)}')
    else:
        print(f'Победа игрока! Игрок: {sum(player_deck)}. Крупье: {sum(computer_deck)}')
