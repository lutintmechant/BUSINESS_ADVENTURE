import pygame
import random

class Gem(pygame.sprite.Sprite):

    def __init__(self,gem_event):
        super().__init__()
        self.image = pygame.image.load('assets/assets/gem-lebon.png')
        self.image = pygame.transform.smoothscale(self.image,(50,70))
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.gem_event = gem_event

    def remove(self):
        self.gem_event.all_gems.remove(self)

        # verifier si le nombre de comètes est de 0
        if len(self.gem_event.all_gems) == 0:
            # remettre la bar à 0
            self.gem_event.reset_percent()
            # appaitre les 2 premiers monstres
            self.gem_event.game.spawn_monster()
            self.gem_event.game.spawn_monster()
            self.gem_event.game.spawn_monster()

    def fall(self):
        self.rect.y += self.velocity

        # si elle ne tombe pas sur le sol
        if self.rect.y >= 500:
            # retirer la boule de feu
            self.remove()
            # si il n'y a plus de boules de feu
            if len(self.gem_event.all_gems) == 0:
                print("L'évenement est fini")

                # remettre la jauge de vie au depart
                self.gem_event.reset_percent()
                self.gem_event.fall_mode2 = False
            # verifier si la boule de feu touche le joueur
            if self.gem_event.game.check_collision(
                    self, self.gem_event.game.all_players
            ):
                print("joueur touché !")
                # retirer la boule de feu
                self.remove()
                # subir 20 points de dégats
                self.gem_event.game.player.kit(10)