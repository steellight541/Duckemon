from Vectors import Vector2D
from pygame import image

class Player:
    def __init__(self) -> None:
        self.pos = Vector2D(0, 0)
        self.image = image.load("player.png")

    def move(self, x, y):
        self.pos.x += x
        self.pos.y += y

p = Player()
p.move(10, 10)
print(p.pos)  # @[10, 10]