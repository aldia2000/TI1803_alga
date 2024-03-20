donnees_meteo = [
    ['2024-01-01', 'Paris', 5, 9, 15],
    ['2024-01-02', 'Paris', 19, 5, 14],
    ['2024-01-03', 'Paris', 7, -5, 13],
    ['2024-01-04', 'Paris', 22, 5, 15],
    ['2024-01-05', 'Paris', 2, 2, 20],
    ['2024-01-06', 'Paris', -1, -2, 20],
    ['2024-01-07', 'Paris', 5, 6, 15],
    ['2024-01-08', 'Paris', 4, -4, 9],
    ['2024-01-09', 'Paris', 5, 5, 3],
    ['2024-01-10', 'Paris', 31, 30, 17],
    ['2024-01-01', 'Lyon', 32, 5, 8],
    ['2024-01-02', 'Lyon', 0, -2, 20],
    ['2024-01-03', 'Lyon', 22, 4, 1],
    ['2024-01-04', 'Lyon', 26, -10, 8],
    ['2024-01-05', 'Lyon', 16, 7, 6],
    ['2024-01-06', 'Lyon', 11, 2, 11],
    ['2024-01-07', 'Lyon', 10, 23, 20],
    ['2024-01-08', 'Lyon', 3, 7, 8],
    ['2024-01-09', 'Lyon', 34, 24, 17],
    ['2024-01-10', 'Lyon', -3, 25, 11]
]

def filtrer_ville(donnees, ville):
    resultats = []
    for enregistrement in donnees:
        if enregistrement[1] == ville:
            resultats.append(enregistrement)
    return resultats

def filtrer_periode(donnees):
    ville = input('Entrer la ville: ')
    debut = input("Entrez la date de début (AAAA-MM-JJ) : ")
    fin = input("Entrez la date de fin (AAAA-MM-JJ) : ")
    resultats = []
    for enregistrement in donnees:
        if ville==enregistrement[1]:
            if debut <= enregistrement[0] <= fin:
                resultats.append(enregistrement)
    return resultats

def temperature_max_min(donnees, ville):
    temperatures = [enregistrement[2:5] for enregistrement in donnees if enregistrement[1] == ville]
    max_temp = max(max(t) for t in temperatures)
    min_temp = min(min(t) for t in temperatures)
    return max_temp, min_temp

def temperature_moyenne(donnees, ville):
    temperatures = [enregistrement[2] for enregistrement in donnees if enregistrement[1] == ville]
    moyenne = sum(temperatures) / len(temperatures)
    return moyenne

def afficher_menu():
    print("1. Filtrer les données météo d'une ville")
    print("2. Filtrer les données météo d'une ville pendant une période")
    print("3. Déterminer la température maximale et minimale d'une ville")
    print("4. Déterminer la température moyenne d'une ville")
    print("5. Quitter")

def main():
    while True:
        afficher_menu()
        choix = input("Choisissez une option : ")

        if choix == "1":
            ville = input("Entrez le nom de la ville : ")
            resultats = filtrer_ville(donnees_meteo, ville)
            print(resultats)
        elif choix == "2":
            
            resultats = filtrer_periode(donnees_meteo)
            print(resultats)
        elif choix == "3":
            ville = input("Entrez le nom de la ville : ")
            max_temp, min_temp = temperature_max_min(donnees_meteo, ville)
            print("Température maximale :", max_temp)
            print("Température minimale :", min_temp)
        elif choix == "4":
            ville = input("Entrez le nom de la ville : ")
            moyenne = temperature_moyenne(donnees_meteo, ville)
            print("Température moyenne :", moyenne)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez choisir une option valide.")


main()
