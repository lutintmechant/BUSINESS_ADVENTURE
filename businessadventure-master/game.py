import pygame
from player import Player
from monster import Monster
from gem_event import GemFallEvent
from comet_event import CometFallEvent

#creer une seconde classe qui va representer notre jeu
class Game:

    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing =False
        #generer notre joueur
        self.all_players=pygame.sprite.Group()
        self.player= Player(self)
        self.all_players.add(self.player)
        #generer l'évenement
        self.gem_event = GemFallEvent(self)
        self.comet_event = CometFallEvent(self)
        #groupe de monstre
        self.all_monsters=pygame.sprite.Group()
        #mettre le score à 0
        self.score = 0
        self.pressed={}


    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()
        
    def add_score(self,points):
        self.score+= points


    def game_over(self):
        #remettre le jeu au début,retirer les monstres,remettre le joueur à 100 de pv,jeu en attente
        self.all_monsters=pygame.sprite.Group()
        self.gem_event.all_gems = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health=self.player.max_health
        self.gem_event.reset_percent()
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        
    def update(self,screen):
        #afficher le score sur l'écran
        font = pygame.font.SysFont("monospace", 16)
        score_text = font.render(f"Score : {self.score}",1,(0,0,0))
        screen.blit(score_text, (20, 20))
        
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser la bar d'evenement du jeu
        self.gem_event.update_bar(screen)
        self.comet_event.update_bar(screen)

        # recuperer les projectiles de joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)

        #recuperer les comètes de notre jeu
        for gem in self.gem_event.all_gems:
            gem.fall()
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des images de mon groupe de comète
        self.gem_event.all_gems.draw(screen)
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur souhaite allez à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self):
        monster=Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)