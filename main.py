import pygame
from constants import *
from player import Player


def main() -> None:
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Create player x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)

    updatable = pygame.sprite.Group(player)
    drawable = pygame.sprite.Group(player)
    Player.containers = (updatable, drawable)


    while True:
        screen.fill("black")
        for d in drawable:
            d.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000
        for u in updatable:
            u.update(dt)

        pygame.display.flip()

if __name__ == "__main__":
    main()
