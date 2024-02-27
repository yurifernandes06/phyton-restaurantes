import os

restaurantes = [{'nome':'Deu em Pizza', 'especialidade':'Italiana', 'ativo':False}, 
               {'nome':'Sushi mister', 'especialidade':'Temakis', 'ativo':True},
                {'nome':'Burguer King', 'especialidade':'Batata frita', 'ativo':False}]   

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░ 
       """)

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar o estado do restaurante')
    print('4. Sair\n')

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu principal')
    main()

def finalizar_app():
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' *(len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do restaurante' .ljust(22)} | {'Categoria'.ljust(20)} Status')
    for restaurante in restaurantes:
       nome_do_restaurante = restaurante['nome']
       especialidade_do_restaurante = restaurante['especialidade']
       ativo = 'ativado' if restaurante['ativo'] else 'desativado'
       print(f'- {nome_do_restaurante.ljust(20)} | {especialidade_do_restaurante.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_do_restaurante= input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado= False
    
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {nome_do_restaurante} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')
    voltar_ao_menu_principal()


def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante= input('Digite o nome do restaurante que deseja cadastrar: ')
    especialidade_do_restaurante= input(f'Digite o nome da categoria do restaurante {nome_do_restaurante} que deseja cadastrar: ')
    dados_do_restaurante= {'nome': nome_do_restaurante, 'especialidade': especialidade_do_restaurante, 'ativo': False}
    if nome_do_restaurante in restaurantes:
        print('O restaurante já está na lista!')
    else:
        restaurantes.append(dados_do_restaurante)
        print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!\n')
    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
    voltar_ao_menu_principal()
main()

if __name__ == '__main__':
    main()
   