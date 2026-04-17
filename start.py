import pygame
from player import player
from mobs import mob
import random

# pygame setup

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True
dt = 0 # delta time
mobs = []
font = pygame.font.Font("8-bit Arcade In.ttf", 50)  # default font, size 50
show_message = False
message_timer = 0
map_data = open("map.txt", "r")
map = []

for i in map_data:
    i = i.strip()
    if i != "":
        row = [int(x) for x in i.split()]
        map.append(row)

# player in the middle
# player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

Player = player(pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2))
mob1 = mob(pos = pygame.Vector2(random.randint(0, 1900), random.randint(0, 1050)))
mob2 = mob(pos = pygame.Vector2(random.randint(0, 1900), random.randint(0, 1050)))
mob3 = mob(pos = pygame.Vector2(random.randint(0, 1900), random.randint(0, 1050)))

mobs = [mob1, mob2, mob3]

# random speed generation for mobs
for i in mobs:
    i.setSpeed(100 * random.randint(1 , 3))

# pygame.QUIT event occurs when user clicks X
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

        # dash ability timer
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LSHIFT and Player.dash_cooldown <= 0:
                message_timer = 5
                Player.dash_timer = 0.2
                Player.dash_cooldown = 5
            elif event.key == pygame.K_LSHIFT and Player.dash_cooldown >= 0:
                show_message = True

    if Player.dash_cooldown > 0:
        Player.dash_cooldown -= dt

    if Player.dash_timer > 0:
        Player.speed = Player.dash_speed
        Player.dash_timer -= dt

    if Player.dash_timer <= 0:
        Player.resetSpeed()
        
    if message_timer > 0:
        message_timer -= dt
    
    if message_timer <= 0:
        show_message = False

                
    # fill the screen with a  color to wipe away anything from last frame
    screen.fill("black")
    # print wait message
    if (show_message):
        cooldown_text = font.render(f"WAIT {round(Player.dash_cooldown)} SECONDS", True, (255, 0, 0))
        screen.blit(cooldown_text, (800, (1080/2)))

    # draw a red circle on the screen imma test it
    pygame.draw.circle(screen, "red", Player.pos, 20)


    # keys used to move

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        Player.pos.y -= Player.speed * dt
    if keys[pygame.K_s]:
        Player.pos.y += Player.speed * dt
    if keys[pygame.K_a]:
        Player.pos.x -= Player.speed * dt
    if keys[pygame.K_d]:
        Player.pos.x += Player.speed * dt


    # mobs practice
    for i in mobs:
        pygame.draw.circle(screen, "blue", i.pos, 20)
        if i.pos != Player.pos:
            if i.pos.x < Player.pos.x:
                i.pos.x += i.speed *dt

            elif i.pos.x > Player.pos.x:
                i.pos.x -= i.speed *dt

            if i.pos.y < Player.pos.y:
                i.pos.y += i.speed *dt

            elif i.pos.y > Player.pos.y:
                i.pos.y -= i.speed *dt
            
            if i.pos.distance_to(Player.pos) < 20:
                Player.health -= 1


    # render and display text
    health_text = font.render(f"Health {Player.health}", True, (255, 255, 255))
    screen.blit(health_text, (20, 20))  # position top-left
    pygame.draw.rect(screen, "green",[20 ,80 ,(Player.health / Player.max_health * 250), 20])


    

    # death
    if Player.health <= 0:
        pygame.quit()


    # close game
    if keys[pygame.K_ESCAPE]:
       pygame.quit()
            

    # flip() the display to screen
    pygame.display.flip()

    # limit fps to 60
    dt = clock.tick(60) / 1000 

    

pygame.quit()

