"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random 


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 700
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

possible_ball_colors = [BLACK, WHITE, GREEN, RED, BLUE]

#Ball 1 and Ball 2
xspeed = random.randint(-10,10)
yspeed = random.randint(-10,10)

x_location = int(screen_width/2)
y_location = int(screen_height/2)

ball_size = random.randint(20, 40)


xspeed_2 = random.randint(-10,10)
yspeed_2= random.randint(-10,10)

x_location_2 = int(screen_width/2)
y_location_2 = int(screen_height/2)

ball_size_2 = random.randint(20, 40)


# BOUNCING BALL CLASS CODE  

class BouncingBall(): 

    # CONSTRUCTOR METHOD 
    def __init__(self, x_location, y_location, x_speed, y_speed, ball_size):  
    # Attributes of the bouncing ball 
        self.x_location = x_location
        self.y_location = y_location  
        self.x_speed = x_speed
        self.y_speed = y_speed 
        self.ball_size = ball_size 

    # BALL METHODS 
    # Flash and Bounce: The actions the ball can perform 
    def flashBounce(self, screen, colors, screen_width, screen_height):

        ball_color = random.choice(colors) # This is outside because of variable scoping.
        pygame.draw.circle(screen, ball_color, [self.x_location, self.y_location], self.ball_size)

        if self.x_location >= screen_width - self.ball_size or self.x_location < self.ball_size:
            self.x_speed = self.x_speed * -1

        if self.y_location >= screen_height - self.ball_size or self.y_location < self.ball_size:
            self.y_speed = self.y_speed * -1

        self.x_location += self.x_speed 
        self.y_location += self.y_speed 

        



#What happens if I instantiate the ball inside the loop?
Ball1 = BouncingBall(x_location, y_location, xspeed, yspeed, ball_size)
Ball2 = BouncingBall(x_location_2, y_location_2, xspeed_2, yspeed_2, ball_size_2)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True




    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here
    #pygame.draw.line(screen, BLUE, (0,0), (200, 300), 10)
    
    #Ball 1
    
    Ball1.flashBounce(screen, RED, screen_width, screen_height)
    Ball2.flashBounce(screen, RED, screen_width, screen_height)
    
    #Ball 1
    pygame.draw.circle(screen, RED, [x_location, y_location], ball_size)
    
    if x_location >= screen_width - ball_size or x_location < ball_size:
    	xspeed  = -1 * xspeed
    
    if y_location >= screen_height - ball_size or y_location < ball_size:
    	yspeed  = -1 * yspeed
    	
    x_location += xspeed
    y_location += yspeed  
    
    #Ball2	
    pygame.draw.circle(screen, RED, [x_location_2, y_location_2], ball_size_2)
    
    if x_location_2 >= screen_width - ball_size_2 or x_location_2 < ball_size_2:
    	xspeed_2  = -1 * xspeed_2
    
    if y_location_2 >= screen_height - ball_size or y_location_2 < ball_size_2:
    	yspeed_2  = -1 * yspeed_2
    
    
    x_location_2 += xspeed_2
    y_location_2 += yspeed_2    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
