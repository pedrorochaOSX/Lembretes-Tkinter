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

    def adicionar_lembrete(self, data: str, info: int):
            novoLembrete = Lembrete(data, info)
            self.lista.append(novoLembrete)    

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))    

    def escolherBotao(self, button_press):
        self.botaoEscolhido = self.botaoLembrete[button_press]
        self.textShow.config(state=NORMAL)
        self.textShow.delete(1.0, END)
        self.textShow.insert(END, self.lista[button_press])
        self.textShow.config(state=DISABLED)

        if (self.botaoAntigo == self.botaoEscolhido):
            self.botaoEscolhido.config(font='arial 14',fg='white',background='#121212')
            self.changeOnHover(self.botaoEscolhido, '#24292e', '#121212')
            self.botaoAntigo = 'nada'

        else:    
            self.botaoEscolhido.config(fg='black',font='arial 15',background='white')
            self.changeOnHover(self.botaoEscolhido, '#24292e', 'white')
            if (self.botaoAntigo != 'nada'):
                self.botaoAntigo.config(font='arial 14',fg='white',background='#121212')
                self.changeOnHover(self.botaoAntigo, '#24292e', '#121212')
                self.botaoAntigo = self.botaoEscolhido

            else: 
                self.botaoAntigo = self.botaoEscolhido

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

            self.statusMessage.destroy()
            self.statusMessage = Label(window, text=(f'  LEMBRETES: {self.quantidade}'),anchor='w', background='#121212', font='arial 16', fg='white')
            self.statusMessage.place(height=20, width=900, x=0, y=85)          

            for n in range(0,self.quantidade-1,1):
                self.botaoLembrete[n].destroy()

            self.botaoAdicionar.destroy()
            self.botaoEditar.destroy()
            self.botaoExcluir.destroy()
            self.botaoLimpar.destroy()
            self.textEntry.destroy()
            self.textShow.destroy()

            self.Start()

    def editar(self):
        self.textShow.config(state=NORMAL)
        self.textShow.delete(1.0, END)
        self.textShow.config(state=DISABLED)
        for n in range(0,self.quantidade,1):
            self.botaoLembrete[n].destroy()

        if (self.quantidade >= 0):
            posicaoBotao = 120

            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(window, text=(f'  {i}'),anchor='w', background='#121212', font='arial 14', fg='white',bd=0, 
                command=lambda m=n: self.editarBotao(m))
                self.botaoLembrete[n].place(height=30, width=900, x=0, y=posicaoBotao)
                posicaoBotao += 30
                self.changeOnHover(self.botaoLembrete[n], '#24292e', '#121212')

        self.botaoExcluir.destroy()
        self.botaoExcluir = Button(window, text="Excluir", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.excluir)
        self.botaoExcluir.place(height=35, width=225, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#2e3338', '#24292e')

        self.botaoEditar.destroy()
        self.botaoEditar = Button(window, text="Editar", background='#121212',bd=0, font='arial 14', fg='#ffffff', 
        command=lambda:[self.destruirBotoes(), self.Start()])
        self.botaoEditar.place(height=35, width=225, x=225, y=0)
        self.changeOnHover(self.botaoEditar, '#191919', '#121212')   

        self.statusMessage.destroy()
        self.statusMessage = Label(window, text=(f'  LEMBRETES: {self.quantidade}'),anchor='w', background='#121212', font='arial 16', fg='white')
        self.statusMessage.place(height=20, width=900, x=0, y=85)     

    def editarBotao(self,button_press):
        if (self.textEntry.get().strip() != ''):
            del self.lista[button_press]
            self.quantidade -= 1

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

            print(self.lista)            

            self.editar()

    def excluir(self):
        self.textShow.config(state=NORMAL)
        self.textShow.delete(1.0, END)
        self.textShow.config(state=DISABLED)        
        if (self.quantidadeAntiga != 'nada'):
            for n in range(0,self.quantidadeAntiga,1):
                    self.botaoLembrete[n].destroy()
        else:
            for n in range(0,self.quantidade,1):
                    self.botaoLembrete[n].destroy()
        if (self.quantidade >= 0):
            posicaoBotao = 120

            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(window, text=(f'  {i}'),anchor='w', background='#121212', font='arial 14', fg='white',bd=0, 
                command=lambda m=n: self.excluirBotao(m))
                self.botaoLembrete[n].place(height=30, width=900, x=0, y=posicaoBotao)
                posicaoBotao += 30
                self.changeOnHover(self.botaoLembrete[n], '#24292e', '#121212')
        
        self.botaoEditar.destroy()
        self.botaoEditar = Button(window, text="Editar", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.editar)
        self.botaoEditar.place(height=35, width=225, x=225, y=0)
        self.changeOnHover(self.botaoEditar, '#2e3338', '#24292e')
        
        self.botaoExcluir.destroy()        
        self.botaoExcluir = Button(window, text="Excluir", background='#121212',bd=0, font='arial 14', fg='#ffffff',
         command=lambda:[self.destruirBotoes(), self.Start()])
        self.botaoExcluir.place(height=35, width=225, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#191919', '#121212')

        self.statusMessage.destroy()
        self.statusMessage = Label(window, text=(f'  LEMBRETES: {self.quantidade}'),anchor='w', background='#121212', font='arial 16', fg='white')
        self.statusMessage.place(height=20, width=900, x=0, y=85)
                
    def excluirBotao(self,button_press):
        if (self.quantidade > 0):
            del self.lista[button_press]
            self.quantidadeAntiga = self.quantidade
            self.quantidade -= 1
            with open('textoLembretes.txt', 'w') as arquivo:
                    for i in self.lista:
                        arquivo.writelines("%s\n" % i)
            self.excluir()

    def limpar(self):
        os.system('cls')

        self.lista.clear()
        print('''LISTA LIMPA''')

        self.destruirBotoes()

        with open('textoLembretes.txt', 'w') as arquivo:
            for i in self.lista:
                arquivo.writelines("%s\n" % i)

        self.quantidade = 0
        
        self.destruirBotoes()
        self.Start() 

    def destruirBotoes(self):       
        if (self.quantidade >= 1 ):    
            for n in range(0, self.quantidade, 1):
                self.botaoLembrete[n].destroy()

        self.botaoExcluir.destroy()
        self.botaoAdicionar.destroy() 
        self.botaoEditar.destroy()  
        self.botaoLimpar.destroy() 
        self.statusMessage.destroy() 
        self.textEntry.destroy() 
        self.textShow.destroy()  

    def Start(self):  
        self.textEntry = Entry(window, font='arial 14', fg='white', bg='#24292e',bd=0)
        self.textEntry.place(height=30, width=880, x=10, y=45)
        self.textEntry.focus_set()

        self.textShow = Text(window, font='arial 14', fg='white', bg='black',bd=0,state=DISABLED,wrap='word')
        self.textShow.place(height=90, width=880, x=10, y=800)

        self.statusMessage = Label(window, text=(f'  LEMBRETES: {self.quantidade}'),anchor='w', background='#121212', font='arial 16', fg='white')
        self.statusMessage.place(height=20, width=900, x=0, y=85)

        self.botaoLembrete = []
                
        self.botaoAdicionar = Button(window, text="Adicionar", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.adicionar)
        self.botaoAdicionar.place(height=35, width=225, x=0, y=0)
        self.changeOnHover(self.botaoAdicionar, '#2e3338', '#24292e')

        self.botaoEditar = Button(window, text="Editar", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.editar)
        self.botaoEditar.place(height=35, width=225, x=225, y=0)
        self.changeOnHover(self.botaoEditar, '#2e3338', '#24292e')

        self.botaoExcluir = Button(window, text="Excluir", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.excluir)
        self.botaoExcluir.place(height=35, width=225, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#2e3338', '#24292e')

        self.botaoLimpar = Button(window, text="Limpar", background='#24292e',bd=0, font='arial 14', fg='#ffffff', command=self.limpar)
        self.botaoLimpar.place(height=35, width=225, x=675, y=0)
        self.changeOnHover(self.botaoLimpar, '#2e3338', '#24292e')

        self.botaoEscolhido = 'nada'
        self.botaoAntigo = 'nada'
        self.quantidadeAntiga = 'nada'


        if (self.quantidade >= 1):
            posicaoBotao = 120
        
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

app = App()
app.Start()

window.mainloop()