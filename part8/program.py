# Import pygame modules
import pygame

# Import random module
import random

# Coordinates for serpent and pie
serpent = [ [ 1 , 1 ] ]
pie = [ 19 , 14 ]

# Serpent direction
direction = [ 1 , 0 ]

# Initialize display module
pygame.display.init( )

# Create display screen
screen = pygame.display.set_mode( ( 800 , 600 ) )

# The game loop
def loop( ) :

    # Used for slowing game down
    clock = pygame.time.Clock( )

    while True :

        # Clear the screen
        pygame.draw.rect( screen , ( 0 , 0 , 0 ) , ( 0 , 0 , 800 , 600 ) )

        # Draw 
        draw( )

        # Update the display
        pygame.display.update( )

        # Update state of play
        update( )

        # Slow down game
        clock.tick( 3 )

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
    pygame.draw.circle( screen , ( 89 , 152 , 47 ) , ( serpentx * 40 , serpentx * 40 ) , 20 , 0 )
    pygame.draw.circle( screen , ( 227 , 11 , 93 ) , ( pie[ 0 ] * 40 , pie[ 1 ] * 40 ) , 20 , 0 )

# Update state
def update( ) :
    global serpent , pie

    head = serpent[ 0 ]

    serpentx = head[ 0 ] + direction[ 0 ]
    serpenty = head[ 1 ] + direction[ 1 ]

    # Clamp serpent
    if serpentx > 19 : serpentx = 19
    if serpentx < 1 : serpentx = 1
    if serpenty > 14 : serpenty = 14
    if serpenty < 1 : serpenty = 1

    # Check if serpent is same place as the pie
    if serpentx == pie[ 0 ] and serpenty == pie[ 1 ] :
        pie = [ random.randint( 1 , 19 ) , random.randint( 1 , 14 ) ]

    head = [ serpentx , serpenty ]
    serpent[ 0 ] = head


# Change serpent direction to parameters
def changedirection( dx , dy ) :
    global direction
    direction = [ dx , dy ]

# Run main loop
loop( )
