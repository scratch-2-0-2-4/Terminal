import sys
import time
import random

cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "help":
    print("Commandes : help, time, date, IA, random, idée, pub (=ad), LGDC Forum")

elif cmd == "time":
    print(time.strftime("%H:%M:%S"))

elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))

elif cmd == "random":
    print(random.randint(1, 100))

elif cmd == "LGDC Forum":
    print("Découvrez LGDC Forum ( https://lgdc.flarum.cloud ), un forum pour parler de LGDC, Scratch et bien + encore !")

elif cmd == "example":
    print("Ceci est un example de message. Il vous prouve que le terminal fonctionne.")

else:
    print(f"**Erreur 404 :** {cmd} est une commande inconnue.")
