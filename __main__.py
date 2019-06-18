import sys
from features import constant
import pygame


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode(constant.SCREEN_RESOLUTION)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(constant.COLOR_RGB_BLACK)
        pygame.display.flip()


if __name__ == "__main__":
    main()
