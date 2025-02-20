import pygame
import constants as con
import player as ply

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    print("Starting Asteroids!")
    print(f"Screen width: {con.SCREEN_WIDTH}")
    print(f"Screen height: {con.SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_WIDTH))
    player = ply.Player(con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT / 2)



    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        screen.fill("black")
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()