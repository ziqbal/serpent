# Import pygame modules
import pygame

# Initialize display module
pygame.display.init( )

# Create display screen with given resolution
screen = pygame.display.set_mode( ( 800 , 600 ) )

# The almighty game loop
def gameloop( ) :

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
    pygame.draw.circle( screen , ( 255 , 255 , 255 ) , ( 400 , 300 ) , 200 , 0 )

# Run main loop
gameloop( )
