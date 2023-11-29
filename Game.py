import pygame, sys
from Definitions import *
from Player import *
from Enemy import *
from Coin import *
from CollisionManager import *
from ScoreManager import *
from GameStateManager import *

#inicializar Pygame
pygame.init()

#configurar la pantalla
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Juego de Tomás Mugetti")

def init_game(player, enemy_manager, coin_manager, score_manager, collision_manager):
    player = Player((screen_width/2, screen_height/2))
    enemy_manager = EnemyManager()
    coin_manager = CoinManager()
    score_manager = ScoreManager()
    collision_manager = CollisionManager(player, enemy_manager.get_enemies(), coin_manager.get_coins(), score_manager)

def main():
    clock = pygame.time.Clock()
    game_state_manager = GameStateManager()

    player = Player((screen_width/2, screen_height/2))
    enemy_manager = EnemyManager()
    coin_manager = CoinManager()
    score_manager = ScoreManager()
    collision_manager = CollisionManager(player, enemy_manager.get_enemies(), coin_manager.get_coins(), score_manager, game_state_manager)
    

    exit = False
    while not exit:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(background_color)

        #input
        keys = pygame.key.get_pressed()
        
        match game_state_manager.get_state():
            case 0:
                font = pygame.font.SysFont(fuente, texto_chico)
                text = "presiona ESPACIO para comenzar"
                start_text_surface = font.render(text,False,(255,255,255))
                text_rect = start_text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(start_text_surface, text_rect)

                exit_text = "presiona ESCAPE para salir"
                exit_text_surface = font.render(exit_text, False, (255,255,255))
                exit_text_rect = exit_text_surface.get_rect(center=(screen_width/2, screen_height/2 + text_rect.height))
                screen.blit(exit_text_surface, exit_text_rect)

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_state_manager.play()
                        elif event.key == pygame.K_ESCAPE:
                            game_state_manager.quit()

            case 1:
                if keys[pygame.K_ESCAPE]:
                    game_state_manager.pause()
                
                #update
                player.move(keys)
                enemy_manager.spawn()
                enemy_manager.move()
                coin_manager.spawn()
                coin_manager.move()
                collision_manager.check_collisions()

                #dibujar
                player.draw(screen)
                enemy_manager.draw(screen)
                coin_manager.draw(screen)
                score_manager.draw(screen)

            case 2:
                font = pygame.font.SysFont(fuente, texto_chico)
                continue_text = "presiona ESPACIO para continuar"
                continue_text_surface = font.render(continue_text, False, WHITE)
                text_rect = continue_text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(continue_text_surface, text_rect)

                exit_text = "presiona ESCAPE para salir"
                exit_text_surface = font.render(exit_text, False, WHITE)
                exit_text_rect = exit_text_surface.get_rect(center=(screen_width/2, screen_height/2 + text_rect.height))
                screen.blit(exit_text_surface, exit_text_rect)
                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            game_state_manager.play()
                        elif event.key == pygame.K_ESCAPE:
                            game_state_manager.quit
            case 3:
                font = pygame.font.SysFont(fuente, texto_grande)
                score_text = "Score: " + str(score_manager.get_score())
                score_text_surface = font.render(score_text, False, WHITE)
                text_rect = score_text_surface.get_rect(center=(screen_width/2, 50))
                screen.blit(score_text_surface, text_rect)

                font = pygame.font.SysFont(fuente, texto_chico)
                restart_text = "presiona ESPACIO para jugar denuevo"
                restart_text_surface = font.render(restart_text, False, WHITE)
                text_rect = restart_text_surface.get_rect(center=(screen_width/2, screen_height/2))
                screen.blit(restart_text_surface, text_rect)

                exit_text = "presiona ESCAPE para salir"
                exit_text_surface = font.render(exit_text, False, WHITE)
                text_rect = exit_text_surface.get_rect(center=(screen_width/2, screen_height/2 + text_rect.height))
                screen.blit(exit_text_surface, text_rect)

                for event in events:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            player = Player((screen_width/2, screen_height/2))
                            enemy_manager = EnemyManager()
                            coin_manager = CoinManager()
                            score_manager = ScoreManager()
                            collision_manager = CollisionManager(player, enemy_manager.get_enemies(), coin_manager.get_coins(), score_manager, game_state_manager)

                            game_state_manager.play()
                        elif event.key == pygame.K_ESCAPE:
                            game_state_manager.quit()
            case 4:
                exit = True

        #actualizar la pantalla
        pygame.display.flip()

        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
