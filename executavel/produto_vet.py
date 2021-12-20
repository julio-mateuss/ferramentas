from tkinter import *
import tkinter as tk
def pv():
    c = ["#32BAB3", "#217A76","#43FAF1", " #151626", "#F2F2F2"]
    app = Tk()
    app.title("produto vetorial")
    app.geometry("320x160")
    app.resizable(width=0, height=0)
    app.configure(background= c[0])

    def calcular():
        a11 = float(a1.get())
        a22 = float(a2.get())
        a33 = float(a3.get())
        b11 = float(b1.get())
        b22 = float(b2.get())
        b33 = float(b3.get())
        a= [ a11, a22, a33]
        b= [b11, b22, b33]
        vet = [(a[1]*b[2]-a[2]*b[1]), (a[2]*b[0]-a[0]*b[2]),(a[0]*b[1]-a[1]*b[0])]
        c = str(vet)
        p.set(c)
        

    p = tk.StringVar()
    p.set(" ... ")
    Label(app, text ="valor para î", background =c[4], foreground = c[1], anchor = W).place(x =10, y =20, width = 100, height = 20)
    a1 = Entry(app)
    a1.place(x=10, y = 40, width = 100, height =20)
    b1 = Entry(app)
    b1.place(x=10, y = 60, width = 100, height =20)


    Label(app, text ="valor para j", background =c[4], foreground = c[1], anchor = W).place(x =110, y =20, width = 100, height = 20)
    a2 = Entry(app)
    a2.place(x=110, y = 40, width = 100, height =20)
    b2 = Entry(app)
    b2.place(x=110, y = 60, width = 100, height =20)



    Label(app, text ="valor para k", background =c[4], foreground = c[1], anchor = W).place(x =210, y =20, width = 100, height = 20)
    a3 = Entry(app)
    a3.place(x=210, y = 40, width = 100, height =20)
    b3 = Entry(app)
    b3.place(x=210, y = 60, width = 100, height =20)

    Label(app, text = "resultado:" , background =c[4], foreground = c[1], anchor = W).place(x =10, y =80, width = 300, height = 20)
    Label(app, textvariable = p , background =c[4], foreground = c[1], anchor = W).place(x =10, y =100, width = 300, height = 20)


    botao = Button(app, height = 20, width = 20, text = "calcular", command = calcular, foreground = c[4], background =c[1])
    botao.place(x=130, y=120, width=60, height = 20)
                


    app.mainloop
