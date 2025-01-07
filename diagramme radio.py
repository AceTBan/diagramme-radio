import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(num_vars, data):
    # Calculer l'angle de chaque axe dans le graphique (diviser la circonférence du cercle par le nombre de variables)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Assurer la continuité en fermant le cercle
    data = np.concatenate((data, [data[0]]))  # fermer le cercle
    angles += angles[:1]  # fermer le cercle

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, data, color='red', alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(range(1, num_vars + 1))

    plt.show()

# Demander à l'utilisateur le nombre de données
num_vars = int(input("Entrez le nombre de données que doit contenir le graphique : "))

# Demander à l'utilisateur les valeurs des données
data = []
for i in range(num_vars):
    val = float(input(f"Entrez la valeur pour la donnée {i+1} (E à A) : "))
    data.append(val)

# Créer le graphique en radar
create_radar_chart(num_vars, data)