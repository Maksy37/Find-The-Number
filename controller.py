from tkinter import *
import tkinter as tk


class Controller:  # Classe qui gère les actions effectué par l'utilisateur entre model.py et view.py #
    def returnmenu(self, checkbutton, gamewindow, gamescreen, parameters, controller):
        checkbutton_img = PhotoImage(file="assets/returnmenu.png")
        checkbutton.configure(image=checkbutton_img)
        checkbutton.photo = checkbutton_img
        checkbutton.configure(
            command=lambda: [
                gamewindow.destroy(),
                gamescreen.runmenu(parameters, gamescreen, controller),
            ]
        )

    def attemptsremaining(
        self,
        attempt_text_var,
        gamewindow,
        gamescreen,
        checkbutton,
        parameters,
        controller,
    ):  # Fonction qui gère le nombre de tentatives restantes #
        parameters.difficulty_attempts -= 1
        if parameters.difficulty_attempts > 0:
            attempt_text_var.set(
                f"Attempts remaining : {parameters.difficulty_attempts}"
            )
        elif parameters.difficulty_attempts == 0:
            attempt_text_var.set("GAME OVER !")
            self.returnmenu(checkbutton, gamewindow, gamescreen, parameters, controller)

    def justprice(
        self,
        indication_text_var,
        number_entry,
        number_to_find,
        parameters,
        checkbutton,
        gamewindow,
        gamescreen,
        controller,
    ):  # Fonction qui gère les indications au joueur sur le montant à trouver #
        try:
            if int(number_entry.get()) == number_to_find:
                indication_text_var.set(
                    "Congratulations ! You found the right amount !"
                )
                self.returnmenu(
                    checkbutton, gamewindow, gamescreen, parameters, controller
                )
            elif int(number_entry.get()) > number_to_find:
                indication_text_var.set("The amount to be found is lower")
            elif int(number_entry.get()) < number_to_find:
                indication_text_var.set("The amount to be found is greater")
        except ValueError:
            indication_text_var.set("Please enter a number")
