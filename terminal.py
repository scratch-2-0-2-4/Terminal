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

elif cmd == "IA":
    print("À venir pour bientôt. Promis !")

elif cmd == "random":
    print(random.randint(1, 100))

elif cmd == "idée":
    print("Oh, tu as une idée de commande... Donne la à [@Scratch_2_0_2_4](https://scratch.mit.edu/users/Scratch_2_0_2_4/#comments)")

elif cmd == "pub" or cmd == "ad":
    print("Contactez [@Scratch_2_0_2_4](https://scratch.mit.edu/users/Scratch_2_0_2_4/#comments) pour mettre votre pub ici.")

elif cmd == "LGDC Forum":
    print("Découvrez [LGDC Forum](https://lgdc.flarum.cloud), un forum pour parler de LGDC, Scratch et bien + encore !")

elif cmd == "example":
    print("Ceci est un example de message. Il vous prouve que le terminal fonctionne.")

else:
    print(f"{cmd} est une commande inconnue.")
