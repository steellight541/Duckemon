import pygame
from pygame.locals import *

class Game:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.is_running = False

    def start(self):
        self.is_running = True
        self.on_start()

        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)  # Limit the frame rate to 60 FPS

        self.on_exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                self.on_key_down(event.key)
            elif event.type == KEYUP:
                self.on_key_up(event.key)
            elif event.type == MOUSEBUTTONDOWN:
                self.on_mouse_down(event.button, event.pos)
            elif event.type == MOUSEBUTTONUP:
                self.on_mouse_up(event.button, event.pos)
            elif event.type == MOUSEMOTION:
                self.on_mouse_motion(event.buttons, event.pos, event.rel)

    def update(self):
        pass

    def render(self):
        self.window.fill((255, 255, 255))  # Fill the window with white color
        pygame.display.update()

    def on_start(self):
        pass

    def on_exit(self):
        pygame.quit()

    def on_key_down(self, key):
        pass

    def on_key_up(self, key):
        pass

    def on_mouse_down(self, button, pos):
        pass

    def on_mouse_up(self, button, pos):
        pass

    def on_mouse_motion(self, buttons, pos, rel):
        pass

# Example usage:
class MyGame(Game):
    def on_start(self):
        print("Game started")

    def update(self):
        # Game logic and state updates
        pass

    def render(self):
        # Render game graphics
        super().render()

    def on_exit(self):
        print("Game exited")

game = MyGame(800, 600)
game.start()