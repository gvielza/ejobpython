#En este segundo ejercicio, tendréis que crear una interfaz sencilla la cual debe de contener
# una lista de elementos seleccionables, también debe de tener un label con el texto que queráis.
import tkinter
from tkinter import ttk
window=tkinter.Tk()
window.geometry("250x250")


def funcion():
    print("Muy bien")
    window.title("Lindo país!")

lista=['Argentina','España','EEUU','Cuba','Canada','Brazil','Nueva Zelanda']
lista_paises=tkinter.StringVar(value=lista)
label=tkinter.Label(text="Escoge tu país natal")
list_box=tkinter.Listbox(window,height=10,listvariable=lista_paises)
boton=tkinter.Button(text="Aceptar",command=funcion,background="cyan")

label.grid(column=0,row=0,padx=50,pady=5)
list_box.grid(column=0,row=1)
boton.grid(column=0,row=2)


window.mainloop()
