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
yellow = (229, 221, 149)
lilla = (100, 100, 255,)

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

map = [["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","1","1","1","1","1","1","1","0","0","0","1","1","1","1","1","1","1","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","1","1","1","1","1","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","1","0","0","1","1","1","1","1","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","1","1","1","1","1","1","1","0","0","0","1","1","1","1","1","1","1","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",],
       ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0",]]

# Lager et rektangel-objekt, definerer (x, y, lengde, høyde, r, g, b, vindusobjekt)
løper = rektangel(0, 0, 30, 30, blue, vindu)
harn = rektangel(600, 600, 30, 30, red, vindu)
nektar = rektangel(300, 300, 30, 30, yellow, vindu)
#nektar = rektangel(round(r.random()*630), round(r.random()*630), 30, 30, 255, 255, 0, vindu)

speed = 2
slowness = 0.01

# Gjenta helt til brukeren lukker vinduet. Her kaller man funksjonener som flytter og tenger firkantene

def draw_map():
    løper_rect = pg.Rect(løper.x, løper.y, løper.lengde, løper.høyde)
    collided_rects = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == "1":
                firkant = rektangel(30*x, 30*y, 30, 30, lilla, vindu)
                firkant_rect = pg.Rect(firkant.x, firkant.y, firkant.lengde, firkant.høyde)
                firkant.tegn()
                print(løper.x)
                if løper_rect.colliderect(firkant_rect):
                    collided_rects.append(firkant_rect)
    if collided_rects:
        if løper.x + 30 <= firkant_rect.x:
           løper.x = løper.x - 3
           løper.farge = green 
        if løper.x - 30 >= firkant_rect.x:
           løper.farge = red
    else:
        løper.farge = blue
            # løper.colliderect(firkant):
            #    løper.farge = red

fortsett = True
while fortsett:
    pg.time.Clock().tick(120)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False


    trykkede_taster = pg.key.get_pressed()
#harn
    if trykkede_taster[K_RIGHT]:
      harn.x = harn.x + speed
    if trykkede_taster[K_LEFT]:
      harn.x = harn.x - speed
    if trykkede_taster[K_UP]:
        harn.y =harn.y - speed
    if trykkede_taster[K_DOWN]:
        harn.y =harn.y + speed
    
#løper
    if trykkede_taster[K_d]:
      løper.x = løper.x + speed - slowness
    if trykkede_taster[K_a]:
      løper.x = løper.x - speed + slowness
    if trykkede_taster[K_w]:
        løper.y =løper.y - speed + slowness
    if trykkede_taster[K_s]:
        løper.y =løper.y + speed - slowness

    # if (løper.x + løper.lengde)>=harn.x and (løper.x-løper.lengde)<=harn.x+30 and løper.y+løper.lengde>=harn.y and løper.y+løper.lengde<=harn.y+30:
    #     pg.quit()
    if løper.x == nektar.x and løper.y == nektar.y:
      pg.quit()

    # Farger bakgrunnen lyseblå
    vindu.fill((255, 255, 255 ))

    # Tegner og flytter rektangelene
    løper.tegn()
    harn.tegn()
    nektar.tegn()
    draw_map()

#sjekker om løper eller harn er utenfor vinudet
    utenfor(løper)
    utenfor(harn)
 # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()