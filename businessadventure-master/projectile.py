import pygame

#definir la classe qui va gerer le projectile de notre joueur
class Projectile(pygame.sprite.Sprite):

    #definir le constructeur de cette classe
   def __init__(self,player):
       super().__init__()
       self.velocity=4
       self.player=player
       self.image= pygame.image.load('assets/assets/projectile 1.png')
       self.image= pygame.transform.scale(self.image,(200,200))
       self.rect =self.image.get_rect()
       self.rect.x=player.rect.x+50
       self.rect.y=player.rect.y+1
       self.origin_image=self.image
       self.angle=0

   def rotate(self):
       #tourner le projetile
       self.angle+=9
       self.image=pygame.transform.rotozoom(self.origin_image,self.angle,1)
       self.rect=self.image.get_rect(center=self.rect.center)

   def remove(self):
       self.player.all_projectiles.remove(self)

   def move(self):
       self.rect.x += self.velocity
       self.rotate()

       #verifier entre en collision avec un monstre
       for monster in self.player.game.check_collision(self,self.player.game.all_monsters):
            #supprimeer le projectile
            self.remove()
           #infliger des dégats
            monster.damage(self.player.attack)

       #verifier si notre projectilen'est plus présent sur l'écran
       if self.rect.x > 1080:
          #supprimer le projectile(en dehors de l'écran)
          self.remove()
