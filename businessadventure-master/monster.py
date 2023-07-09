import pygame
import random

#creer une classe qui va gerer un monstre sur notre jeu

class Monster(pygame.sprite.Sprite):

   def __init__(self,game):
       super().__init__()
       self.game=game
       self.health=100
       self.max_health=100
       self.attack=0.3
       self.image=pygame.image.load('assets/assets/sdf.png')
       self.image=pygame.transform.smoothscale(self.image,(95,125))
       self.rect=self.image.get_rect()
       self.rect.x=1000+ random.randint(0,300)
       self.rect.y=540
       self.velocity=random.randint(1,3)

   def damage(self,amount):
       #infliger les degats
       self.health-= amount

       #verifie si son nouveau nombrre de point de vie est inférieur ou égal à 0
       if self.health<= 0:
           #reapparaitre comme un nouveau monstre
           self.rect.x=1000+random.randint(0,300)
           self.velocity = random.randint(1, 3)
           self.health=self.max_health
           self.game.add_score(100)
           #print(self.game.score)
           #si la barre d'évenement est chargé àson maximum
           if self.game.comet_event.is_full_loaded() and self.game.gem_event.is_full_loaded():
              #retirer du jeu
              self.game.all_monsters.remove(self)

              # appel de la méthode pour essayer de déclencher la pluie de comètes
              self.game.comet_event.attempt_fall()
             # retirer du jeu
              self.game.all_monsters.remove(self)

            # appel de la méthode pour essayer de déclencher la pluie de comètes
              self.game.gem_event.attempt_fall()

   def update_health_bar(self,surface):

       #dessiner notre bar de vie
       pygame.draw.rect(surface, (101,119,97), [self.rect.x + 10, self.rect.y - 20, self.max_health, 5])
       pygame.draw.rect(surface,(111,210,46),[self.rect.x+10,self.rect.y-20,self.health,5])

   def forward(self):
       # le deplacement nese fait que si il n'y a pas de collision avec un groupe de joueur
       if not self.game.check_collision(self,self.game.all_players):
          self.rect.x -= self.velocity
       #si le monstre est en collision avec le joueur
       else:
           #infliger des degats au joueur
        self.game.player.damage(self.attack)