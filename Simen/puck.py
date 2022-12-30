#importerer de forskjellie bibliotekene
import pygame as pg
import math as m

from pygame.locals import (K_UP, K_DOWN, K_LEFT, K_RIGHT)

# Initialiserer/starter pygame
pg.init()

# Oppretter et vindu hvor alt skjer
VINDU_BREDDE = 500
VINDU_HOYDE  = 500
vindu = pg.display.set_mode([VINDU_BREDDE, VINDU_HOYDE])

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

# Lager et rektangel-objekt, definerer (x, y, xfart, yfart, lengde, høyde, vindusobjekt)
rektangel1 = rektangel(350, 450, 0, 0, 50, 20, vindu)
rektangel2 = rektangel(300, 200, 1, 1, 20, 20, vindu)
rektangel3 = rektangel(100, 200, 1, 1, 20, 20, vindu)

"Kode som ikke ble ferdig"
# def finn_avstand(obj1, obj2):
#   xAvstand2 = (obj1.x - obj2.x)**2  # x-avstand i andre
#   yAvstand2 = (obj1.y - obj2.y)**2  # y-avstand i andre
#   avstand = m.sqrt(xAvstand2 + yAvstand2)
#   if avstand <= obj1.lengde + obj2.lengde:
#     obj1.yfart = -obj1.yfart
#     obj1.xfart = -obj1.xfart
#     obj2.yfart = -obj2.yfart
#     obj2.xfart = -obj2.xfart
#   return avstand



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
    rektangel1.tegn()
    rektangel1.flytt_x()
    rektangel1.flytt_y()

    rektangel2.tegn()
    rektangel2.flytt_x()
    rektangel2.flytt_y()

    # rektangel3.tegn()
    # rektangel3.flytt_x()
    # rektangel3.flytt_y()

    # Definerer forskjellige variabler som skulle bli brukt for kollisjon
    player_top = rektangel1.y
    player_side_right = rektangel1.x
    player_side_left = -rektangel1.x
    player_position = rektangel1.x + rektangel1.y
    rektangel_bottom = rektangel2.y + rektangel2.høyde
    rektangel_side_left = rektangel2.x
    rektangel_side_right = -rektangel2.x
    rektangel_position = rektangel2.x + rektangel2.y

  #sjekker om spilleren kræsjer med den andre firkanten som flyr rundt
    if player_top <= rektangel_bottom and player_side_right <= rektangel_side_left:
      rektangel2.yfart = -rektangel2.yfart
    # elif player_top <= rektangel_bottom and player_side_right <= rektangel_side_right:
    #   rektangel2.yfart = -rektangel2.yfart
    
    # if rektangel2.y < rektangel1.y + rektangel1.høyde and \
    #             rektangel2.høyde + rektangel2.y > rektangel1.y:
    #         if rektangel2.x < rektangel1.x + rektangel1.width and \
    #                 rektangel2.x + rektangel2.width > rektangel1.x:
    
     #Kode for å kunne flytte på objektet rektangel1
    trykkede_taster = pg.key.get_pressed()

    if trykkede_taster[K_RIGHT]:
      rektangel1.x = rektangel1.x + 2
    if trykkede_taster[K_LEFT]:
      rektangel1.x = rektangel1.x - 2
      
    # Oppdaterer alt innholdet i vinduet
    pg.display.flip()

# Avslutter pygame
pg.quit()
