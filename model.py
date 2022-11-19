from tkinter import *
import tkinter as tk
import random

class Parameters: # Classe qui gère les paramètres du jeu #

    def __init__(self, difficulty_attempts): # Fonction qui génère le nombre à trouver #
        self.difficulty_attempts = difficulty_attempts

    def numbertofind(self):
        self.number_to_find = random.randint(0, 10000)

    def difficultyset(self, difficulty): # Fonction qui gère le niveau de difficulté #
        difficulty_choice = {1: 20, 2: 10, 3: 5}
        self.difficulty_attempts = difficulty_choice[difficulty]


class Database: # Classe qui gère la base de donnée du jeu (comptes, statistiques) #
    pass #code de gestion de données à mettre en place#


class Backup: # Classe qui gère les sauvegardes du jeu #
    pass #code de sauvegarde à mettre en place#
