# Liste de tuples des éléments, leurs poids et leurs valeurs.
ele = [
    ("Montre à gousset", 2, 6),
    ("Boule de bowling", 3, 10),
    ("Portait de tata Germaine", 4, 12),
]


def dynamic_knapsack(capacite, elements):
    matrice = [[0 for x in range(capacite + 1)] for x in range(len(elements) + 1)]
    print("matrice :", matrice)

    # On itère sur le nombre d'éléments
    for i in range(1, len(elements) + 1):
        print("i", i)
        # On parcourt notre tableau des capacités
        for w in range(1, capacite + 1):
            print("w", w)
            if elements[i - 1][1] <= w:
                matrice[i][w] = max(
                    elements[i - 1][2] + matrice[i - 1][w - elements[i - 1][1]],
                    matrice[i - 1][w],
                )

            else:
                matrice[i][w] = matrice[i - 1][w]

    print(matrice)

    # Retrouver les éléments en fonction de la somme
    w = capacite
    n = len(elements)
    elements_selection = []

    while w >= 0 and n >= 0:
        e = elements[n - 1]
        print("e", e)
        if matrice[n][w] == matrice[n - 1][w - e[1]] + e[2]:
            elements_selection.append(e)
            w -= e[1]

        n -= 1

    return matrice[-1][-1], elements_selection


test = dynamic_knapsack(5, ele)
print("final", test)
