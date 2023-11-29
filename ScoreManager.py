import pygame
from Definitions import *

class ScoreManager:
    def __init__(self):
        pygame.font.init()
        self.score = 0
        self.font = pygame.font.SysFont('Times New Roman', 30)

    def add_score(self):
        self.score += coin_value

    def draw(self, screen):
        text = 'Score: ' + str(self.score)
        text_surface = self.font.render(text, False, (0, 0, 0))
        screen.blit(text_surface, (0,0))
    
    def get_score(self):
        return self.score