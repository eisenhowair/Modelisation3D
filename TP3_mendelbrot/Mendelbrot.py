import pygame
import math
import colorsys


class FractalRenderer:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height), pygame.SCALED)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()


class Mandelbrot(FractalRenderer):
    def __init__(self, width, height, max_iter=100):
        super().__init__(width, height)
        self.max_iter = max_iter

    def get_color(self, iterations):
        if iterations == self.max_iter:
            return (0, 0, 0)
        hue = iterations / self.max_iter
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
        return tuple(int(255 * x) for x in rgb)

    def draw(self):
        for x in range(self.width):
            for y in range(self.height):
                zx = 2.0 * (x - self.width / 2) / (0.5 * self.width)
                zy = 1.5 * (y - self.height / 2) / (0.5 * self.height)
                c = complex(zx, zy)
                z = 0

                iterations = 0
                while abs(z) <= 2 and iterations < self.max_iter:
                    z = z * z + c
                    iterations += 1

                color = self.get_color(iterations)
                self.screen.set_at((x, y), color)


def main():

    fractal = Mandelbrot(800, 600, max_iter=100)

    fractal.draw()
    fractal.run()


if __name__ == "__main__":
    main()
