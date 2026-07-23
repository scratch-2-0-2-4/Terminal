import sys
import time
import random

version = "1.1"
print(f"Terminal [v. {version}]")
print("Tape 'help' pour une liste des commandes. \n")
cmd = input("Commande >>> ")


if cmd == "help":
    print("Commandes : help, time, date, random, version, exemple, LGDC Forum")

elif cmd == "time":
    print(time.strftime("%H:%M:%S"))

elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))

elif cmd == "random":
    print(random.randint(1, 100))

elif cmd == "LGDC Forum":
    print("Découvrez LGDC Forum ( https://lgdc.flarum.cloud ), un forum pour parler de LGDC, Scratch et bien + encore !")

elif cmd == "exemple":
    print("Ceci est un example de message. Il vous prouve que le terminal fonctionne.")

elif cmd == "version" :
    print(f"[v. {version}]")

else:
    print(f"Erreur 404 : {cmd} est une commande inconnue.")
