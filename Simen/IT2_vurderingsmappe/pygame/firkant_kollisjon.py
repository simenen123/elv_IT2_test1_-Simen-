import pygame
import random

pygame.init()


skjerm_bredde = 800
skjerm_høyde = 600
screen = pygame.display.set_mode((skjerm_bredde, skjerm_høyde))
pygame.display.set_caption("Player Collision")

clock = pygame.time.Clock()


sort = (0, 0, 0)
hvit = (255, 255, 255)
rød = (255, 0, 0)


player_speed = 5
player_rect = pygame.Rect(400, 300, 50, 50)


størrelse_på_objekt = 50
mengden_firkanter = 5
object_list = []

#tegner firkanter random steder
for i in range(mengden_firkanter):
    object_x = random.randint(0, skjerm_bredde - størrelse_på_objekt)
    object_y = random.randint(0, skjerm_høyde - størrelse_på_objekt)
    object_rect = pygame.Rect(object_x, object_y, størrelse_på_objekt, størrelse_på_objekt)
    object_list.append(object_rect)


fortsett = True
while fortsett:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fortsett = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x = player_rect.x - player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x = player_rect.x + player_speed
    if keys[pygame.K_UP]:
        player_rect.y = player_rect.y - player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y = player_rect.y + player_speed
    
    # kollisjon
    for obj in object_list:
        if player_rect.colliderect(obj):
            # Determine the direction of collision
            collision_x = player_rect.x - obj.center_x
            collision_y = player_rect.y - obj.center_y
            if abs(collision_x) > abs(collision_y):
                if collision_x > 0:
                    player_rect.left = obj.right
                else:
                    player_rect.right = obj.left
            else:
                if collision_y > 0:
                    player_rect.top = obj.bottom
                else:
                    player_rect.bottom = obj.top
                    

    screen.fill(hvit)
    

    pygame.draw.rect(screen, rød, player_rect)
    

    for obj in object_list:
        pygame.draw.rect(screen, sort, obj)
    

    pygame.display.flip()
    


pygame.quit()

