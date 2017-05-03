# Import pygame modules
import pygame

# Coordinates for serpent and pie
serpentx = 1
serpenty = 1
piex = 19
piey = 14

# Serpent direction
dirx = 1
diry = 0

# Initialize display module
pygame.display.init( )

# Create display screen
screen = pygame.display.set_mode( ( 800 , 600 ) )

# The game loop
def loop( ) :

    while True :

        # Clear the screen
        pygame.draw.rect( screen , ( 0 , 0 , 0 ) , ( 0 , 0 , 800 , 600 ) )

        # Draw 
        draw( )

        # Update the display
        pygame.display.update( )

        # Update state of play
        update( )

        # Handle keyboard events
        pygame.event.pump( )

        for event in pygame.event.get( ) :

            # Escape key exits game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :

                    pygame.quit( )  

                    return

            # Handle arrow keys
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN :

                changedirection( 0 , 1 )

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP :

                changedirection( 0 , -1 )

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT :

                changedirection( 1 , 0 )

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT :

                changedirection( -1 , 0 )

# Draw everything onto the screen
def draw( ) :
    pygame.draw.circle( screen , ( 227 , 11 , 93 ) , ( piex * 40 , piey * 40 ) , 20 , 0 )
    pygame.draw.circle( screen , ( 89 , 152 , 47 ) , ( serpentx * 40 , serpenty * 40 ) , 20 , 0 )

# Update state
def update( ) :
    global serpentx , serpenty
    serpentx = serpentx + dirx
    serpenty = serpenty + diry
    # Clamp serpent
    if serpentx > 19 : serpentx = 19
    if serpentx < 1 : serpentx = 1
    if serpenty > 14 : serpenty = 14
    if serpenty < 1 : serpenty = 1

# Change serpent direction to parameters
def changedirection( dx , dy ) :
    global dirx , diry
    dirx = dx
    diry = dy

# Run main loop
loop( )
