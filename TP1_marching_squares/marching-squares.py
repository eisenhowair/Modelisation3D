import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import sys


class MarchingSquares:
    def __init__(self, image_path, grid_size=100):
        """
        Initialise l'algorithme Marching Squares

        Args:
            image_path (str): Chemin vers l'image source
            grid_size (int): Nombre de zones qui divisent l'image
        """
        self.image_path = image_path
        self.grid_size = grid_size
        self.image = None
        self.threshold = 127  # Seuil pour la binarisation
        self.contours = []

        # tableau de 16 pour représenter les 16 cas possibles des carrés
        # Chaque segment est défini par deux points (x1,y1), (x2,y2)
        self.CASES = {
            0: [],  # tous les points passe le seuil
            1: [((0.5, 1.0), (1.0, 0.5))],
            2: [((1.0, 0.5), (0.5, 0.0))],
            3: [((0.5, 1.0), (0.5, 0.0))],
            4: [((0.0, 0.5), (0.5, 0.0))],
            5: [((0.5, 1.0), (0.0, 0.5))],
            6: [((0.0, 0.5), (1.0, 0.5))],
            7: [((0.5, 1.0), (1.0, 0.5))],
            8: [((0.5, 1.0), (0.0, 0.5))],
            9: [((0.0, 0.5), (1.0, 0.5))],
            10: [((0.5, 1.0), (0.5, 0.0))],
            11: [((1.0, 0.5), (0.5, 0.0))],
            12: [((0.0, 0.5), (0.5, 0.0))],
            13: [((0.5, 1.0), (0.5, 0.0))],
            14: [((0.0, 0.5), (1.0, 0.5))],
            15: [],  # aucun point passent le seuil
        }

    def load_and_prepare_image(self):
        """Charge et prépare l'image pour le traitement"""

        image = Image.open(self.image_path).convert("L")
        self.image = np.array(image.resize((self.grid_size, self.grid_size)))
        self.image = (self.image > self.threshold).astype(int)

    def get_cell_case(self, i, j):
        """
        Marching Squares pour une cellule

        Args:
            i (int): Index de ligne
            j (int): Index de colonne

        Returns:
            int: Numéro du cas (0-15)
        """
        if i >= self.grid_size - 1 or j >= self.grid_size - 1:
            return 0

        # Récupérer les valeurs des 4 coins
        top_left = self.image[i, j]
        top_right = self.image[i, j + 1]
        bottom_left = self.image[i + 1, j]
        bottom_right = self.image[i + 1, j + 1]

        # Calculer le cas
        case = 8 * top_left + 4 * top_right + 2 * bottom_right + bottom_left
        return case

    def generate_contours(self):
        """Génère les contours pour toute l'image"""
        self.contours = []

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                case = self.get_cell_case(i, j)
                segments = self.CASES[case]

                # Convertir les segments en coordonnées réelles
                for start_point, end_point in segments:
                    start = (j + start_point[0], i + start_point[1])
                    end = (j + end_point[0], i + end_point[1])
                    self.contours.append((start, end))

    def plot_contours(self, output_path=None):
        """
        Affiche ou sauvegarde les contours générés

        Args:
            output_path (str, optional): Chemin pour sauvegarder l'image
        """
        plt.figure(figsize=(10, 10))
        plt.imshow(self.image, cmap="gray")

        for start, end in self.contours:
            x_coords = [start[0], end[0]]
            y_coords = [start[1], end[1]]
            plt.plot(x_coords, y_coords, "r-", linewidth=2)

        plt.grid(True)
        plt.axis("equal")

        if output_path:
            plt.savefig(output_path)
        else:
            plt.show()

    def process(self, output_path=None):
        """
        Exécute l'algorithme complet de Marching Squares

        Args:
            output_path (str, optional): Chemin pour sauvegarder le résultat
        """
        self.load_and_prepare_image()
        self.generate_contours()
        self.plot_contours(output_path)


def main():
    image_path = "images_test/096833.jpg"

    if len(sys.argv) > 1:
        grid_size = 5
    else:
        grid_size = int(sys.argv[1])  # Nombre de zones qui divisent l'image
    nom_image = image_path.replace("images_test/", "").replace(".jpg", "")
    output_path = f"resultat_{nom_image}.png"  # Optionnel
    print(output_path)

    # Créer et exécuter l'algorithme
    ms = MarchingSquares(image_path, grid_size)
    ms.process(output_path)


if __name__ == "__main__":
    main()
