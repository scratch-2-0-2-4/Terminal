import sys
import time

cmd = sys.argv[1] if len(sys.argv) > 1 else ""

if cmd == "help":
    print("Commandes : help, time, date")
elif cmd == "time":
    print(time.strftime("%H:%M:%S"))
elif cmd == "date":
    print(time.strftime("%d/%m/%Y"))
else:
    print(f"{cmd} est une commande inconnue.")
