from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import random

# Initialisation ChatterBot
bot = ChatBot("SafeBot", logic_adapters=["chatterbot.logic.BestMatch"], read_only=True)

# Chargement des données
def charger_donnees(fichier):
    with open(fichier, 'r', encoding='utf-8') as f:
        lignes = [ligne.strip() for ligne in f if ligne.strip()]
    return lignes

def preparer_paires(lignes):
    if len(lignes) % 2 != 0:
        raise ValueError("Fichier data.txt : nombre impair de lignes.")
    paires = []
    for i in range(0, len(lignes), 2):
        paires.append(lignes[i])
        paires.append(lignes[i + 1])
    return paires

# Entraînement
lignes = charger_donnees("data.txt")
trainer = ListTrainer(bot)
trainer.train(preparer_paires(lignes))

# Données supplémentaires
conseils = [
    "Utilise un mot de passe différent pour chaque site.",
    "Active l’authentification à deux facteurs.",
    "Installe un antivirus fiable et mets-le à jour.",
    "Ne clique jamais sur des pièces jointes inconnues.",
    "Fais des sauvegardes régulières de tes données."
]

quiz = [
    {
        "question": "Quel est le mot de passe le plus sécurisé ?",
        "options": ["A. 123456", "B. motdepasse", "C. T!gR3%v1L@2025"],
        "reponse": "C"
    },
    {
        "question": "Quelle est la première chose à faire après un piratage ?",
        "options": ["A. Changer d'ordinateur", "B. Déconnecter d'Internet", "C. Pleurer"],
        "reponse": "B"
    }
]

urgence = [
    "Déconnecte ton appareil d'Internet.",
    "Change tous tes mots de passe depuis un appareil sûr.",
    "Analyse le système avec un antivirus.",
    "Préviens ton entourage si leurs données sont à risque.",
    "Contacte un expert si nécessaire."
]

# Menu principal
def afficher_menu():
    print("\n🎯 MENU PRINCIPAL")
    print("1. Parler avec SafeBot (chat)")
    print("2. Obtenir un conseil")
    print("3. Lancer un quiz")
    print("4. Mode urgence")
    print("5. Quitter")

def boucle_chat():
    print("\n💬 Tape 'retour' pour revenir au menu.")
    while True:
        msg = input("Vous: ")
        if msg.lower() in ['retour', 'exit', 'quit']:
            break
        print("SafeBot:", bot.get_response(msg))

def donner_conseil():
    print("\n💡 Conseil :", random.choice(conseils))

def lancer_quiz():
    score = 0
    print("\n🧠 Quiz cybersécurité :")
    for q in quiz:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        rep = input("Votre réponse : ").strip().upper()
        if rep == q["reponse"]:
            print("✅ Bonne réponse !")
            score += 1
        else:
            print(f"❌ Mauvaise réponse. C'était {q['reponse']}.")
    print(f"\n🎯 Score final : {score}/{len(quiz)}")

def mode_urgence():
    print("\n🚨 Urgence cybersécurité :")
    for etape in urgence:
        input(f"\n{etape} [Entrée pour continuer]")

# Main
def main():
    print("🔐 SafeBot 2.0 – Assistant cybersécurité intelligent")
    while True:
        afficher_menu()
        choix = input("Choix : ").strip()
        if choix == "1":
            boucle_chat()
        elif choix == "2":
            donner_conseil()
        elif choix == "3":
            lancer_quiz()
        elif choix == "4":
            mode_urgence()
        elif choix == "5":
            print("👋 Merci d’avoir utilisé SafeBot. À bientôt !")
            break
        else:
            print("❌ Choix invalide.")

if __name__ == "__main__":
    main()
