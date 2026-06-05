import json
import time

# Lire la commande depuis command.json
try:
    with open("command.json") as f:
        data = json.load(f)
        cmd = data.get("cmd", "")
except:
    cmd = ""

# Exécuter la commande
if cmd == "help":
    output = "Commandes : help, time"
elif cmd == "time":
    output = time.strftime("%H:%M:%S")
else:
    output = f"{cmd} est une commande inconnue."

# Écrire la réponse dans response.json
with open("response.json", "w") as f:
    json.dump({"output": output}, f)
