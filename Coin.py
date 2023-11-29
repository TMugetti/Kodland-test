import pygame, random, time
from Definitions import *

class Coin:
    def __init__(self):
        self.position = (-10, -10)
        self.is_active = False
        self.speed = 0

    def spawn(self, position):
        self.position = position
        self.speed = coin_speed
        self.is_active = True

    def die(self):
        self.position = (-10, -10)
        self.is_active = False
        self.speed = 0

    def draw(self, screen):
        if self.is_active:
            pygame.draw.circle(screen, coin_color, (self.position), coin_radius)

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

class CoinManager():
    def __init__(self):
        self.last_spawn = 0
        self.coins = []
        for i in range(10):
            self.coins.append(Coin())

    def spawn(self):
        if time.time() - self.last_spawn > coin_spawn_cooldown:
            y = 0
            x = random.randrange(0 + coin_radius, screen_width - coin_radius)
            coin = self.coins.pop(0)
            coin.spawn((x,y))
            self.coins.append(coin)
            self.last_spawn = time.time()

    def move(self):
        for coin in self.coins:
            coin.move()
    
    def draw(self, screen):
        for coin in self.coins:
            coin.draw(screen)

    def get_coins(self):
        return self.coins