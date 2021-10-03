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

        def adicionar_lembrete(data: str, info: int):
            novoLembrete = Lembrete(data, info)
            self.lista.append(novoLembrete)

           

        self.textEntry = Entry(window, font='arial 14', fg='white', bg='black')
        self.textEntry.place(height=30, width=500, x=50, y=680)

        self.status = self.quantidade

        self.statusMessage = Label(window, text=(f'LEMBRETES: {self.quantidade}'), background='#121212', font='arial 16', fg='white')
        self.statusMessage.place(height=20, width=600, x=0, y=20)

        self.botaoLembrete = []
        
               

                
        self.botaoAdicionar = Button(window, text="ADICIONAR", background='grey', font='arial 11 bold', fg='#ffffff', command=self.adicionar)
        self.botaoAdicionar.place(height=40, width=600, x=0, y=720)

        self.botaoEditar = Button(window, text="EDITAR", background='grey', font='arial 11 bold', fg='#ffffff', command=self.editar)
        self.botaoEditar.place(height=40, width=200, x=0, y=760)

        self.botaoExcluir = Button(window, text="EXCLUIR", background='grey', font='arial 11 bold', fg='#ffffff', command=self.excluir)
        self.botaoExcluir.place(height=40, width=200, x=200, y=760)

        self.botaoLimpar = Button(window, text="LIMPAR", background='grey', font='arial 11 bold', fg='#ffffff', command=self.limpar)
        self.botaoLimpar.place(height=40, width=200, x=400, y=760)

    def changeOnHover(self, button, colorOnHover, colorOnLeave):
        button.bind("<Enter>", func=lambda e: button.config(background=colorOnHover))
        button.bind("<Leave>", func=lambda e: button.config(background=colorOnLeave))    

    def which_button(self,button_press:int):
        print(button_press,' deletado')
        del self.lista[button_press]
        window.update()

    def Start(self):   
        if (self.quantidade >= 1):
            posicaoBotao = 60
    
        for n in range(0,self.quantidade,1):
            i = self.lista[n]
            
            self.botaoLembrete.append('')
            self.botaoLembrete[n] = Button(window, text=i, background='black', font='arial 12', fg='#ffffff',bd=0, 
            command=lambda m=n: self.which_button(m))
            self.botaoLembrete[n].place(height=40, width=600, x=0, y=posicaoBotao)
            posicaoBotao += 40
            self.changeOnHover(self.botaoLembrete[n], '#24292e', 'black') 

    def adicionar(self):
        self.textEntry.insert(END, '2')

    def editar(self):
        self.textEntry.insert(END, '3')

    def excluir(self):
        self.textEntry.insert(END, '4')

    def limpar(self):
        self.textEntry.insert(END, '5')

  


    
    

    def Countdown(self):

        while(self.fullTime > 0):
            self.status = ('%.2d:%.2d:%.2d' %
                           (self.timeHour, self.timeMin, self.timeSec))

            self.statusMessage.destroy()
            self.statusMessage = Label(window, text=('''
  %s''' % (self.status)), background='#121212', font='arial 16', fg='#c72344')
            self.statusMessage.pack()

            window.update()

            time.sleep(1)

            if(self.timeSec >= 0):
                self.timeSec -= 1

            if(self.timeSec < 0 and self.timeMin > 0):
                self.timeMin -= 1
                self.timeSec = 59

            if(self.timeSec < 0 and self.timeMin == 0 and self.timeHour > 0):
                self.timeHour -= 1
                self.timeSec = 59
                self.timeMin = 59

            self.fullTime -= 1

    def Cancel(self):

        self.fullTime = 0

        print('Canceled Shutdown (%s)' % (self.status))

        self.status = 'No Sleep time'

        self.statusMessage.destroy()
        self.statusMessage = Label(window, text=('''
  %s''' % (self.status)), background='#121212', font='arial 16', fg='#c72344')
        self.statusMessage.pack()

        os.system('shutdown /a')


window = Tk()
window.title('Lembretes')
window.configure(background='#121212')
window.resizable(width=False, height=False)
window.minsize(width=600, height=800)




aaa = App()
aaa.Start()

window.mainloop()
