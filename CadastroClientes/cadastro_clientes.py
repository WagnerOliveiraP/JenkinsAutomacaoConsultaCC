#Listas/Excel/BD (Global)

Restaurantes = [{'Nome':'Burguer King','Tipo':'Fast Food','Status':False},
                {'Nome':'Pizza Hut','Tipo':'Pizzaria','Status':True},
                {'Nome':'Pizza Hut','Tipo':'Pizzaria','Status':False}]

#Bibliotecas
import os
#import keyboard

#Função

def alterar_cadastro():
    nome_restaurante = input('Digite o Nome do Restaurante que deseja alterar:')
    campo_desejado = input('Digite o Campo que Deseja Alterar:')
    restaurante_encontrato = False

    for restaurante in Restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrato = True
            
            if campo_desejado in restaurante:
                    novo_valor = input(f'Digite o novo valor para \n{campo_desejado}:')
                    restaurante[campo_desejado] = novo_valor
                    print(f'\nCampo {campo_desejado} atualizado com sucesso!\n')
                    voltar_menu()
            else:
                print(f'\nO campo "{campo_desejado}" não existe no cadastro do restaurante.\n')
                voltar_menu()    
    if not restaurante_encontrato:
        print('\nRestaurante não encontrado na lista.\n')
        voltar_menu()

def alterar_status():
    exibir_subtitulo('Alterando Status do Restaurante')
    nome_restaurante = input('\nDigite o Nome do Restaurante:')
    restaurante_encontrado = False

    for restaurante in Restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Status'] = not restaurante['Status']
            mensagem = f'O Restaraunte {nome_restaurante} foi Ativado com sucesso!' if restaurante['Status'] else f'O Restaurante {nome_restaurante} foi Desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'O Restaurante {nome_restaurante}')
    voltar_menu()

def voltar_menu():
    input('\nDigite uma Tecla para Voltar ao Menu Principal\n')
    main()

def exibir_subtitulo(texto):
    os.system('clear')
    linha = '*' * (len(texto))
    print(linha)
    print(f'\n{texto}\n')
    print(linha)

def opcao_invalida():
    exibir_subtitulo('Opção Invalida!')
    voltar_menu()

def finalizar_app():
    os.system('clear')
    print('\nFinalizando o Aplicativo\n')

def exibir_nome_do_programa():

    print("""
    ░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
    ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
    ╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
    ░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
    ██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
    ╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░""") 

def exibir_opcoes():
    print('\n1. Cadastrar Restaurente')
    print('2. Listar Restaurantes')
    print('3. Ativar/Desativar Restaurantes')
    print('4. Alterar Cadastro')
    print('5. Sair\n')

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma Opção:'))
        print(f'\nVocê escolhei a opção {opcao_escolhida}\n')

        #print(type(1)) Type = Identifica qual e o Tipo da Variavel
        if opcao_escolhida == 1:
            cadastrar_restaurente()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            alterar_status()
        elif opcao_escolhida ==4:
            alterar_cadastro() 
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
            opcao_invalida()

def cadastrar_restaurente():
    while True:
        exibir_subtitulo('Cadastro de Novos Restaurantes')
        nome_restaurente = input('\nDigite o Nome do Restaurente:\n')
        tipo_restaurante = input('\nDigite o Tipo do Restaurente:\n')

        dados_restaurante = {f'Nome':nome_restaurente,'Tipo':tipo_restaurante,'Status':False}
        Restaurantes.append(dados_restaurante)
        print(f'\no Restaurante {nome_restaurente} foi cadastrado com Sucesso!\n')
        voltar_menu()
        break

def listar_restaurantes():
    exibir_subtitulo('Listas Restaurantes') 
    print(f"{'Nome do Restaurante'.ljust(22)} | {'Tipo'.ljust(20)} | {'Status'.ljust(20)}")

    for index, restaurante in enumerate(Restaurantes, start=1):
        nome_resturante = restaurante['Nome']
        tipo_restaurante = restaurante['Tipo']
        status = restaurante['Status']
        if status == True:
            status = 'Ativo'
        else:
            status = 'Inativo'
        print(f'{index}. {nome_resturante.ljust(20)} | {tipo_restaurante.ljust(20)} | {status}')
    voltar_menu()

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
