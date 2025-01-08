import matplotlib.pyplot as plt
import numpy as np

def create_radar_chart(num_vars, data, labels, title):
    # Calculer l'angle de chaque axe dans le graphique (diviser la circonférence du cercle par le nombre de variables)
    angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

    # Assurer la continuité en fermant le cercle
    data = np.concatenate((data, [data[0]]))  # fermer le cercle
    angles += angles[:1]  # fermer le cercle

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.fill(angles, data, color='red', alpha=0.25)
    ax.set_yticklabels([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    plt.title(title)
    plt.show()
    
# Demander à l'utilisateur le titre du graphique
title = input("Entrez le titre du graphique : ")

# Demander à l'utilisateur le nombre de données
num_vars = int(input("Entrez le nombre de données que doit contenir le graphique : "))

# Demander à l'utilisateur les noms des données
labels = []
for i in range(num_vars):
    label = input(f"Entrez le nom pour la donnée {i+1} : ")
    labels.append(label)

# Demander à l'utilisateur les valeurs des données (1=E - 5=A)
data = []
for i in range(num_vars):
    val = float(input(f"Entrez la valeur pour la donnée {i+1} (E à A) : "))
    data.append(val)

# Créer le graphique en radar
create_radar_chart(num_vars, data, labels, title)