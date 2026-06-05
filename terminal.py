import sys
import time

# Récupérer la commande passée en argument
cmd = sys.argv[1] if len(sys.argv) > 1 else ""

# Exécuter la commande
if cmd == "help":
    print("Commandes : help, time, date")
elif cmd == "time":
    print(time.strftime("%H:%M:%S"))
elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))
else:
    print(f"{cmd} est une commande inconnue.")
