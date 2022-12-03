import pygame, random

# Toimiva versio. Toiminnallisuus:
#   Haamu seuraa, collision toimii 
#   Kolikoita voi kerätä ja laskuri lisääntyy / nollaantuu
#   Robottia voi ohjata
#   Kommentointi englanniksi jos täytyy kysyä apua koodiin ulkomaailmasta. Ei tarvinnut.

def loop():
    while True:
        check_events()
        draw_screen()
        chase()
        kolikko_random()

def check_events():
    global robotti_vasemmalle, robotti_oikealle, robotti_ylos, robotti_alas
    for event in pygame.event.get():
        # Check keys down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                robotti_vasemmalle = True
            if event.key == pygame.K_RIGHT:
                robotti_oikealle = True
            if event.key == pygame.K_UP:
                robotti_ylos = True
            if event.key == pygame.K_DOWN:
                robotti_alas = True
        # Check keys up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                robotti_vasemmalle = False
            if event.key == pygame.K_RIGHT:
                robotti_oikealle = False
            if event.key == pygame.K_UP:
                robotti_ylos = False
            if event.key == pygame.K_DOWN:
                robotti_alas = False
        if event.type == pygame.QUIT:
            exit()

    # Movement and walls
    if robotti_vasemmalle and robotti_rect.x > 0:
        robotti_rect.x -= robotti_speed
    if robotti_oikealle and robotti_rect.x <= screen_width - robotti.get_width():
        robotti_rect.x += robotti_speed
    if robotti_ylos and robotti_rect.y >= 5:
        robotti_rect.y -= robotti_speed
    if robotti_alas and robotti_rect.y <= screen_height - robotti.get_height():
        robotti_rect.y += robotti_speed

def draw_screen():
    screen.fill((255, 0, 0) if robotti_rect.colliderect(haamu_rect) else (255, 255, 255))
    screen.blit(robotti, robotti_rect)
    screen.blit(haamu, haamu_rect)
    screen.blit(kolikko, kolikko_rect)
    score_counter()
    pygame.display.flip()
    clock.tick(60)

def chase():
    if haamu_rect.y > robotti_rect.y:
        haamu_rect.y -= haamu_speed
    if haamu_rect.y < robotti_rect.y:
        haamu_rect.y += haamu_speed

    if haamu_rect.x > robotti_rect.x:
        haamu_rect.x -= haamu_speed
    if haamu_rect.x < robotti_rect.x:
        haamu_rect.x += haamu_speed

    if haamu_rect.colliderect(robotti_rect):
        score_counter(True, False)

def kolikko_random():
    if robotti_rect.colliderect(kolikko_rect):
        kolikko_rect.x = random.randint(0, screen_width - kolikko.get_width())
        kolikko_rect.y = random.randint(0, screen_height - kolikko.get_height())
        score_counter(False, True)

# Score counter. Hitting kolikko adds one to global variable score. Hitting haamu resets score to 0.
def score_counter(reset: bool=False, add_point: bool=False):
    global score
    font = pygame.font.SysFont("Arial", 24)
    text = font.render(str(score), True, (0, 0, 255))
    if add_point == True:
        score += 1
    if reset == True:
        score = 0
    text = font.render(str(score), True, (0, 0, 255))
    screen.blit(text, (screen_width/2 - text.get_width(), 0))



pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Kolikkojahti')
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)
score = 0


# Loading robotti
robotti = pygame.image.load('robo.png')
robotti_rect = robotti.get_rect()
robotti_rect.topleft = 0, 0
robotti_speed = 5
robotti_vasemmalle, robotti_oikealle, robotti_ylos, robotti_alas = False, False, False, False

# Loading haamu
haamu = pygame.image.load('hirvio.png')
haamu_rect = robotti.get_rect()
haamu_rect.bottomright = screen_width, screen_height
haamu_speed = 3

# Loading kolikko
kolikko = pygame.image.load('kolikko.png')
kolikko_rect = kolikko.get_rect()
kolikko_rect.center = random.randint(0, screen_width), random.randint(0, screen_height)



if __name__ == "__main__":
    
    loop()  
