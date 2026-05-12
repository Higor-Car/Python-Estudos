from tkinter import *

janela = Tk()

janela.geometry("900x600")

janela.title("Calculadora")

numeroUm = Entry(font="Arial 26")
numeroUm.grid(row=1, column=1, sticky="W")

numeroDois = Entry(font="Arial 26")
numeroDois.grid(row=1, column=2, sticky="W")

def calcularMais():
    total = float(numeroUm.get()) + float(numeroDois.get())
    labelTotal.config(text = total)

botaoMais = Button(janela, text="+", font="Arial 20", command=calcularMais)
botaoMais.grid(row=2, column=0)

def calcularMenos():
    total = float(numeroUm.get()) - float(numeroDois.get())
    labelTotal.config(text = total)

botaoMenos = Button(janela, text="-", font="Arial 20", command=calcularMenos)
botaoMenos.grid(row=2, column=1)

def calcularVezes():
    total = float(numeroUm.get()) * float(numeroDois.get())
    labelTotal.config(text = total)

botaoVezes = Button(janela, text="*", font="Arial 20", command=calcularVezes)
botaoVezes.grid(row=2, column=2)

def calcularDivisao():
    if(numeroDois.get()=="0"):
        labelTotal.config(text="Erro: Divisão por zero")
        return
    else:
        total = float(numeroUm.get()) / float(numeroDois.get())
        labelTotal.config(text = total)

botaoDivisao = Button(janela, text="/", font="Arial 20", command=calcularDivisao)
botaoDivisao.grid(row=2,column=3)

labelTotal = Label(janela, text="0", font="Arial 26")
labelTotal.grid(row=3, column=1)

janela.mainloop()
