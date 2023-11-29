import pygame, random, time
from Definitions import *

class Enemy:
    def __init__(self):
        self.position = (-10, -10)
        self.is_active = False
        self.speed = 0

    def spawn(self, position):
        self.position = position
        self.speed = random.randint(enemy_speed_range[0], enemy_speed_range[1])
        self.is_active = True
    
    def die(self):
        self.position = (-10, -10)
        self.is_active = False
        self.speed = 0
    
    def draw(self, screen):
        if self.is_active:
            pygame.draw.rect(screen, enemy_color, (self.position[0], self.position[1], enemy_height, enemy_width))

    def move(self):
        if self.is_active:
            x = self.position[0]
            y = self.position[1]
            y += self.speed

            self.position = (x,y)

            if self.position[1] >= screen_height:
                self.die()
    
    def get_active(self):
        return self.is_active
    
    def get_position(self):
        return self.position

class EnemyManager:
    def __init__(self):
        self.last_spawn = 0
        self.enemies = []
        for i in range(50):
            self.enemies.append(Enemy())

    def spawn(self):
        if time.time() - self.last_spawn > enemy_spawn_cooldown:
            y = 0
            x = random.randrange(0, (screen_width - enemy_width))
            enemy = self.enemies.pop(0)
            enemy.spawn((x,y))
            self.enemies.append(enemy)
            self.last_spawn = time.time()

    def move(self):
        for enemy in self.enemies:
            enemy.move()
    
    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)

    def get_enemies(self):
        return self.enemies