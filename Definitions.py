from enum import Enum

#screen
screen_width = 500
screen_height = 800
background_color = (102,155,155)

#player
player_color = (0,255,0)
player_radius = 20
player_speed = 5

#bullet
bullet_color = (255, 255, 0)
bullet_radius = 5
bullet_speed = 10
shooting_cooldown = 1

#enemy
enemy_color = (255,0,0)
enemy_width = 50
enemy_height = 50
enemy_speed_range = (3, 10)
enemy_spawn_cooldown = 0.5

#coin
coin_color = (255, 215, 0)
coin_radius = 15
coin_speed = 3
coin_spawn_cooldown = 2
coin_value = 1

#text
WHITE = (255,255,255)
BLACK = (0, 0, 0)
fuente = "Times New Roman"
texto_grande = 50
texto_chico = 30