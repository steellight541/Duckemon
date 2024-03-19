from Window import Window
from Player import Player

window = Window(800, 600, "Game")
player = Player()

running = True
while running:
    window.clear()
    window.draw_image("player.png")
    window.update()
    for event in window.events.get_events():
        if event.type == window.events.QUIT_event():
            running = False

window.close_window()

