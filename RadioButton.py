import tkinter
from tkinter import ttk

#En este ejercicio tenéis que crear una lista de RadioButton que muestre la opción que se ha seleccionado
# y que contenga un botón de reinicio para que deje todo como al principio
#  Al principio no tiene que haber una opción seleccionada.
window=tkinter.Tk()
window.title("Radio Button")


def mifuncion():
    if(seleccionado.get()=='1'):
        print("En serio crees que está Buena,Seleccionaste la opcion 1")
    if (seleccionado.get() == '2'):
        print("En serio crees que está Muy Buena,Seleccionaste la opcion 2")
    if (seleccionado.get() == '3'):
        print("En serio crees que está Excelente,Seleccionaste la opcion 3")


def reiniciar():
    seleccionado.set(None)
    print("Empezamos nuevamente")

def salir():
    window.quit()
    print("Buena tarde!")

seleccionado=tkinter.StringVar()

label_curso=ttk.Label(window,text="Nivel de satisfaccion con el curso de Python")
radio1=ttk.Radiobutton(window,text="Buena",command=mifuncion,variable=seleccionado ,value='1')
radio2=ttk.Radiobutton(window,text="Muy Buena",command=mifuncion,variable=seleccionado,value='2')
radio3=ttk.Radiobutton(window,text="Excelente",command=mifuncion,variable=seleccionado,value='3')
button=ttk.Button(window,text='Reiniciar',command=reiniciar)
button_salir=ttk.Button(window,text='Salir',command=salir)

label_curso.grid(column=1,row=0,sticky=tkinter.E,padx=100,pady=10)
radio1.grid(column=1,row=1,sticky=tkinter.W,padx=100,pady=5)
radio2.grid(column=1,row=2,sticky=tkinter.W,padx=100,pady=5)
radio3.grid(column=1,row=3,sticky=tkinter.W,padx=100,pady=5)
button.grid(column=1,row=5,sticky=tkinter.W,padx=100,pady=5)
button_salir.grid(column=2,row=5,sticky=tkinter.W,padx=10,pady=5)



window.mainloop()