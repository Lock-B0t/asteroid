import pygame
import constants as con

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {con.SCREEN_WIDTH}")
    print(f"Screen height: {con.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_WIDTH))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")


        pygame.display.flip()



if __name__ == "__main__":
    main()