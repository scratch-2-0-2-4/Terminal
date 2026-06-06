import sys
import time
import random

cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "help":
    print("Commandes : help, time, date, IA, random, idée")

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
   

else:
    print(f"{cmd} est une commande inconnue.")
