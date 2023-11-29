import pygame
from Definitions import *

class Player:
    def __init__(self, position):
        self.position = position

    def move(self, keys):
        x = self.position[0]
        y = self.position[1]
        x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * player_speed
        y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * player_speed

        # Limite del jugador para que no salga de la pantalla
        x = max(player_radius, min(x, screen_width - player_radius))
        y = max(player_radius, min(y, screen_height - player_radius))

        self.position = (x,y)

    def get_position(self):
        return self.position
    
    def draw(self, screen):
        pygame.draw.circle(screen, player_color, (self.position), player_radius)