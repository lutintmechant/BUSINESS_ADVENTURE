import pygame
from comet import Comet
#creer une classe pr gérer cet évenemnt
class CometFallEvent:

    #lors du chargement -> creer un compteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode = False

        #definir un groupe de sprite pour stocker nos comètes
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0
    def meteor_fall(self):
        #boucle pour les valeurs entre 1 et 10
        for i in range(1,10):
           #apparaitre une premiére boule de feu
           self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge est totalement chargé
        if self.is_full_loaded()and len(self.game.all_monsters
        ):

            self.meteor_fall()
            self.fall_mode = True # activer l'évenement


    def update_bar(self,surface):
        #ajouter du pourcentage à la bar
        self.add_percent()



        #bar noir(en arrière plan)
        pygame.draw.rect(surface,(0,0,0),[
            0,#axe des x
            surface.get_height()-30,#l'axe des y
            surface.get_width(),#longueur de la fenetre
            10#épaisseur de la bar
        ])
        #barre rouge (jauge de l'event)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # axe des x
            surface.get_height()-30,  # l'axe des y
            (surface.get_width() / 100) * self.percent,  # longueur de la fenetre
            10  # épaisseur de la bar
        ])