import pygame
import random

#creer une class pour gérer cette comète
class Comet(pygame.sprite.Sprite):

    def __init__(self,comet_event):
        super().__init__()
        #definir l'image associé de cette comète
        self.image = pygame.image.load('assets/assets/taxes_lebon.png')
        self.image = pygame.transform.smoothscale(self.image,(70,70))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(20,800)
        self.rect.y = - random.randint(0,800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        #verifier si le nombre de comètes est de 0
        if len(self.comet_event.all_comets)==0:
            #remettre la bar à 0
            self.comet_event.reset_percent()
            #appaitre les 3 premiers monstres
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()
            self.comet_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        #si elle ne tombe pas sur le sol
        if self.rect.y >= 500:
            #retirer la boule de feu
            self.remove()
            #si il n'y a plus de boules de feu
            if len(self.comet_event.all_comets) == 0:
                print("L'évenement est fini")

                #remettre la jauge de vie au depart
                self.comet_event.reset_percent()
                self.comet_event.fall_mode= False
            #verifier si la boule de feu touche le joueur
            if self.comet_event.game.check_collision(
                    self,self.comet_event.game.all_players
            ):
                print("joueur touché !")
                #retirer la boule de feu
                self.remove()
                #subir 20 points de dégats
                self.comet_event.game.player.damage(20)