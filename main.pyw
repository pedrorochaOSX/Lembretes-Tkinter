import os
from classLembrete import Lembrete
from timeFunctions import getTime
from tkinter import *

class App:
    def __init__(self):

        self.lista = []
        self.iniciar = 1
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
    
    def Start(self):  
        self.textEntry = Text(root, font='arial 14', fg='#dfdfdf', bg='#333333',bd=0,state=NORMAL,wrap='word',padx=20,pady=20,insertbackground= '#dfdfdf')
        scrollbar = Scrollbar(root,orient=VERTICAL,width=20)
        scrollbar.config(command=self.textEntry.yview)
        self.textEntry.config(yscrollcommand=scrollbar.set)
        self.textEntry.place(height=300, width=280, x=15, y=50)
        self.textEntry.focus_set()

        self.statusMessage = Label(root, text=(f'  Lembretes: {self.quantidade}'),anchor='w', background='#202020', font='arial 16 bold', fg='white')
        self.statusMessage.place(height=20, width=600, x=0, y=365)

        self.botaoLembrete = []
                
        self.botaoAdicionar = Button(root, text="Adicionar", background='#202020',bd=0, font='arial 14', fg='#ffffff', command=self.adicionar)
        self.botaoAdicionar.place(height=35, width=150, x=0, y=0)
        self.changeOnHover(self.botaoAdicionar, '#2f2f2f', '#202020')

        self.botaoEditar = Button(root, text="Editar", background='#202020',bd=0, font='arial 14', fg='#ffffff', command=self.editar)
        self.botaoEditar.place(height=35, width=150, x=150, y=0)
        self.changeOnHover(self.botaoEditar, '#2f2f2f', '#202020')

        self.botaoExcluir = Button(root, text="Excluir", background='#202020',bd=0, font='arial 14', fg='#ffffff', command=self.excluir)
        self.botaoExcluir.place(height=35, width=150, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#2f2f2f', '#202020')

        self.botaoLimpar = Button(root, text="Limpar", background='#202020',bd=0, font='arial 14', fg='#ffffff', command=self.limpar)
        self.botaoLimpar.place(height=35, width=150, x=300, y=0)
        self.changeOnHover(self.botaoLimpar, '#2f2f2f', '#202020')

        self.botaoEscolhido = 'nada'
        self.botaoAntigo = 'nada'
        self.quantidadeAntiga = 'nada'

        if (self.quantidade > 5):
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0, 0,self.quantidade*42))
            scrollbar = Scrollbar(self.canvas,orient=VERTICAL,width=20)
            scrollbar.pack(fill=Y,side=RIGHT)
            scrollbar.config(command=self.canvas.yview)
            self.canvas.config(yscrollcommand=scrollbar.set)

            posicaoBotao = 0
            
            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                command=lambda m=n: self.escolherBotao(m))
                self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=580,height=37)
                posicaoBotao += 42
                self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

            self.canvas.place(height=210,width=600,x=0,y=390)    

        else:
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
        
            if (self.quantidade >= 1):
                posicaoBotao = 0
            
                for n in range(0,self.quantidade,1):
                    i = self.lista[n]
                    
                    self.botaoLembrete.append('')
                    self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                    command=lambda m=n: self.escolherBotao(m))
                    self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=600,height=37)
                    posicaoBotao += 42
                    self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

                self.canvas.place(height=210,width=600,x=0,y=390)   

        root.bind('<Control-Return>', self.adicionar)  

    def escolherBotao(self, button_press):
        self.botaoEscolhido = self.botaoLembrete[button_press]


        if (self.botaoAntigo == self.botaoEscolhido):
            self.botaoEscolhido.config(font='arial 14',fg='white',background='#333333')
            self.changeOnHover(self.botaoEscolhido, '#414141', '#333333')
            self.botaoAntigo = 'nada'
            self.textShow.destroy()

        else:   
            self.botaoEscolhido.config(fg='black',font='arial 14',background='white')
            self.changeOnHover(self.botaoEscolhido, '#333333', 'white')
            
            if (self.botaoAntigo != 'nada'):
                self.botaoAntigo.config(font='arial 14',fg='white',background='#333333')
                self.changeOnHover(self.botaoAntigo, '#414141', '#333333')
                self.botaoAntigo = self.botaoEscolhido
                
                self.textShow.config(state=NORMAL)
                self.textShow.delete(1.0, END)
                self.textShow.insert(END, str(self.lista[button_press]).replace('   ','\n'))
                self.textShow.config(state=DISABLED)

            else: 
                self.textShow = Text(root, font='arial 14', fg='white', bg='black',bd=0,state=NORMAL,wrap='word',padx=20,pady=20)
                scrollbar = Scrollbar(root,orient=VERTICAL,width=20)
                scrollbar.config(command=self.textShow.yview)
                self.textShow.config(yscrollcommand=scrollbar.set)
                self.textShow.place(height=300, width=280, x=305, y=50)
                self.textShow.delete('1.0', END)
                self.textShow.insert(END, str(self.lista[button_press]).replace('   ','\n'))
                self.textShow.config(state=DISABLED)
                
                self.botaoAntigo = self.botaoEscolhido

    def adicionar(self, event=None):
        if (self.textEntry.get('1.0','end-1c').strip() != ''):
            self.info = self.textEntry.get('1.0',"end-1c")
            self.info = self.info.replace('\n','   ')

            data = getTime()

            self.adicionar_lembrete(data, self.info)
            print(f'''
LEMBRETE ADICIONADO: {self.lista[-1]}''')
            self.quantidade += 1
            
            aux = 0

            for i in range(0, self.quantidade-1, 1):
                aux = self.lista[i+1]
                self.lista[i+1] = self.lista[0]
                self.lista[0] = aux

            with open('textoLembretes.txt', 'w') as arquivo:
                for i in self.lista:
                    arquivo.writelines("%s\n" % i)

            self.botaoAntigo = 'nada' 

            try:
                self.textShow.destroy()

            except AttributeError:
                print('No textShow') 
                
            self.textEntry.delete('1.0', END)          

            self.restart_botaoEditar()
            self.restart_botaoExcluir()
            self.restart_canvas()
            self.restart_statusMessage()

    def editar(self):
        self.botaoAntigo = 'nada'

        try:
            self.textShow.destroy()

        except AttributeError:
            print('No textShow')    

        self.textEntry.delete('1.0',END)

        self.restart_botaoExcluir()
        self.restart_statusMessage()

        self.botaoEditar.destroy()
        self.botaoEditar = Button(root, text="Editar", background='#202020',bd=0, font='arial 14', fg='#909090', 
        command=lambda:[self.restart_statusMessage(), self.restart_botaoEditar(),self.restart_canvas()])
        self.botaoEditar.place(height=35, width=150, x=150, y=0)
        self.changeOnHover(self.botaoEditar, '#2f2f2f', '#202020') 

        self.botaoLembrete = []
        self.canvas.destroy()

        if (self.quantidade > 5):
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
            scrollbar = Scrollbar(self.canvas,orient=VERTICAL,width=20)
            scrollbar.pack(fill=Y,side=RIGHT)
            scrollbar.config(command=self.canvas.yview)
            self.canvas.config(yscrollcommand=scrollbar.set)

            posicaoBotao = 0
        
            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                command=lambda m=n: self.editarBotao(m))
                self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=580,height=37)
                posicaoBotao += 42
                self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

            self.canvas.place(height=210,width=600,x=0,y=390)

        else:
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
        
            if (self.quantidade >= 1):
                posicaoBotao = 0
            
                for n in range(0,self.quantidade,1):
                    i = self.lista[n]
                    
                    self.botaoLembrete.append('')
                    self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                    command=lambda m=n: self.editarBotao(m))
                    self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=600,height=37)
                    posicaoBotao += 42
                    self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

                self.canvas.place(height=210,width=600,x=0,y=390)  

    def editarBotao(self,button_press):
        if (self.textEntry.get('1.0','end-1c').strip() != ''):
            del self.lista[button_press]
            self.quantidade -= 1
        
            self.info = self.textEntry.get('1.0', 'end-1c')
            
            self.info = self.info.replace('\n','   ')
            
            data = getTime()

            self.adicionar_lembrete(data, self.info)
            print(f'''
LEMBRETE ADICIONADO: {self.lista[-1]}''')
            self.quantidade += 1
            
            aux = 0

            for i in range(0, self.quantidade-1, 1):
                aux = self.lista[i+1]
                self.lista[i+1] = self.lista[0]
                self.lista[0] = aux

            with open('textoLembretes.txt', 'w') as arquivo:
                for i in self.lista:
                    arquivo.writelines("%s\n" % i)

            print(self.lista)            

            self.editar()

    def excluir(self):
        self.restart_botaoEditar()

        self.botaoAntigo = 'nada'

        try:
            self.textShow.destroy()

        except AttributeError:
            print('No textShow')

        self.textEntry.delete(1.0,END)

        self.restart_botaoEditar()
        self.restart_statusMessage()
       
        self.botaoExcluir.destroy()        
        self.botaoExcluir = Button(root, text="Excluir", background='#202020',bd=0, font='arial 14', fg='#909090',
        command=lambda:[self.restart_statusMessage(), self.restart_botaoExcluir(),self.restart_canvas()])
        self.botaoExcluir.place(height=35, width=150, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#2f2f2f', '#202020')

        self.botaoLembrete = []
        self.canvas.destroy()

        if (self.quantidade > 5):
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
            scrollbar = Scrollbar(self.canvas,orient=VERTICAL,width=20)
            scrollbar.pack(fill=Y,side=RIGHT)
            scrollbar.config(command=self.canvas.yview)
            self.canvas.config(yscrollcommand=scrollbar.set)

            posicaoBotao = 0
            
            for n in range(0,self.quantidade,1):
                i = self.lista[n]
                
                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                command=lambda m=n: self.excluirBotao(m))
                self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=580,height=37)
                posicaoBotao += 42
                self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

            self.canvas.place(height=210,width=600,x=0,y=390)    

        else:
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
        
            if (self.quantidade >= 1):
                posicaoBotao = 0
            
                for n in range(0,self.quantidade,1):
                    i = self.lista[n]
                    
                    self.botaoLembrete.append('')
                    self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                    command=lambda m=n: self.excluirBotao(m))
                    self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=600,height=37)
                    posicaoBotao += 42
                    self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

                self.canvas.place(height=210,width=600,x=0,y=390)
                
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
        self.clearConfirmBackground = Frame(root, background='#202020')
        self.clearConfirmBackground.place(height=600, width=600, x=0, y=0)

        self.clearConfirmationText = Label(root, text='LIMPAR TUDO?',anchor='c', background='#202020', font='arial 18', fg='white')
        self.clearConfirmationText.place(height=20, width=600, x=0, y=200)

        self.botaoClearConfirm = Button(root, text="SIM", background='#2f2f2f',bd=0, font='arial 16', fg='#ffffff', command=self.clearConfirm)
        self.botaoClearConfirm.place(height=100, width=150, x=135, y=250)

        self.botaoClearCancel = Button(root, text="CANCELAR", background='#2f2f2f',bd=0, font='arial 16', fg='#ffffff', command=self.clearCancel)
        self.botaoClearCancel.place(height=100, width=150, x=315, y=250)

    def clearConfirm(self):
        self.lista.clear()
        print('''LISTA LIMPA''')
        with open('textoLembretes.txt', 'w') as arquivo:
            for i in self.lista:
                arquivo.writelines("%s\n" % i)
        self.quantidade = 0
        try:
            self.textShow.destroy()
        except AttributeError:
            print('No textShow')
        self.clearConfirmBackground.destroy()
        self.clearConfirmationText.destroy()
        self.botaoClearConfirm.destroy()
        self.botaoClearCancel.destroy()
        self.restart_botaoEditar()
        self.restart_botaoExcluir()

        self.restart_botaoEditar()
        self.restart_botaoExcluir()
        self.restart_canvas()
        self.restart_statusMessage()
        
    def clearCancel(self):
        self.clearConfirmBackground.destroy()
        self.clearConfirmationText.destroy()
        self.botaoClearConfirm.destroy()
        self.botaoClearCancel.destroy()
        self.restart_botaoEditar()
        self.restart_botaoExcluir()

        try:
            self.textShow.destroy()
            self.botaoAntigo = 'nada'
        except AttributeError:
            self.botaoAntigo = 'nada'

        self.restart_botaoEditar()
        self.restart_botaoExcluir()
        self.restart_canvas()
        self.restart_statusMessage()
        
    def restart_statusMessage(self): 
        self.statusMessage.destroy()   
        self.statusMessage = Label(root, text=(f'  Lembretes: {self.quantidade}'),anchor='w', background='#202020', font='arial 16 bold', fg='white')
        self.statusMessage.place(height=20, width=600, x=0, y=365)

    def restart_botaoEditar(self):
        self.botaoEditar.destroy()
        self.botaoEditar = Button(root, text="Editar", background='#202020',bd=0, font='arial 14', fg='white', command=self.editar)
        self.botaoEditar.place(height=35, width=150, x=150, y=0)
        self.changeOnHover(self.botaoEditar, '#2f2f2f', '#202020')

    def restart_botaoExcluir(self):
        self.botaoExcluir.destroy()
        self.botaoExcluir = Button(root, text="Excluir", background='#202020',bd=0, font='arial 14', fg='white', command=self.excluir)
        self.botaoExcluir.place(height=35, width=150, x=450, y=0)
        self.changeOnHover(self.botaoExcluir, '#2f2f2f', '#202020')

    def restart_canvas(self):    
        self.canvas.destroy()
        self.botaoLembrete = []

        if (self.quantidade > 5):
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
            scrollbar = Scrollbar(self.canvas,orient=VERTICAL,width=20)
            scrollbar.pack(fill=Y,side=RIGHT)
            scrollbar.config(command=self.canvas.yview)
            self.canvas.config(yscrollcommand=scrollbar.set)

            posicaoBotao = 0
            
            for n in range(0,self.quantidade,1):
                i = self.lista[n]

                self.botaoLembrete.append('')
                self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                command=lambda m=n: self.escolherBotao(m))
                self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=580,height=37)
                posicaoBotao += 42
                self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

            self.canvas.place(height=210,width=600,x=0,y=390)    

        else:
            self.canvas = Canvas(root,background='#202020',highlightthickness=0, scrollregion=(0,0,0,self.quantidade*42))
        
            if (self.quantidade >= 1):
                posicaoBotao = 0
            
                for n in range(0,self.quantidade,1):
                    i = self.lista[n]

                    self.botaoLembrete.append('')
                    self.botaoLembrete[n] = Button(self.canvas, text=(f'  {i}'),anchor='w', background='#333333', font='arial 14', fg='#eeeeee',bd=0,
                    command=lambda m=n: self.escolherBotao(m))
                    self.canvas.create_window((0, posicaoBotao), window=self.botaoLembrete[n], anchor=N+W,width=600,height=37)
                    posicaoBotao += 42
                    self.changeOnHover(self.botaoLembrete[n], '#414141', '#333333')

            self.canvas.place(height=210,width=600,x=0,y=390)

root = Tk()
root.title('Lembretes')
root.configure(background='#202020')
root.resizable(width=False, height=False)
root.minsize(width=600, height=600)
root.iconbitmap('Lembretes-tk.ico')

app = App()
app.Start()

root.mainloop()