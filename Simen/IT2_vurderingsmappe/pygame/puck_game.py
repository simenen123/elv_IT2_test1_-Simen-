#importerer de forskjellie bibliotekene
import pygame as pg
import math as m
import random as r

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu hvor alt skjer
VINDU_BREDDE = 630
VINDU_HOYDE  = 630
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])


speed_x = 1
speed_y = 1

def utenfor(object):
  #x-asksen
  if object.x <= 0:
    object.x = 1
  elif object.x >= VINDU_BREDDE - object.lengde:
    object.x = VINDU_BREDDE - object.lengde
    #y-aksen
  elif object.y <= 0:
    object.y = 1
  elif object.y >= VINDU_HOYDE - object.høyde:
    object.y = VINDU_HOYDE - object.høyde

def utenfor_ball(object):
  global speed_x, speed_y
  #x-asksen
  if object.x <= 0:
    speed_x = speed_x * -1
  elif object.x >= VINDU_BREDDE - object.lengde:
    speed_x = speed_x * -1
    #y-aksen
  elif object.y <= 0:
    speed_y = speed_y * -1

#lager klassen rektangel, denne klassen er både spilleren og rektangelen som flyr rundt.
class rektangel:
  """Klasse for å representere en rektangel"""
  def __init__(self, x, y, xfart, yfart, lengde, høyde, vindusobjekt , R = 255,G = 69,B = 0):
    """posisjon"""
    self.x = x
    self.y = y
    "fart"
    self.xfart = xfart
    self.yfart = yfart
    "størrelse"
    self.lengde = lengde
    self.høyde = høyde
    self.vindusobjekt = vindusobjekt
    "fargene, rød, grønt og blått"
    self.R = R
    self.G = G
    self.B = B

  def rect(self):
    """Returnerer en Rect-objekt for rektangelet"""
    return pg.Rect(self.x, self.y, self.lengde, self.høyde)
  
  def tegn(self):
    """Metode for å tegne rektangel"""
    pg.draw.rect(self.vindusobjekt, (self.R, self.G, self.B), (self.x, self.y, self.lengde, self.høyde)) 

  def flytt_x(self):
    """Metode for å flytte rektangel"""
    # Sjekker om rektangelen er utenfor høyre/venstre kant av spill vinduet
    if ((self.x - self.lengde) <= 0) or ((self.x + self.lengde) >= self.vindusobjekt.get_width()):
      self.xfart = -self.xfart
      # Flytter rektangelen
    self.x += self.xfart

  def flytt_y(self):
    "flytte rektangelen opp"
    # Sjekker om rektangelen treffer taket eller bunnen av spill vinduet
    if ((self.y - self.høyde) <= 0) or ((self.y + self.høyde) >= self.vindusobjekt.get_height()):
      self.yfart = -self.yfart
    self.y +=self.yfart


def lag_ny_ball():
  player_rect = pg.Rect(round(r.random()*600), 300, 20, 20)
  return player_rect

# Lager et rektangel-objekt, definerer (x, y, xfart, yfart, lengde, høyde, vindusobjekt)
spiller = rektangel(350, 600, 0, 0, 50, 20, vindu)
ball = rektangel(round(r.random()*600), 30, 1, 1, 20, 20, vindu)

baller = [ball]


# Gjenta helt til brukeren lukker vinduet. Her kaller man funksjonener som flytter og tenger firkantene
fortsett = True
while fortsett:
    pg.time.Clock().tick(120)
    # Sjekker om brukeren har lukket vinduet
    for event in pg.event.get():
        if event.type == pg.QUIT:
            fortsett = False
    # Farger bakgrunnen lyseblå
    vindu.fill((135, 206, 235 ))

    # Tegner og flytter rektangelene
    spiller.tegn()
    utenfor(spiller)

    # if (ball.x + ball.lengde)>=spiller.x and (ball.x-ball.lengde)<=spiller.x+100 and ball.y+ball.lengde>=spiller.y and ball.y+ball.lengde<=spiller.y+20:
    #   ball.yfart = -ball.yfart
    #   mengden_baller = mengden_baller + 1


    for obj in baller:
      obj.tegn()
      obj.flytt_x()
      obj.flytt_y()
      utenfor_ball(obj)
      if spiller.rect().colliderect(obj):
        obj.yfart = obj.yfart *-1
        ball = rektangel(round(r.random()*600), 30, 1, 1, 20, 20, vindu)
        baller.append(ball)

    #prøvde å fikse kolisjon mellom ballene
    for obj in baller:
      for element in baller:
        if obj.rect().colliderect(element):
          print("hello")
          obj.xfart = obj.xfart * -1
          element.xfart = element.xfart * -1


    ball.tegn()
    
      
    
     #Kode for å kunne flytte på objektet spiller
    trykkede_taster = pg.key.get_pressed()

    if trykkede_taster[K_RIGHT]:
      spiller.x = spiller.x + 2
    if trykkede_taster[K_LEFT]:
      spiller.x = spiller.x - 2
    
    utenfor(spiller)
      
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()

