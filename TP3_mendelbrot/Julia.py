import pygame
import math
import colorsys

from Mendelbrot import FractalRenderer


class JuliaSet(FractalRenderer):
    def __init__(self, width, height, c=-0.4 + 0.6j, max_iter=100):
        super().__init__(width, height)
        self.c = c
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
                # on convertit les coordonnées
                zx = 1.5 * (x - self.width / 2) / (0.5 * self.width)
                zy = 1.0 * (y - self.height / 2) / (0.5 * self.height)
                z = complex(zx, zy)

                iterations = 0
                while abs(z) <= 2 and iterations < self.max_iter:
                    z = z * z + self.c
                    iterations += 1

                color = self.get_color(iterations)
                self.screen.set_at((x, y), color)


def main():

    fractal = JuliaSet(800, 600, c=-0.4 + 0.6j, max_iter=100)
    fractal.draw()
    fractal.run()


if __name__ == "__main__":
    main()
