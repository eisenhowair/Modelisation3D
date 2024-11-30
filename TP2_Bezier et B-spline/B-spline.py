import numpy as np
import matplotlib.pyplot as plt


def de_boor_cox(t, k, i, knots, control_points):
    if k == 0:
        return 1 if knots[i] <= t < knots[i + 1] else 0
    else:
        if knots[i + k] == knots[i]:
            alpha = 0
        else:
            alpha = (t - knots[i]) / (knots[i + k] - knots[i])
        if knots[i + k + 1] == knots[i + 1]:
            beta = 0
        else:
            beta = (knots[i + k + 1] - t) / (knots[i + k + 1] - knots[i + 1])
        return alpha * de_boor_cox(
            t, k - 1, i, knots, control_points
        ) + beta * de_boor_cox(t, k - 1, i + 1, knots, control_points)


def bezier_curve(control_points, num_points=100):
    n = len(control_points) - 1
    t = np.linspace(0, 1, num_points)
    x = np.zeros(num_points)
    y = np.zeros(num_points)

    for i, t_i in enumerate(t):
        for k in range(n + 1):
            x[i] += control_points[k][0] * de_boor_cox(
                t_i, n, k, [0] * (n + 1) + [1] * (n + 1), control_points
            )
            y[i] += control_points[k][1] * de_boor_cox(
                t_i, n, k, [0] * (n + 1) + [1] * (n + 1), control_points
            )

    return x, y


def b_spline_curve(control_points, knots, degree, num_points=100):
    t = np.linspace(knots[degree], knots[-degree - 1], num_points)
    x = np.zeros(num_points)
    y = np.zeros(num_points)

    for i, t_i in enumerate(t):
        for k in range(len(control_points)):
            x[i] += control_points[k][0] * de_boor_cox(
                t_i, degree, k, knots, control_points
            )
            y[i] += control_points[k][1] * de_boor_cox(
                t_i, degree, k, knots, control_points
            )

    return x, y


def main():

    bezier_points = [(0, 0), (1, 2), (3, 1), (4, 4)]
    b_spline_points = [(0, 0), (1, 2), (3, 1), (4, 4)]
    bezier_points = [(0, 0), (2, 3), (4, 1), (6, 6)]
    b_spline_points = [(0, 0), (2, 3), (4, 1), (6, 6)]
    knots = [0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 4]
    degree = 3

    x_bezier, y_bezier = bezier_curve(bezier_points)
    x_spline, y_spline = b_spline_curve(b_spline_points, knots, degree)

    plt.figure(figsize=(10, 5))
    plt.plot(x_bezier, y_bezier, label="Bézier Curve")
    plt.plot(x_spline, y_spline, label="B-spline Curve")

    for point in bezier_points:
        plt.plot(point[0], point[1], "ro")

    plt.legend()
    plt.title("Courbes de Bézier et B-spline")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
