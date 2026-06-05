import sys
import time

# Récupérer la commande passée en argument
cmd = sys.argv[1] if len(sys.argv) > 1 else ""

# Exécuter la commande
if cmd == "help":
    output = "Commandes : help, time"
elif cmd == "time":
    output = time.strftime("%H:%M:%S")
else:
    output = f"{cmd} est une commande inconnue."

# Afficher la réponse (GitHub Actions la récupère)
print(output)
