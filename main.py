import os
from classLembrete import Lembrete
from timeFunctions import getNTPTimeLocal

lista = []
lista_inversa = []
iniciar = 1
codigo_atual = 0
codigo_escolhido = 0
quantidade = 0

try:        
    with open('textoLembretes.txt', 'r') as arquivo:
        lista = [linha.strip() for linha in arquivo if linha.strip()]
    for i in lista:
        quantidade += 1
except FileNotFoundError:    
    with open('textoLembretes.txt', 'w+') as arquivo:
        arquivo.writelines('')

def adicionar_lembrete(data: str, info: int):
    novoLembrete = Lembrete(data, info)
    lista.append(novoLembrete)


while (iniciar == 1):
    print(' LEMBRETES: ', quantidade)
    opcao = input(''' MENU
  
  1 - ADICIONAR LEMBRETE
  2 - EDITAR LEMBRETE
  3 - EXCLUIR LEMBRETE
  4 - LISTA DE LEMBRETES
  5 - LIMPAR LISTA
  6 - SAIR

  ESCOLHA UMA OPÇÃO: ''')

    opcao = opcao.strip()

    if (opcao == 1 or opcao == "1"):
        os.system('cls')
        repetir = 1
        while (repetir == 1):
            info = str(input(''' ADICIONAR LEMBRETE

      DIGITE AS INFORMAÇÕES DO LEMBRETE (DIGITE "MENU" PARA VOLTAR AO MENU PRINCIPAL): '''))

            if (info.strip().upper() == 'MENU'):
                os.system('cls')
                repetir = 0

            elif(info.strip().upper() == ''):

                print('''ERRO
INSIRA AS INFORMAÇÕES DO LEMBRETE''')

            else:

                data = getNTPTimeLocal()

                adicionar_lembrete(data, info)
                print(f'''
LEMBRETE ADICIONADO: {lista[-1]}''')
                codigo_atual += 1
                quantidade += 1
                repetir = 0

                aux = 0

                for i in range(0, quantidade - 1, 1):
                    aux = lista[i+1]
                    lista[i+1] = lista[0]
                    lista[0] = aux

                if (quantidade >= 1):
                    for n in enumerate(lista):
                        print(*n, sep=' ')

                with open('textoLembretes.txt', 'w') as arquivo:
                    for i in lista:
                        arquivo.writelines("%s\n" % i)   

                os.system('pause')
                os.system('cls')

    elif (opcao == 2 or opcao == "2"):
        os.system('cls')
        repetir = 1
        while (repetir == 1):
            for n in enumerate(lista):
                print(*n, sep=' ')

            try:
                codigo_escolhido = input(''' EDITAR LEMBRETE

DIGITE O NÚMERO REFERENTE AO LEMBRETE OU "MENU" PARA VOLTAR AO MENU PRINCIPAL: ''')
                codigo_escolhido = codigo_escolhido.strip()
                codigo_escolhido = int(codigo_escolhido)
                if (codigo_escolhido < len(lista) and codigo_escolhido >= 0):
                    info = str(input('DIGITE A NOVA INFORMAÇÃO DO LEMBRETE: '))

                    if(info.strip().upper() == ''):
                        print('''ERRO
INSIRA AS NOVAS INFORMAÇÕES DO LEMBRETE''')
                        repetir = 1

                    else:

                        data = getNTPTimeLocal()

                        antigo = lista[codigo_escolhido]
                        del lista[codigo_escolhido]
                        adicionar_lembrete(data, info)
                        print(f'EDITADO: {antigo}    >>>    {lista[-1]}')
                        codigo_atual += 1

                        repetir = 0
                        os.system('pause')
                        os.system('cls')

                        aux = 0

                        for i in range(0, quantidade - 1, 1):
                            aux = lista[i+1]
                            lista[i+1] = lista[0]
                            lista[0] = aux

                        with open('textoLembretes.txt', 'w') as arquivo:
                            for i in lista:
                                arquivo.writelines("%s\n" % i)    

                else:
                    print('''ERRO
INSIRA UM NÚMERO INTEIRO EXISTENTE NA LISTA''')
                    os.system('pause')
                    os.system('cls')
                    repetir = 1

            except ValueError:
                if (codigo_escolhido.strip().upper() == "MENU"):
                    repetir = 0
                    os.system('cls')

                else:
                    print('''ERRO
INSIRA UM NÚMERO INTEIRO EXISTENTE NA LISTA''')
                    os.system('pause')
                    os.system('cls')
                    repetir = 1

    elif (opcao == 3 or opcao == "3"):
        os.system('cls')
        repetir = 1
        while (repetir == 1):
            for n in enumerate(lista):
                print(*n, sep=' ')

            try:
                codigo_escolhido = input(''' EXCLUIR LEMBRETE

DIGITE O NÚMERO REFERENTE AO LEMBRETE OU "MENU" PARA VOLTAR AO MENU PRINCIPAL: ''')
                codigo_escolhido = int(codigo_escolhido)
                if (codigo_escolhido < len(lista) and codigo_escolhido >= 0):
                    print(f'EXCLUÍDO: {lista[codigo_escolhido]}')
                    del lista[codigo_escolhido]
                    quantidade -= 1

                    repetir = 0

                    with open('textoLembretes.txt', 'w') as arquivo:
                        for i in lista:
                            arquivo.writelines("%s\n" % i)

                    os.system('pause')
                    os.system('cls')

                else:
                    print('''ERRO
INSIRA UM NÚMERO INTEIRO EXISTENTE NA LISTA''')
                    os.system('pause')
                    os.system('cls')
                    repetir = 1

            except ValueError:
                if (codigo_escolhido.strip().upper() == "MENU"):
                    repetir = 0
                    os.system('cls')

                else:
                    print('''ERRO
INSIRA UM NÚMERO INTEIRO EXISTENTE NA LISTA''')
                    os.system('pause')
                    os.system('cls')
                    repetir = 1

    elif (opcao == 4 or opcao == "4"):
        os.system('cls')

        if (quantidade >= 1):
            for n in enumerate(lista):
                print(*n, sep=' ')

        else:
            print('LISTA VAZIA')

        os.system('pause')
        os.system('cls')

    elif (opcao == 5 or opcao == "5"):
        repetir = 1
        while (repetir == 1):
            os.system('cls')
            confirmar = str(input('''LIMPAR LISTA DE LEMBRETES? 
S = SIM       N = NÃO
CONFIRMAR: '''))
            confirmar = confirmar.strip()
            if (confirmar.strip().upper() == 'N'):
                repetir = 0
                os.system('pause')
                os.system('cls')

            elif (confirmar.strip().upper() == 'S'):
                lista.clear()
                repetir = 0
                quantidade = 0
                print('''LISTA LIMPA''')
                with open('textoLembretes.txt', 'w') as arquivo:
                    for i in lista:
                        arquivo.writelines("%s\n" % i)
                
                os.system('pause')
                os.system('cls')

            else:
                print('''ERRO
CONFIRMAR COM S = SIM OU N = NÃO''')
                os.system('pause')

    elif (opcao == 6 or opcao == "6"):
        iniciar = 0

    else:
        print(''' ERRO
ESCOLHA UM NÚMERO DE 1 A 6''')
        os.system('pause')
        os.system('cls')
