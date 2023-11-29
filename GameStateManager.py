class GameStateManager:
    def __init__(self):
        self.start()
    
    def start(self):
        self.game_state = 0

    def play(self):
        self.game_state = 1

    def pause(self):
        self.game_state = 2

    def player_death(self):
        self.game_state = 3

    def quit(self):
        self.game_state = 4

    def get_state(self):
        return self.game_state