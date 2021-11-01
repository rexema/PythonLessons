import random

class LotoCard:
    def __init__(self, player_type):
        self.player_type = player_type
        self._card = [
            [],
            [],
            []
        ]
        self._MAX_NUMBER = 90
        self._MAX_NUMBER_IN_CARD = 15
        self._number_stroked = 0
        NEED_SPACES = 4
        NEED_NUMBERS = 5
        self.rand_num = random.randint(1, self._MAX_NUMBER)

        self._number = random.sample(range(1, self._MAX_NUMBER + 1), self._MAX_NUMBER_IN_CARD)

        for line in self._card:
            for _ in range(NEED_SPACES):
                line.append(" ")
            for _ in range(NEED_NUMBERS):
                line.append(self._number.pop())

        def check_sort_item(item):
            if isinstance(item, int):
                return item
            return random.randint(1, self._MAX_NUMBER)

        for index, line in enumerate(self._card):
            self._card[index] = sorted(line, key=check_sort_item)

    def __str__(self):
        return self.player_type + '\n' + f'-' * 22 + '\n' + '\n'.join([' '.join(map(str, line)) for line in self._card])


human = LotoCard("Игрок")
comp = LotoCard("Компьютер")

class LotoGame:
    def __init__(self, human_player, comp_player):

        self.human_player = human_player
        self.comp_player = comp_player
        self.number_pool = list(range(1, 91))

    print(f'Игра началась!')

    def display_cards(self):
        print(human)
        print(comp)

    def lotto_choice(self):
        choice = random.choice(self.number_pool)
        self.number_pool.remove(choice)
        return choice

    def the_game(self):

        while self.human_player._MAX_NUMBER_IN_CARD != 0 and self.comp_player._MAX_NUMBER_IN_CARD != 0:
            choice = game.lotto_choice()
            print(f"На бочонке выпало число {choice}")
            game.display_cards()
            cross_number = input("Вы хотите зачеркнуть число? ")

            if cross_number == 'y':
                for line in self.human_player._card:
                    for index, item in enumerate(line):
                        if choice == item:
                            line[index] = '-'
                            self.human_player._MAX_NUMBER_IN_CARD -= 1
                for line in self.comp_player._card:
                    for index, item in enumerate(line):
                        if choice == item:
                            line[index] = '-'
                            self.comp_player._MAX_NUMBER_IN_CARD -= 1
            elif cross_number == 'n':
                for line in self.comp_player._card:
                    for index, item in enumerate(line):
                        if choice == item:
                            line[index] = '-'
                            self.comp_player._MAX_NUMBER_IN_CARD -= 1
                for line in self.human_player._card:
                    for index, item in enumerate(line):
                        if choice == item:
                            print("Вы ошиблись!")
                            raise ValueError
            else:
                print("Вы ошиблись!")
                raise ValueError
        else:
            if self.human_player._MAX_NUMBER_IN_CARD == 0 and self.comp_player._MAX_NUMBER_IN_CARD == 0:
                print("Ничья")
            elif self.human_player._MAX_NUMBER_IN_CARD == 0:
                print("Вы выиграли!")
            elif self.comp_player._MAX_NUMBER_IN_CARD == 0:
                print("Компьютер выиграл!")

game = LotoGame(human, comp)
game.the_game()
