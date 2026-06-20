#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""terminal.py — version corrigée pour scratch-2-0-2-4/Terminal-test
Corrige la syntaxe d'origine, ajoute argparse pour la gestion des arguments,
et fournit des alias et des messages en français.
"""
import argparse
import sys
import random
from datetime import datetime

COMMANDS = {
    "help": "Afficher l'aide",
    "time": "Afficher l'heure (HH:MM:SS)",
    "date": "Afficher la date (jj/mm/AAAA)",
    "ia": "Fonction IA (à venir)",
    "random": "Nombre aléatoire entre 1 et 100",
    "idée": "Envoyer une idée",
    "idee": "Envoyer une idée (alias sans accent)",
    "pub": "Contact pour publicité",
    "ad": "Contact pour publicité (alias)",
    "lgdc": "Lien vers le forum LGDC",
    "lgdc-forum": "Lien vers le forum LGDC",
    "forum": "Lien vers le forum LGDC (alias)",
    "example": "Afficher un message d'exemple",
}


def print_help():
    print("Commandes disponibles :")
    for cmd, desc in sorted(COMMANDS.items()):
        print(f"  {cmd:12} - {desc}")


def handle_command(cmd):
    if not cmd:
        print_help()
        return 0

    key = cmd.strip().lower()

    if key in ("help", "h", "--help", "-h"):
        print_help()

    elif key == "time":
        print(datetime.now().strftime("%H:%M:%S"))

    elif key == "date":
        print(datetime.now().strftime("%d/%m/%Y"))

    elif key == "ia":
        print("À venir bientôt. Promis !")

    elif key == "random":
        print(random.randint(1, 100))

    elif key in ("idée", "idee"):
        print(
            "Oh, tu as une idée de commande... Donne-la à @Scratch_2_0_2_4 sur https://scratch.mit.edu/users/Scratch_2_0_2_4/#comments"
        )

    elif key in ("pub", "ad"):
        print(
            "Contactez @Scratch_2_0_2_4 (https://scratch.mit.edu/users/Scratch_2_0_2_4/#comments) pour mettre votre pub ici."
        )

    elif key in ("lgdc", "lgdc-forum", "forum"):
        print("Découvrez LGDC Forum: https://lgdc.flarum.cloud — un forum pour parler de LGDC, Scratch et bien plus !")

    elif key == "example":
        print("Ceci est un exemple de message. Il vous prouve que le terminal fonctionne.")

    else:
        print(f"{cmd} est une commande inconnue.")
        return 2

    return 0


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    parser = argparse.ArgumentParser(
        prog="terminal.py",
        description="Petit terminal de commandes simples (projet Scratch_2_0_2_4)",
        add_help=False,
    )
    parser.add_argument("command", nargs="?", help="Commande à exécuter")
    parser.add_argument("-h", "--help", action="store_true", help="Afficher l'aide")

    args = parser.parse_args(argv)

    if args.help:
        print_help()
        return 0

    cmd = args.command or ""
    return handle_command(cmd)


if __name__ == "__main__":
    raise SystemExit(main())
