import numpy as np
import matplotlib.pyplot as plt

def generer_donnees(n_points):
    X = np.random.rand(n_points, 2)
    t = np.array([1 if (2 * x[0] + x[1] - 1 > 0) else -1 for x in X])
    return X, t

class Neurone:
    def __init__(self, alpha=0.01):
        self.biais = 0.5
        self.poids = np.random.uniform(-1, 1, 2)
        self.alpha = alpha

    def fonction_seuil(self, x):
        somme = np.dot(self.poids, x) + self.biais
        return 1 if somme > 0 else -1

    def mise_a_jour(self, x, t):
        y = self.fonction_seuil(x)
        erreur = t - y
        self.biais += self.alpha * erreur * 1
        self.poids += self.alpha * erreur * x
        return int(y != t)

def entrainer(neurone, X, t, iterations=100):
    erreurs_par_epoch = []
    for _ in range(iterations):
        erreurs = 0
        for xi, ti in zip(X, t):
            erreurs += neurone.mise_a_jour(xi, ti)
        erreurs_par_epoch.append(erreurs / len(X))
    return erreurs_par_epoch

def tracer_erreurs(erreurs):
    plt.plot(erreurs)
    plt.xlabel("Itérations")
    plt.ylabel("Taux d'erreur")
    plt.title("Évolution du nombre d'erreurs")
    plt.grid(True)
    plt.show()

def experimenter(n_train=100, n_test=50, alpha=0.01):
    X_train, t_train = generer_donnees(n_train)
    X_test, t_test = generer_donnees(n_test)
    neurone = Neurone(alpha)
    erreurs = entrainer(neurone, X_train, t_train)
    erreurs_test = sum(neurone.fonction_seuil(x) != t for x, t in zip(X_test, t_test))
    taux_erreur_test = erreurs_test / len(X_test)
    print(f"Taux d'erreur sur l'ensemble de test : {taux_erreur_test:.2f}")
    tracer_erreurs(erreurs)

experimenter()
