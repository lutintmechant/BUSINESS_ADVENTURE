import pygame
from Gem import Gem


#creer une classe pr gérer cet évenemnt
class GemFallEvent:

    #lors du chargement -> creer un compteur
    def __init__(self,game):
        self.percent = 0
        self.percent_speed = 10
        self.game = game
        self.fall_mode2 = False

        #definir un groupe de sprite pour stocker nos comètes
        self.all_gems = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0
    def gem_fall(self):
        #boucle pour les valeurs 1
        for i in range(1,10):
           #apparaitre une premiére boule de feu
           self.all_gems.add(Gem(self))

    def attempt_fall(self):
        #la jauge est totalement chargé
        if self.is_full_loaded() and len(self.game.all_monsters):

            self.gem_fall()
            self.fall_mode2 = True # activer l'évenement


    def update_bar(self,surface):
        #ajouter du pourcentage à la bar
        self.add_percent()



