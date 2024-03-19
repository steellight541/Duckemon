class Vector2D:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def to_tuple(self):
        return (self.x, self.y)

    def to_list(self):
        return [self.x, self.y]

    def to_dict(self):
        return {"x": self.x, "y": self.y}

    def to_set(self):
        return {self.x, self.y}

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)

    def __floordiv__(self, other):
        return Vector2D(self.x // other.x, self.y // other.y)

    def __mod__(self, other):
        return Vector2D(self.x % other.x, self.y % other.y)

    def __pow__(self, other):
        return Vector2D(self.x**other.x, self.y**other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __le__(self, other):
        return self.x <= other.x and self.y <= other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __ge__(self, other):
        return self.x >= other.x and self.y >= other.y

    def __str__(self) -> str:
        return f"@[{self.x}, {self.y}]"

