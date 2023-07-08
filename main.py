import pygame
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
        
class Home:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
        

class Game:
    def __init__(self, width, height, fps=60):
        pygame.init()
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.fps = fps
        self.delta_time = 0.0
        self.player = Player(self.width // 2, self.height // 2)
        self.home = Home(0,0, 30, 30)
        
        
    def render_rect(self, rect):
        pygame.draw.rect(self.window, (255, 0, 0), rect)
       

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                rect_obj = pygame.Rect(rect)
                if rect_obj.collidepoint(mouse_pos):
                    print("Hello, world!")

                    
    def start(self):
        self.is_running = True
        self.on_start()

        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(self.fps)
            self.delta_time = self.clock.get_time() / 1000.0  # Convert to seconds

        self.on_exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.is_running = False
            elif event.type == KEYDOWN:
                self.on_key_down(event.key)
            elif event.type == KEYUP:
                self.on_key_up(event.key)

    def update(self):
        # Update player position based on user input or game logic
        dx = 0
        dy = 0

        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            dx = -5 
        elif keys[K_RIGHT]:
            dx = 5
        if keys[K_UP]:
            dy = -5
        elif keys[K_DOWN]:
            dy = 5 

        self.player.move(dx, dy)

    def render(self):
        # Calculate the camera position for tracking shot
        camera_x = self.player.x - self.width // 2
        camera_y = self.player.y - self.height // 2

        self.window.fill((255, 255, 255))  # Fill the window with white color
        self.render_rect( (10,10,20,20))
        # Render the player at the adjusted position
        player_rect = pygame.Rect(self.player.x - camera_x, self.player.y - camera_y, 20, 20)
        pygame.draw.rect(self.window, (255, 0, 0), player_rect)
        
        # Other entities or objects in the scene can also be rendered using the same camera position
        # Example:
        # entity_rect = pygame.Rect(entity.x - camera_x, entity.y - camera_y, entity.width, entity.height)
        # pygame.draw.rect(self.window, (0, 0, 255), entity_rect)
        entity_rect = pygame.Rect(self.home.x - camera_x, self.home.y - camera_y, self.home.w, self.home.h)
        pygame.draw.rect(self.window, (0, 0, 255), entity_rect)

        pygame.display.update()

    def on_start(self):
        pass

    def on_exit(self):
        pygame.quit()

    def on_key_down(self, key):
        pass

    def on_key_up(self, key):
        pass

# Example usage:
game = Game(800, 600)
game.start()