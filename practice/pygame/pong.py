import pygame
from pygame.locals import *

def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 480   # Desired physical surface size, in pixels.

    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    x1 = 0
    x2 = 0
    user1 = (x1,460,150,10)
    user2 = (x2,10,150,10)
    some_color = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:
            key = pygame.key.get_pressed()
            print(key)
            if key[K_d]:
                if x1 <= surface_sz:
                    x1 += 10
            elif key[K_a]:
                if x1 >= 0:
                    x1 -= 10
            user1 = (x1,460,150,10)
            user2 = (x2,10,150,10)
            print(x1, x2)

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((0, 200, 255))

        # Overpaint a smaller rectangle on the main surface
        main_surface.fill(some_color, user1)
        main_surface.fill(some_color, user2)


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()