import random
import tkinter
from tkinter import ttk

window=tkinter.Tk()

label1=tkinter.Label(window,text="Pos Abspluta",background='blue',fg="white")
label1.place(x=10,y=20)

label2=tkinter.Label(window,text="Otro",background='yellow',fg="green")
label2.place(x=15,y=50)

colors=['blue','red','yellow','pink','black','white','green']
for i in range(0,10):
    color1=random.randint(0,len(colors)-1)
    color2=random.randint(0,len(colors)-1)
    label=tkinter.Label(window,text="etiwueta ramdom",background=colors[color1],fg=colors[color2])
    label.place(x=random.randint(0,100),y=random.randint(0,100))

window.mainloop()