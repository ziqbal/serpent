# Import pygame modules
import pygame

# Coordinates for serpent and pie
serpentx = 1
serpenty = 1
piex = 19
piey = 14

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

        # Handle keyboard events
        pygame.event.pump( )

        for event in pygame.event.get( ) :

            # Escape key exits game
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE :

                    pygame.quit( )  

                    return

# Draw everything onto the screen
def draw( ) :
    pygame.draw.circle( screen , ( 89 , 152 , 47 ) , ( serpentx * 40 , serpenty * 40 ) , 20 , 0 )
    pygame.draw.circle( screen , ( 227 , 11 , 93 ) , ( piex * 40 , piey * 40 ) , 20 , 0 )

# Run main loop
loop( )
