import pygame
from Definitions import *
from Coin import *
from Enemy import *
from Player import *

class CollisionManager:
    def __init__(self, player, enemies, coins, score_manager, game_state_manager):
        self.player = player
        self.enemies = enemies
        self.coins = coins
        self.score_manager = score_manager
        self.game_state_manager = game_state_manager

    def check_collisions(self):
        player_x, player_y = self.player.get_position()
        player_rect = pygame.rect.Rect(player_x - player_radius, player_y - player_radius, player_radius * 2, player_radius * 2)
        
        #collision con enemigos
        for enemy in self.enemies:
            if enemy.get_active():
                enemy_x, enemy_y = enemy.get_position()
                enemy_rect = pygame.rect.Rect(enemy_x, enemy_y, enemy_width, enemy_height)
                if player_rect.colliderect(enemy_rect):
                    self.game_state_manager.player_death()

        #colision con monedas
        for coin in self.coins:
            if coin.get_active():
                coin_x, coin_y = coin.get_position()
                coin_rect = pygame.rect.Rect(coin_x - coin_radius, coin_y - coin_radius, coin_radius * 2, coin_radius * 2)
                if player_rect.colliderect(coin_rect):
                    coin.die()
                    self.score_manager.add_score()
