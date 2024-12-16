import random

def evaluation(state):
    return sum(state)

def generer_voisins(state):
    voisins = []
    for i in range(len(state)):
        voisin = state[:]
        voisin[i] = random.randint(0, 10)
        voisins.append(voisin)
    return voisins

def hill_climbing(etat_initial, max_iterations=100):
    current_state = etat_initial
    current_score = evaluation(current_state)
    
    for iteration in range(max_iterations):
        voisins = generer_voisins(current_state)
        meilleur_voisin = max(voisins, key=evaluation)
        meilleur_score = evaluation(meilleur_voisin)
        
        if meilleur_score <= current_score:
            break
        
        current_state = meilleur_voisin
        current_score = meilleur_score
        print(f"Iteration {iteration+1}: Etat = {current_state}, Score = {current_score}")
    
    return current_state, current_score

if __name__ == "__main__":
    etat_initial = [random.randint(0, 10) for _ in range(5)]
    print("État initial :", etat_initial)
    
    solution, score = hill_climbing(etat_initial)
    print("Meilleure solution trouvée :", solution)
    print("Score final :", score)
