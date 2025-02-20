import pygame
import constants as con
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0


    print("Starting Asteroids!")
    print(f"Screedn width: {con.SCREEN_WIDTH}")
    print(f"Screen height: {con.SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((con.SCREEN_WIDTH, con.SCREEN_WIDTH))
    

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable)

    player = Player(con.SCREEN_WIDTH / 2, con.SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        updateable.update(dt)
        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()