from Events import Events
from pygame import display, draw, font, image, quit, init

class Window:
    def __init__(self, width, height, title):
        init()
        self.events = Events()
        self.title = title
        self.width = width
        self.height = height
        self.create_window()
        self.update_title()
        
    def create_window(self):
        self.screen = display.set_mode((self.width, self.height))

    def set_screen_size(self, width, height):
        self.width = width
        self.height = height
        self.create_window()
        
    def update_title(self):
        display.set_caption(self.title)
    
    def set_background(self, color):
        self.screen.fill(color)
        
    def update(self):
        display.update()
        
    def close_window(self):
        quit()

    def clear(self):
        self.screen.fill((255, 255, 255))
    
    def draw_rect(self, color, rect):
        return draw.rect(self.screen, color, rect)
        
    def draw_circle(self, color, pos, radius):
        return draw.circle(self.screen, color, pos, radius)
        
    def draw_line(self, color, start_pos, end_pos, width):
        return draw.line(self.screen, color, start_pos, end_pos, width)
        
    def draw_text(self, text: str, color: tuple, dest, font_size: int):
        _font = font.Font(None, font_size)
        text = _font.render(text, True, color)
        self.screen.blit(text, dest)
        
    def load_image(self, path: str):
        return image.load(path)
    
    def draw_image(self, path):
        self.screen.blit(self.load_image(path), (0, 0))


