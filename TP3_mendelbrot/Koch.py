import pygame
import math
import colorsys

from Mendelbrot import FractalRenderer


class KochSnowflake(FractalRenderer):
    def __init__(self, width, height, iterations=4):
        super().__init__(width, height)
        self.iterations = iterations

    def koch_line(self, start, end, iterations):
        if iterations == 0:
            pygame.draw.line(self.screen, (255, 255, 255), start, end)
            return

        dx = end[0] - start[0]
        dy = end[1] - start[1]

        # les nouveaux points
        p1 = start
        p2 = (start[0] + dx / 3, start[1] + dy / 3)
        p3 = (
            start[0] + dx / 2 - dy * math.sqrt(3) / 6,
            start[1] + dy / 2 + dx * math.sqrt(3) / 6,
        )
        p4 = (start[0] + 2 * dx / 3, start[1] + 2 * dy / 3)
        p5 = end

        self.koch_line(p1, p2, iterations - 1)
        self.koch_line(p2, p3, iterations - 1)
        self.koch_line(p3, p4, iterations - 1)
        self.koch_line(p4, p5, iterations - 1)

    def draw(self):
        size = min(self.width, self.height) * 0.8
        center_x = self.width / 2
        center_y = self.height / 2

        points = [
            (center_x - size / 2, center_y + size / 3),
            (center_x + size / 2, center_y + size / 3),
            (center_x, center_y - size / 3),
        ]

        self.screen.fill((0, 0, 0))
        self.koch_line(points[0], points[1], self.iterations)
        self.koch_line(points[1], points[2], self.iterations)
        self.koch_line(points[2], points[0], self.iterations)


def main():

    fractal = KochSnowflake(800, 600, iterations=5)
    fractal.draw()
    fractal.run()


if __name__ == "__main__":
    main()
