
#DETTE VAR ET PROGRAM JEG LAGDE UNDER EN FREDAGSTIME

#importerer de forskjellie bibliotekene
import pygame as pg
import math as m
import random as r

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT, K_a, K_w, K_d, K_s)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu hvor alt skjer
VINDU_BREDDE = 630
VINDU_HOYDE  = 630
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

def utenfor(object):
  if object.x <= 0:
    object.x = 0
  elif object.x >= 630 - object.lengde:
    object.x = 600
  elif object.y <= 0:
    object.y = 0
  elif object.y >= 630 - object.lengde:
    object.y = 600

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (229, 200, 50)
lilla = (100, 100, 255,)

sidene = ["venstre", "høyre", "oppe", "nede",]
poeng  = 0

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

  
  def tegn(self):
    """Metode for å tegne rektangel"""
    pg.draw.rect(self.vindusobjekt, (self.farge), (self.x, self.y, self.lengde, self.høyde)) 


skudd_speed = 2
skudd_y = 0
skudd_x = 0
start_side = sidene[round(r.random()*3)]
sidene.remove(start_side)

sluttside = sidene[round(r.random()*3)]
sidene.append(start_side)

if start_side == "venstre":
    skudd_y = round(r.random()*630)
    skudd_x = -30

if start_side == "høyre":
    skudd_y =  round(r.random()*650)
    skudd_x = 650

if start_side == "oppe":
    skudd_x = round(r.random()*650)
    skudd_y = 650

if start_side == "nede":
    skudd_x = round(r.random()*650)
    skudd_y = -30

# Lager et rektangel-objekt, definerer (x, y, lengde, høyde, r, g, b, vindusobjekt)
løper = rektangel(0, 0, 30, 30, blue, vindu)
skudd = rektangel(skudd_x, skudd_y, 30, 30, blue, vindu)
nektar = rektangel(round(r.random()*600), round(r.random()*600), 30, 30, yellow, vindu)

print(start_side)
print(sluttside)
speed = 2
slowness = 0.01

# Gjenta helt til brukeren lukker vinduet. Her kaller man funksjonener som flytter og tenger firkantene


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
      løper.x = løper.x + speed - slowness
    if trykkede_taster[K_a]:
      løper.x = løper.x - speed + slowness
    if trykkede_taster[K_w]:
        løper.y =løper.y - speed + slowness
    if trykkede_taster[K_s]:
        løper.y =løper.y + speed - slowness



    if (løper.x + løper.lengde)>=nektar.x and (løper.x-løper.lengde)<=nektar.x+30 and løper.y+løper.lengde>=nektar.y and løper.y+løper.lengde<=nektar.y+30:
        poeng = poeng + 1
        nektar.x = round(r.random()*600)
        nektar.y = round(r.random()*600)
        print(poeng)



    # Farger bakgrunnen lyseblå
    vindu.fill((255, 255, 255 ))

    # Tegner og flytter rektangelene
    løper.tegn()
    nektar.tegn()
    skudd.tegn()

    if start_side == "høyre":
        skudd.x = skudd.x - skudd_speed

    if start_side == "venstre":
        skudd.x = skudd.x + skudd_speed
    
    if start_side == "oppe":
        skudd.y = skudd.y - skudd_speed

    if start_side == "nede":
        skudd.y = skudd.y + skudd_speed
    
    #print(nektar.x)
    #print(nektar.y)

    utenfor(løper)

 # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()