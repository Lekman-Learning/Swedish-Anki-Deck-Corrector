"""Starta Anki-Svenska GUI utan konsolfönster."""
import sys
import os

# Sätt working directory till skriptets mapp
os.chdir(os.path.dirname(os.path.abspath(__file__)))

from gui import main
main()
