import numpy as np
import tkinter as tk
from tkinter import *

def conversor():
    c = ["#32BAB3", "#217A76","#43FAF1", " #151626", "#F2F2F2"]
    app = Tk()
    app.geometry("270x130")
    app.resizable(width=0, height=0)
    app.configure(background= c[0])
    app.title("conversor polar")


    cov = 180/np.pi
    def polar(a):
        arco = (np.angle(a))*cov
        b = np.real(a)
        c = np.imag(a)
        r = (b**2 + c**2)**0.5
        return r , arco

    def calc():
        a = complex(a1.get())
        r, arco = polar(a)
        r = round(r)
        arco = round(arco)
        r= str(r)
        arco = str(arco)
        va_re = "raio: " + r + "    angulo(graus): " +arco
        result.set(va_re)
        
    result = tk.StringVar()
    result.set("...")

    L = Label(app, text = "numero complexo (x+yj) sem espaços",  background =c[4], foreground = c[1], anchor = W).place(x =10, y =20, width = 250, height = 20)
    a1 = Entry(app)
    a1.place(x=10, y = 40, width = 250, height =20)

    L1 = Label(app, text = "resultado:",  background =c[4], foreground = c[1], anchor = W).place(x =10, y =60, width = 250, height = 20)
    L2 = Label(app, textvariable = result,  background =c[4], foreground = c[1], anchor = W).place(x =10, y =80, width = 250, height = 20)

    botao = Button(app, height = 20, width = 20, text = "calcular", command = calc, foreground = c[4], background =c[1])
    botao.place(x=100, y=100, width=60, height = 20)
                    


    app.mainloop()
