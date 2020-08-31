# import pygame
import pygame

# initialize game engine
pygame.init()

window_width=600
window_height=600

animation_increment=10
clock_tick_rate=20

# Open a window
size = (window_width, window_height)
screen = pygame.display.set_mode(size)

# Set title to the window
pygame.display.set_caption("Game")

dead=False

clock = pygame.time.Clock()
background_image = pygame.image.load("pic.png").convert()

win = pygame.display.set_mode((600,600))
x = 275
y = 275
width = 50
height = 50

while(dead==False):
    for event in pygame.event.get():
        pygame.time.delay(120)
    	# iterate over the list of Event objects
    	# that was returned by pygame.event.get() method.
        for event in pygame.event.get():
    		if event.type == pygame.QUIT:
    			run = False
        # nth
        keys = pygame.key.get_pressed()
        pygame.draw.rect(win,(255,0,0),(x,y,width,height))
        pygame.image.load("pic.png").convert()
        pygame.display.update()
        if keys[pygame.K_LEFT] and x>60 and x<600:

    		# decrement in x co-ordinate
            x -= 120
        # nth
        if keys[pygame.K_RIGHT] and x<500:

    		# increment in x co-ordinate
            x += 120
        # nth
        if keys[pygame.K_UP] and y>60 and y<600:

    		# decrement in y co-ordinate
            y -= 120

    	if keys[pygame.K_DOWN] and y<500:
    		# increment in y co-ordinate
    		y += 120
        pygame.display.update()
        if event.type == pygame.QUIT:
            dead = True

    screen.blit(background_image, [0, 0])

    #pygame.display.flip()
    #clock.tick(clock_tick_rate)
