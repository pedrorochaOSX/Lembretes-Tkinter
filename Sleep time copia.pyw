import os
import time
from classLembrete import Lembrete
from timeFunctions import getNTPTimeLocal
from tkinter import *


class App:
    def __init__(self):

        self.lista = []
        self.lista_inversa = []
        self.iniciar = 1
        self.codigo_atual = 0
        self.codigo_escolhido = 0
        self.quantidade = 0
  
        try:
            with open('textoLembretes.txt', 'r') as arquivo:
                self.lista = [linha.strip() for linha in arquivo if linha.strip()]
            for i in self.lista:
                self.quantidade += 1
        except FileNotFoundError:
            with open('textoLembretes.txt', 'w+') as arquivo:
                arquivo.writelines('')

                  

        self.textEntry = Entry(window, font='arial 14', fg='white', bg='#24292e',bd=0)
        self.textEntry.place(height=30, width=880, x=10, y=860)


        self.status = self.quantidade

        self.statusMessage = Label(window, text=(f'  LEMBRETES: {self.quantidade}'),anchor='w', background='#121212', font='arial 16', fg='white')
        self.statusMessage.place(height=20, width=900, x=0, y=50)

        self.botaoLembrete = []
        
               

                
        self.botaoAdicionar = Button(window, text="ADICIONAR", background='#24292e',bd=0, font='arial 12', fg='#ffffff', command=self.adicionar)
        self.botaoAdicionar.place(height=30, width=225, x=0, y=0)
        self.changeOnHover(self.botaoAdicionar, '#121212', '#24292e')

        self.botaoEditar = Button(window, text="EDITAR", background='#24292e',bd=0, font='arial 12', fg='#ffffff', command=self.editar)
        self.botaoEditar.place(height=30, width=225, x=225, y=0)
        self.changeOnHover(self.botaoEditar, '#121212', '#24292e')

        self.botaoExcluir = Button(window, text="EXCLUIR", background='#24292e',bd=0, font='arial 12', fg='#ffffff', command=self.excluir)
        self.botaoExcluir.place(height=30, width=225, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#121212', '#24292e')

        self.botaoLimpar = Button(window, text="LIMPAR", background='#24292e',bd=0, font='arial 12', fg='#ffffff', command=self.limpar)
        self.botaoLimpar.place(height=30, width=225, x=675, y=0)
        self.changeOnHover(self.botaoLimpar, '#121212', '#24292e')

        self.botaoEscolhido = 'nada'

    def adicionar_lembrete(self, data: str, info: int):
            novoLembrete = Lembrete(data, info)
            self.lista.append(novoLembrete)    

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))    

    def escolherBotao(self, button_press):
        if (self.botaoEscolhido == self.botaoLembrete[button_press]):
            self.botaoEscolhido.config(fg='white',background='#121212')
            self.changeOnHover(self.botaoEscolhido, '#24292e', '#121212')
                               

        else:            
            self.botaoAntigo = self.botaoEscolhido
            self.botaoEscolhido = self.botaoLembrete[button_press]
            self.botaoEscolhido.config(fg='black',font='arial 15',background='white')
            self.changeOnHover(self.botaoEscolhido, '#24292e', 'white')
            
            self.textEntry.delete(0,END)
            self.textEntry.insert(END,button_press)
            self.botaoAntigo.config(fg='white',background='#121212')
            self.changeOnHover(self.botaoAntigo, '#24292e', '#121212')
            window.update()

    def adicionar(self):
        if (self.textEntry.get().strip() != ''):
            self.info = self.textEntry.get()
            data = getNTPTimeLocal()

            self.adicionar_lembrete(data, self.info)
            print(f'''
    LEMBRETE ADICIONADO: {self.lista[-1]}''')
            self.quantidade += 1
            
            aux = 0

            for i in range(0, self.quantidade-1, 1):
                aux = self.lista[i+1]
                self.lista[i+1] = self.lista[0]
                self.lista[0] = aux

            self.textEntry.delete(0,END)        

            with open('textoLembretes.txt', 'w') as arquivo:
                for i in self.lista:
                    arquivo.writelines("%s\n" % i)   

            if (self.quantidade >= 0):
                posicaoBotao = 80
        
            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(window, text=(f'  {i}'),anchor='w', background='#121212', font='arial 14', fg='white',bd=0, 
                command=lambda m=n: self.escolherBotao(m))
                self.botaoLembrete[n].place(height=30, width=900, x=0, y=posicaoBotao)
                posicaoBotao += 30
                self.changeOnHover(self.botaoLembrete[n], '#24292e', '#121212')

    def editar(self):
        self.textEntry.insert(END, '3')

    def excluir(self):
        self.textEntry.insert(END, '4')

    def limpar(self):
        repetir = 1
        while (repetir == 1):
            os.system('cls')

            self.lista.clear()
            self.quantidade = 0
            print('''LISTA LIMPA''')
            with open('textoLembretes.txt', 'w') as arquivo:
                for i in self.lista:
                    arquivo.writelines("%s\n" % i)  

            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(window, text=(f'  {i}'),anchor='w', background='#121212', font='arial 14', fg='white',bd=0, 
                command=lambda m=n: self.escolherBotao(m))
                self.botaoLembrete[n].place(height=30, width=900, x=0, y=posicaoBotao)
                posicaoBotao += 30
                self.changeOnHover(self.botaoLembrete[n], '#24292e', '#121212')          
        
    def Start(self):   
        if (self.quantidade >= 1):
            posicaoBotao = 80
    
        for n in range(0,self.quantidade,1):
            i = self.lista[n]
            
            self.botaoLembrete.append('')
            self.botaoLembrete[n] = Button(window, text=(f'  {i}'),anchor='w', background='#121212', font='arial 14', fg='white',bd=0, 
            command=lambda m=n: self.escolherBotao(m))
            self.botaoLembrete[n].place(height=30, width=900, x=0, y=posicaoBotao)
            posicaoBotao += 30
            self.changeOnHover(self.botaoLembrete[n], '#24292e', '#121212') 
    
window = Tk()
window.title('Lembretes')
window.configure(background='#121212')
window.resizable(width=False, height=False)
window.minsize(width=900, height=900)

App = App()
App.Start()

window.mainloop()
