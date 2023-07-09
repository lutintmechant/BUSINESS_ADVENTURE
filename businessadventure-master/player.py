import pygame
from projectile import Projectile

#creer une premiere classe qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self,game):
         super().__init__()
         self.game= game
         self.health=100
         self.max_health=100
         self.attack=20
         self.velocity=5
         self.all_projectiles= pygame.sprite.Group()
         self.image=pygame.image.load('assets/assets/rich-lebon.png')
         self.image=pygame.transform.smoothscale(self.image,(150,170))
         self.image.get_rect()
         self.rect=self.image.get_rect()
         self.rect.x=400
         self.rect.y=500

    def damage(self,amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #si le jouer n'a plus de point de vie
            self.game.game_over()

    def kit(self,amount2):
        if self.health < self.max_health:
            self.health += amount2

        else:
            self.health += 0


    def update_health_bar(self, surface):
        # dessiner notre bar de vie
        pygame.draw.rect(surface, (101, 119, 97), [self.rect.x + 25, self.rect.y -10, self.max_health, 7])
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 25, self.rect.y -10, self.health, 7])

    def launch_projectile(self):
        #creer une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        #si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self,self.game.all_monsters):
           self.rect.x+= self.velocity

    def move_left(self):
         self.rect.x-= self.velocity

