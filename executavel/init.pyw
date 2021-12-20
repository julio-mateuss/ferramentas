import tkinter as tk
from tkinter import *
import produto_vet as me
import conversor_polar_rect as conv
app = Tk()
app.geometry("300x300")
app.title("ferramentas")


    

botao = Button(app, text = "produto vetorial", width= 100, height = 20, command = me.pv)
botao.place(x=10, y=10, width=100, height = 20)

botao2 = Button(app, text = "conversor polar", width= 100, height = 20, command = conv.conversor)
botao2.place(x=10, y=30, width=100, height = 20)
app.mainloop()
