import pygame
import math
from game import Game

def lance():
    
    pygame.init()

    # definir une clock
    clock = pygame.time.Clock()
    FPS = 60
    # génerer la fenetre de notre jeu
    pygame.display.set_caption("Businness adventure")
    screen = pygame.display.set_mode((1080, 720))

    # importer l'arriere plan de notre jeu
    background = pygame.image.load('assets/assets/imagees.jpg')
    background = pygame.transform.smoothscale(background,(1080, 720))

    # importer charger notre banniére
    banner = pygame.image.load('assets/assets/banner.png')
    banner = pygame.transform.scale(banner, (500, 500))
    banner_rect = banner.get_rect()
    banner_rect.x = math.ceil(screen.get_width() / 4)

    # import charger notre bouton pour lancer la partie
    play_button = pygame.image.load("assets/assets/button.png")
    play_button = pygame.transform.scale(play_button, (400, 150))
    play_button_rect = play_button.get_rect()
    play_button_rect.x = math.ceil(screen.get_width() / 3.33)
    play_button_rect.y = math.ceil(screen.get_height() / 2)

    # charger notre jeu
    game = Game()

    running = True

    # boucle tant cette condition est vraie
    while running:

        # appliquer l'arriere plan de notre jeu
        screen.blit(background, (0, 0))

        # verifier si notre jeu a commencé ou non
        if game.is_playing:
            # declencher les instructions de la partie
            game.update(screen)

            # verifier si notre jeu n'a pas commencé
        else:
            # ajouter mon écran de bienvenue
            screen.blit(play_button, play_button_rect)
            screen.blit(banner, banner_rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                   # verification pour savoir si la souris est en collision avec le bouton jouer 
                    if play_button_rect.collidepoint(event.pos):
                   # mettre le jeu en mode 'lancé'
                      game.start()
                elif event.type == pygame.QUIT:
                    running = False
                    pygame.quit()



        # mettre  à jour l'écran
        pygame.display.flip()

        # si le joueur ferme cette fenetre
        for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # detecter si un joueur lache une touche du clavier
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

            # detecter si la touche espace est enclenchée pour lancer notre projectile
                if event.key == pygame.K_SPACE:
                    game.player.launch_projectile()

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            
        #fixer le nombre de fps sur ma clock
        clock.tick(FPS)        