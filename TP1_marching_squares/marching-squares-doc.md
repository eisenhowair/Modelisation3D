# Documentation de l'implémentation Marching Squares

## Vue d'ensemble

L'algorithme Marching Squares est utilisé pour générer des contours à partir d'une image binaire. Cette implémentation permet de :
- Charger une image et la convertir en grille binaire
- Détecter les contours selon l'algorithme Marching Squares
- Visualiser ou sauvegarder le résultat

## Structure du code

### Classe `MarchingSquares`

La classe principale qui gère tout le processus de l'algorithme.

```python
ms = MarchingSquares(image_path="image.png", grid_size=50)
```

#### Paramètres d'initialisation
- `image_path` (str) : Chemin vers l'image source
- `grid_size` (int) : Nombre de divisions de la grille (résolution des contours)

#### Variables importantes
- `threshold` (int) : Seuil de binarisation (défaut: 127)
- `image` (numpy.array) : Image convertie en matrice binaire
- `contours` (list) : Liste des segments de contours générés

## Fonctions principales

### 1. `load_and_prepare_image()`

Prépare l'image pour le traitement.

```python
def load_and_prepare_image(self):
    image = Image.open(self.image_path).convert('L')
    self.image = np.array(image.resize((self.grid_size, self.grid_size)))
    self.image = (self.image > self.threshold).astype(int)
```

Étapes :
1. Charge l'image et la convertit en niveaux de gris
2. Redimensionne selon la taille de grille spécifiée
3. Binarise l'image selon le seuil (`threshold`)

### 2. `get_cell_case(i, j)`

Détermine le cas Marching Squares pour une cellule donnée.

```python
def get_cell_case(self, i, j):
    # Récupération des 4 coins de la cellule
    top_left = self.image[i, j]
    top_right = self.image[i, j + 1]
    bottom_left = self.image[i + 1, j]
    bottom_right = self.image[i + 1, j + 1]
    
    # Calcul du cas (0-15)
    case = 8 * top_left + 4 * top_right + 2 * bottom_right + bottom_left
    return case
```

#### Paramètres
- `i` (int) : Index de ligne
- `j` (int) : Index de colonne

#### Retour
- Entier entre 0 et 15 représentant le cas de configuration

### 3. `generate_contours()`

Génère tous les segments de contours de l'image.

Utilise une table de correspondance `CASES` qui définit les segments à générer pour chaque cas :
```python
self.CASES = {
    0: [],  # Pas de contour
    1: [((0.5, 1.0), (1.0, 0.5))],  # Un segment
    # ... autres cas ...
    15: []  # Cellule pleine, pas de contour
}
```

Chaque segment est défini par :
- Point de départ `(x1, y1)`
- Point d'arrivée `(x2, y2)`
- Coordonnées normalisées entre 0 et 1 dans la cellule

### 4. `plot_contours(output_path=None)`

Visualise ou sauvegarde les contours générés.

```python
def plot_contours(self, output_path=None):
    plt.figure(figsize=(10, 10))
    plt.imshow(self.image, cmap='gray')
    
    for start, end in self.contours:
        x_coords = [start[0], end[0]]
        y_coords = [start[1], end[1]]
        plt.plot(x_coords, y_coords, 'r-', linewidth=2)
```

#### Paramètres
- `output_path` (str, optionnel) : Chemin pour sauvegarder l'image. Si non spécifié, affiche le résultat.

## Utilisation

### Exemple basique
```python
# Création de l'instance
ms = MarchingSquares("image.png", grid_size=50)

# Traitement et sauvegarde
ms.process("resultat.png")
```

### Exemple avec paramètres personnalisés
```python
ms = MarchingSquares("image.png", grid_size=100)
ms.threshold = 150  # Modifier le seuil de binarisation
ms.process()  # Afficher sans sauvegarder
```

## Notes sur les cas Marching Squares

Les 16 cas possibles (0-15) sont déterminés par la configuration des 4 coins de chaque cellule :
- Coin supérieur gauche : 8
- Coin supérieur droit : 4
- Coin inférieur droit : 2
- Coin inférieur gauche : 1

La valeur du cas est la somme des valeurs des coins actifs (au-dessus du seuil).

## Conseils d'optimisation

1. Ajuster le `grid_size` :
   - Valeurs plus grandes → contours plus détaillés mais traitement plus long
   - Valeurs plus petites → traitement plus rapide mais contours plus grossiers

2. Modifier le `threshold` :
   - Augmenter → moins de zones considérées comme actives
   - Diminuer → plus de zones considérées comme actives

