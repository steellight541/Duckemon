from Window import Window
from Player import Player


class Game:
    def __init__(self):
        self.window = Window(800, 600, "Game")
        self.player = Player()

    def update(self):
        self.window.clear()
        self.window.draw_image(self.player.image, self.player.pos.to_tuple())
        self.window.update()

    def run(self):
        while True:
            self.update()
            for events in self.window.events.get():
                if self.window.events.isQuit(events):
                    self.window.close_window()
                    quit()


G = Game()
G.run()
