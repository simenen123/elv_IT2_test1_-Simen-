#importerer de forskjellie bibliotekene
import pygame as pg
import math as m
import random as r
import time as t

from pygame.locals import (K_a, K_w, K_d, K_s)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu hvor alt skjer
VINDU_BREDDE = 630
VINDU_HOYDE  = 630
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

def utenfor(object):
  if object.x <= 30:
    object.x = 30
  elif object.x >= 600 - object.lengde:
    object.x = 570
  elif object.y <= 30:
    object.y = 30
  elif object.y >= 600 - object.lengde:
    object.y = 570

red = (255, 0, 0)
black =  (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (229, 221, 149)
lilla = (100, 100, 255,)
white = (255, 255, 255)

#lager klassen rektangel, denne klassen er både løperen og rektangelen som flyr rundt.
class rektangel:
  """Klasse for å representere en rektangel"""
  def __init__(self, x, y, lengde, høyde, farge, vindusobjekt):
    """posisjon"""
    self.x = x
    self.y = y
    "størrelse"
    self.lengde = lengde
    self.høyde = høyde
    "fargene, rød, grønt og blått"
    self.farge = farge
    self.vindusobjekt = vindusobjekt
  
  def rect(self):
    """Returnerer en Rect-objekt for rektangelet"""
    return pg.Rect(self.x, self.y, self.lengde, self.høyde)
  
  def tegn(self):
    """Metode for å tegne rektangel"""
    pg.draw.rect(self.vindusobjekt, (self.farge), (self.x, self.y, self.lengde, self.høyde)) 



løper = rektangel(300, 600, 30, 30, blue, vindu)
boss = rektangel(160, 90, 30, 30, green, vindu)
stige = rektangel(570, 100, 10, 500, green, vindu)
heis = rektangel(40, 570, 10, 30, lilla, vindu)

platform_nede = rektangel(460, 500, 60, 10, lilla, vindu)
platform_oppe = rektangel(460, 300, 60, 10, lilla, vindu)
platform_boss = rektangel(120, 120, 100, 10, lilla, vindu)

platformer = [platform_nede, platform_oppe, platform_boss]

poeng1 = rektangel(490, 490, 10, 10, red, vindu)
poeng2 = rektangel(490, 290, 10, 10, red, vindu)


vegg_høyre = rektangel(640, 0, 30, VINDU_HOYDE, black, vindu)
vegg_venstre = rektangel(0, 0, 30, VINDU_HOYDE, black, vindu)

vegg_nede = rektangel(0, 600, VINDU_BREDDE, 30, black, vindu)
vegg_nede_liten = rektangel(100, 600, 30, 30, black, vindu)

vegg_oppe = rektangel(0, 0, VINDU_BREDDE, 30, black, vindu)
vegger = [vegg_venstre, vegg_høyre, vegg_nede, vegg_oppe, vegg_nede_liten]

speed = 2
gravity = 2
poeng = 0
h = 0

fortsett = True
while fortsett:
    pg.time.Clock().tick(120)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False



    trykkede_taster = pg.key.get_pressed()
    
#løper
    if trykkede_taster[K_d]:
      løper.x = løper.x + speed
    if trykkede_taster[K_a]:
      løper.x = løper.x - speed
    if trykkede_taster[K_w]:
        løper.y =løper.y - speed
    if trykkede_taster[K_s]:
        løper.y =løper.y + speed


    if løper.rect().colliderect(stige.rect()):
        gravity = 0
    else:
        gravity = 2

    #sjekker om spiller er på platform
    for i in platformer:
         if løper.rect().colliderect(i.rect()):
            løper.y = i.y - løper.høyde
    
    for i in platformer:
         if boss.rect().colliderect(i.rect()):
            boss.y = i.y - boss.høyde


    if løper.rect().colliderect(heis.rect()):
       heis.y = 30
       løper.y = 30


    if løper.rect().colliderect(poeng1.rect()):
       poeng = poeng + 1
       poeng1.x = 700
       print(poeng)
    
    if løper.rect().colliderect(poeng2.rect()):
      poeng = poeng + 1
      poeng2.x = 700
      print(poeng)


      #boss 
    if løper.rect().colliderect(boss.rect()):
       boss.x = boss.x + speed
    


    if løper.y <= 600:
       løper.y = løper.y + gravity
      
    if boss.y <= 600:
       boss.y = boss.y + gravity
       
    # Farger bakgrunnen lyseblå
    vindu.fill((255, 255, 255 ))

    # Tegner og flytter rektangelene
    løper.tegn()
    stige.tegn()
    heis.tegn()
    platform_nede.tegn()
    platform_oppe.tegn()
    platform_boss.tegn()
    poeng1.tegn()
    poeng2.tegn()
    boss.tegn()

    for i in vegger:
         i.tegn()

    #mål 
    if poeng == 2 and boss.x == 7000:
        vegg_nede_liten.farge = white
    #sjekker om løper er utenfor vinduet
    if vegg_nede_liten.farge == white and løper.rect().colliderect(vegg_nede_liten.rect()):
        print("Du vant!")
        fortsett = False
    utenfor(løper)
    if boss.rect().colliderect(vegg_nede.rect()):
        boss.x = 7000

 # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()