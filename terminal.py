import sys
import time
import random

cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "help":
    print("Commandes : help, time, date, IA, random")

elif cmd == "time":
    print(time.strftime("%H:%M:%S"))

elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))

elif cmd == "IA":
    print("À venir pour bientôt. Promis !")

elif cmd == "random":
    print(random.randint(1, 100))

elif cmd == "scratch_2_0_2_4" or cmd == "Scratch_2_0_2_4"
   print("[Scratch_2_0_2_4](https://scratch.mit.edu/users/Scratch_2_0_2_4/) est le scratcheur qui à crée ce terminal.

else:
    print(f"{cmd} est une commande inconnue.")
