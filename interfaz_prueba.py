import tkinter
import pprint
#Geometria PAck
window=tkinter.Tk()

#pprint.pprint(dir(window))

label_saludo=tkinter.Label(window,text="Hola!",background="yellow",fg="blue")
label_saludo.pack(ipadx=20,ipady=10,expand=True)#fill='both',x o y

label_saludo=tkinter.Label(window,text="Adios!",background="red",fg="blue")
label_saludo.pack(ipadx=20,ipady=10,side="left",)
window.mainloop()

