import random

mots = ['papa','chantal','javascript','femmes','jeune','emploi','exemple','vie','hotel','beau','vin']
choix_mots = random.choice(mots)
jeux_mots =['_'for _ in choix_mots]# crée une liste a partir de _
print(jeux_mots) # crée la liste de_
temps = 8 # nombre de choix pour le mots


print("Welcome to Devin_Words")

while temps > 0 and '_' in jeux_mots:
    print("\n" + '' .join(jeux_mots))
    guess = input("Devinez la lettre:").lower()
    if guess in choix_mots:
        for index, letter in enumerate(choix_mots):
            if letter == guess:
                jeux_mots[index] = guess #
    else:
        print("cette lettre ne figure pas dans cet mots, reprends!!!")
        temps -= 1
#conclusion
if '_' not in jeux_mots:
    print("tu as deviné le mots!")
    print(''.join(jeux_mots))
    print("gagnez!")
else:
    print("temps écoulé.le mots est:", + choix_mots)
    print("perdu!")



