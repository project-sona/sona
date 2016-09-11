from .database import *
from sys import argv

CARDS = []
DECKS = []

def main():
    global CARDS, DECKS

    carddir = argv[1] # TODO
    CARDS = getcards(carddir)
