import os

class LegendOfZeldaLostWoods:
    COLUMNS = 20
    STEP = COLUMNS // 5
    player_position = COLUMNS // 2

    def move_player(self, move: int):
        self.player_position = self.player_position + move
        if self.player_position >= self.COLUMNS:
            self.player_position = self.player_position % self.COLUMNS

    def player_won(self):
        return self.player_position < 0

    def drive(self):
        while not self.player_won():
            try:
                self.draw_decision_menu()

                answer = input()[0].lower()

                match answer:
                    case 'l':
                        self.move_left()
                    case 'r':
                        self.move_right()
            except:
                continue

        self.draw_game_won_menu()

    def move_left(self):
        self.move_player(-self.STEP)

    def move_right(self):
        self.move_player(self.STEP)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_welcome_text(self):
        print('You are lost in the Lost Forest.')

    def draw_decision_text(self):
        print('Go left or right?')

    def draw_woods(self):
        print('*' * self.COLUMNS)

    def draw_player(self):
        print(' ' * (self.player_position - 1) + ':)')

    def draw_won_message(self):
        print('You finally got out of there!')

    def draw_decision_menu(self):
        self.clear()
        self.draw_welcome_text()
        self.draw_woods()
        self.draw_player()
        self.draw_woods()
        self.draw_decision_text()

    def draw_game_won_menu(self):
        self.clear()
        self.draw_welcome_text()
        self.draw_woods()
        self.draw_won_message()
        self.draw_woods()

if __name__ == '__main__':
    woods = LegendOfZeldaLostWoods()
    woods.drive()
