from tkinter import *
import tkinter as tk
import random
from model import Parameters
from controller import Controller

class Screen: # Classe qui gère la vue de l'écran #

    def __init__(self): # Initialisation des paramètres et données d'affichage #
        self.titlename = 'Find The Number !'
        self.icon = 'assets/icologo.ico'
        self.bgcolor = '#0168FF'
        self.logotitle = 'assets/logo.png'
        self.ebutton = 'assets/easybutton.png'
        self.hbutton = 'assets/hardbutton.png'
        self.ibutton = 'assets/impossiblebutton.png'
        self.cbutton = 'assets/checkbutton.png'
        self.textlabel = 'assets/textlabel.png'
        self.geometry = '300x400'
        self.fg = 'white'
        self.font = 'Helvetica 10 bold italic'

    def runmenu(self, parameters, gamescreen, controller): # Affichage de l'écran de menu principal #

        menuwindow = Tk()
        menuwindow.title(self.titlename)
        menuwindow.iconbitmap(self.icon)
        menuwindow.config(bg = self.bgcolor)
        menuwindow.geometry(self.geometry)
        menuwindow.maxsize(300,400)
        menuwindow.minsize(300,400)

        logo = PhotoImage(file = self.logotitle)
        window_logo = Label(menuwindow, image = logo, bg = self.bgcolor)
        window_logo.pack()

        easy_button_logo = PhotoImage(file = self.ebutton)
        easy_button = Button(menuwindow, image = easy_button_logo, command = lambda:[parameters.difficultyset(1), parameters.numbertofind(), menuwindow.destroy(), self.rungame(parameters, gamescreen, controller)], bg = self.bgcolor, borderwidth = 0, activebackground = self.bgcolor)
        easy_button.pack()
        easy_button.place(relx=0.5, rely=0.43, anchor=CENTER)

        hard_button_logo = PhotoImage(file = self.hbutton)
        hard_button = Button(menuwindow, image = hard_button_logo, command = lambda:[parameters.difficultyset(2), parameters.numbertofind(), menuwindow.destroy(), self.rungame(parameters, gamescreen, controller)], bg = self.bgcolor, borderwidth = 0, activebackground = self.bgcolor)
        hard_button.pack()
        hard_button.place(relx=0.5, rely=0.63, anchor=CENTER)

        impossible_button_logo = PhotoImage(file = self.ibutton)
        impossible_button = Button(menuwindow, image = impossible_button_logo, command = lambda:[parameters.difficultyset(3), parameters.numbertofind(), menuwindow.destroy(), self.rungame(parameters, gamescreen, controller)], bg = self.bgcolor, borderwidth = 0, activebackground = self.bgcolor)
        impossible_button.pack()
        impossible_button.place(relx=0.5, rely=0.83, anchor=CENTER)

        menuwindow.mainloop()

    def rungame(self, parameters, gamescreen, controller): # Affichage de l'écran de jeu #
        gamewindow = Tk()
        gamewindow.title(self.titlename)
        gamewindow.iconbitmap(self.icon)
        gamewindow.config(bg = self.bgcolor)
        gamewindow.geometry(self.geometry)
        gamewindow.maxsize(300,400)
        gamewindow.minsize(300,400)

        logo = PhotoImage(file = self.logotitle)
        window_logo = Label(gamewindow, image = logo, bg = self.bgcolor)
        window_logo.pack()

        principal_text_img = PhotoImage(file = self.textlabel)
        principal_text = Label(gamewindow, image = principal_text_img, bg = self.bgcolor)
        principal_text.pack()
        principal_text.place(relx=0.5, rely=0.45, anchor=CENTER)

        number_entry = Entry(gamewindow)
        number_entry.pack()
        number_entry.place(relx=0.5, rely=0.55, anchor=CENTER)

        indication_text_var = StringVar()
        indication_text = Label(gamewindow, textvariable = indication_text_var, bg = self.bgcolor, fg = self.fg, font = self.font)
        indication_text.pack()
        indication_text.place(relx=0.5, rely=0.61, anchor=CENTER)

        attempt_text_var = StringVar()
        attempt_text = Label(gamewindow, textvariable = attempt_text_var, bg = self.bgcolor, fg = self.fg, font = self.font)
        attempt_text.pack()
        attempt_text.place(relx=0.5, rely=0.85, anchor=CENTER)

        checkbutton_img = PhotoImage(file = self.cbutton)
        checkbutton = Button(gamewindow, image = checkbutton_img, command = lambda:[controller.justprice(indication_text_var, number_entry, parameters.number_to_find, parameters, checkbutton, gamewindow, gamescreen, controller), controller.attemptsremaining(attempt_text_var, gamewindow, gamescreen, checkbutton, parameters, controller)], bg = self.bgcolor, borderwidth = 0, activebackground = self.bgcolor)
        checkbutton.pack()
        checkbutton.place(relx=0.5, rely=0.72, anchor=CENTER)

        gamewindow.mainloop()