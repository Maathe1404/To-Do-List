#Cristo Vive
import os

tarefas = [

]

def título():
    print('''
████████╗ ██████╗     ██████╗  ██████╗     ██╗     ██╗███████╗████████╗
╚══██╔══╝██╔═══██╗    ██╔══██╗██╔═══██╗    ██║     ██║██╔════╝╚══██╔══╝
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║███████╗   ██║   
   ██║   ██║   ██║    ██║  ██║██║   ██║    ██║     ██║╚════██║   ██║   
   ██║   ╚██████╔╝    ██████╔╝╚██████╔╝    ███████╗██║███████║   ██║   
   ╚═╝    ╚═════╝     ╚═════╝  ╚═════╝     ╚══════╝╚═╝╚══════╝   ╚═╝   
                                                                       ''')

def menu():
 limpa_tela()
 print('Bem-vindo ao To Do List!')
 print(' 1 - Adicionar tarefa')
 print(' 2 - Visualizar tarefas')
 print(' 3 - Remover tarefa')
 print(' 4 - Sair')
 opção = input('Escolha uma opção: ')
 return opção

def escolher_opção(opção):
 if opção == '1':
    adicionar_tarefa()
 elif opção == '2':
    visualizar_tarefas()
 elif opção == '3':
    remover_tarefas()


def limpa_tela():
   os.system('cls')
   título()
   
def adicionar_tarefa():
    limpa_tela()
    Tarefa = input('Digite a tarefa que deseja adicionar: ')
    dados_da_tarefa = {'Tarefa':Tarefa, 'Dia':input('Digite o dia da tarefa: '), 'Horario':input('Digite o horario da tarefa: ')}
    tarefas.append(dados_da_tarefa)
    print(f'A tarefa {Tarefa} foi adicionada com sucesso!')
    input('Aperte uma tecla para voltar ao menu principal...')

def visualizar_tarefas():
    limpa_tela()
    print('Lista de tarefas: ')
    for Tarefa in tarefas:
       print(f'Tarefa: {Tarefa['Tarefa']} | Dia: {Tarefa['Dia']} | Horário: {Tarefa['Horario']}')
    input('Aperte uma tecla para voltar ao menu principal...')

def remover_tarefas(): 
   limpa_tela()
   print('Lista de tarefas: ')
   numero = 1
   for Tarefa in tarefas:
      print(numero,'-' f' Tarefa: {Tarefa['Tarefa'].ljust(20)} | Dia: {Tarefa['Dia'].ljust(20)} | Horário: {Tarefa['Horario'].ljust(20)}')
      numero = numero + 1
   remover = int(input ('Qual tarefa deseja remover? Escolha o número da tarefa.'))
   del tarefas[remover - 1]
   print(f'Tarefa {remover} removida com sucesso!')
   input('Aperte uma tecla para voltar ao menu principal...')

def encerrar_o_programa():
   limpa_tela()
   print('Encerrando o programa!')

while True:
    opção = menu()
    if opção == '4':
       encerrar_o_programa()
       break

    escolher_opção(opção)
