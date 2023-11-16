def menu_principal():
    print("Menu Principal:")
    print("1. Chiffrement/Dechiffrement")
    print("2. Brute Force")
    print("0. Quitter")

def brute_force(texte_chiffre):
    alphabet = "abcdefghijklmnopqrstuvwxyz , abcdefghijklmnopqrstuvwxyz"

    for decalage in range(len(alphabet)):
        texte_dechiffre = ""
        for caractere in texte_chiffre:
            if caractere in alphabet:
                texte_dechiffre += alphabet[(alphabet.index(caractere) - decalage + len(alphabet)) % len(alphabet)]
            else:
                texte_dechiffre += caractere

        print(f"Décalage {decalage}: {texte_dechiffre}")

def chiffdechif_cesar(texte, decalage, mode):
    alphabet = "abcdefghijklmnopqrstuvwxyz , abcdefghijklmnopqrstuvwxyz"
    resultat = ""

    for caractere in texte:
        if caractere in alphabet:
            if mode == "chiffrer":
                resultat += alphabet[(alphabet.index(caractere) + decalage) % len(alphabet)]
            elif mode == "dechiffrer":
                resultat += alphabet[(alphabet.index(caractere) - decalage + len(alphabet)) % len(alphabet)]
        else:
            resultat += caractere

    return resultat

def sous_menu_1():
    choose_menu = input ("Saisissez votre option" + "\n" + "1- Chiffrer" + "\n" +  "2- Dechiffrer " + "\n" + "Saisissez un chiffre : ")

    if choose_menu == "1":
        chiffrer = input("Saisir le mot à chiffrer : " + "\n")
        decalage_chiffrage = int(input("Saisir le décalage des lettres : " + "\n"))
        texte_chiffre = chiffdechif_cesar(chiffrer, decalage_chiffrage, "chiffrer")
        print("Texte chiffré:", texte_chiffre)

    elif choose_menu == "2":
        dechiffrer = input("Saisir le mot à déchiffrer : ")
        decalage_dechiffrage = int(input("Saisir le décalage des lettres : "))
        texte_dechiffre = chiffdechif_cesar(dechiffrer, decalage_dechiffrage, "dechiffrer")
        print("Texte déchiffré:", texte_dechiffre)
        
    else:
        print("Option invalide.")
        

def sous_menu_2():
    print("Vous avez pris l'option Brute Force")
    bruteforce = input("Saisir le texte à décrypter en force brute : ")
    brute_force(bruteforce)


while True:
    menu_principal()
    choix = input("Entrez le numéro de votre choix (0 pour quitter): ")

    if choix == '1':
        sous_menu_1()
        
    elif choix == '2':
        sous_menu_2()
        
    elif choix == '0':
        print("Vous avez decidé de sortir du logiciel. Au revoir !")
        break
    else:
        print("Choix invalide. Veuillez entrer un numéro valide.")
