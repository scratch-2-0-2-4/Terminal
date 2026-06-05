import sys
import time

cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "help":
    print("Commandes : help, time, date, IA")
elif cmd == "time":
    print(time.strftime("%H:%M:%S"))
elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))
elif cmd == "IA":
    print("À venir pour bientôt. Promis !")
else:
    print(f"{cmd} est une commande inconnue.")
