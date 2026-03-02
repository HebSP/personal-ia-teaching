from generator import gerar_exemplo, gerar_exercicio, gerar_explicacao
from storage import carregar_perfil, deletar_perfil, listar_perfis, salvar_perfil

def inicializar_interface():
    '''
    Função para inicializar a interface do usuário
    '''
    print("--- Iniciando a Plataforma Educativa IA ---")

def error_mensagem(mensagem):
    '''
    Função para exibir mensagens de erro para o usuário
    '''
    print(f"Erro: {mensagem}")

def rodar_menu(client):
    """
    Função que executa o menu interativo da plataforma educativa.
    """
    print("--- Bem-vindo à Plataforma Educativa IA ---")
    
    perfil = selecionar_perfil(client)

    topico = selecionar_topico(client)

    while True:

        print("\n--- Menu Principal ---")
        
        print("\nEscolha uma opção:")
        print("1. Gerar explicação conceitual")
        print("2. Criar exemplo prático")
        print("3. gerar exercício de fixação")
        print("4. escolher outro tópico")
        print("5. escolher outro perfil")
        print("6. editar perfil atual")
        print("7. Deletar perfil atual")
        print("8. Sair")

        opcao = input("\nEscolha uma opção (1-8): ").strip()
        
        if opcao == "1":
            print(gerar_explicacao(client, topico, perfil))
        elif opcao == "2":
            print(gerar_exemplo(client, topico, perfil))
        elif opcao == "3":
            print(gerar_exercicio(client, topico, perfil))
        elif opcao == "4":
            topico = selecionar_topico()
        elif opcao == "5":
            perfil = selecionar_perfil()
        elif opcao == "6":
            perfil = editar_perfil(listar_perfis(), perfil)
        elif opcao == "7":
            deletar_perfil(perfil["nome"])
            print(f"Perfil '{perfil['nome']}' deletado com sucesso.")
            print("Selecione um novo perfil para continuar:")
            perfil = selecionar_perfil()
        elif opcao == "8":
            print("Encerrando a aplicação. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def selecionar_perfil():
    '''
    Permite ao usuário selecionar ou criar um perfil de aluno, ou criar um novo
    '''

    print("Selecione um perfil de aluno:")
    perfis = listar_perfis()
    for i, perfil in enumerate(perfis, 1):
        print(f"{i}. {perfil}")

    perfil = None
    while True:
        opcao = input("\nDigite o número do perfil ou 'n' para criar um novo perfil:").strip()
        if opcao.lower() == 'n':
            criar_perfil(perfis)
            break
        elif opcao.isdigit() and 1 <= int(opcao) <= len(perfis):
            perfil = carregar_perfil(perfis[int(opcao)-1])
            break
        else:
            print("Opção inválida. Tente novamente.")
    return perfil

def criar_perfil(perfis):
    '''
    Permite ao usuário criar um novo perfil de aluno
    '''
    perfil = obter_valores_perfil(perfis)
    salvar_perfil(perfil)
    return perfil

def editar_perfil(perfis, perfil_atual):
    '''
    Permite ao usuário editar um perfil existente
    '''
    print(f"Editando perfil: {perfil_atual['nome']}")
    print("Deixe o campo em branco para manter o valor atual.")
    perfil = obter_valores_perfil(perfis)
    perfil["nome"] = perfil_atual["nome"]

def obter_valores_perfil(perfis, perfil_atual=None):

    if not perfil_atual:
            perfil_atual = {
                "nome": "",
                "idade": "",
                "nivel": "",
                "estilo_aprendizagem": ""
            }

    while True:
        nome = input("Digite o nome do novo perfil: ").strip()
        if not nome:
            if perfil_atual["nome"]:
                print(f"Manter nome atual '{perfil_atual['nome']}' para o perfil? (s/n): ")
                if input().strip().lower() == 's':
                    nome = perfil_atual["nome"]
                    break
            else:
                print("O nome do perfil não pode ser vazio. Por favor, digite um nome.")
        elif nome in perfis and nome != perfil_atual["nome"]:
            print("Já existe um perfil com esse nome. Por favor, escolha outro nome.")
        elif input(f"Confirma o '{nome}' para o novo perfil? (s/n): ").strip().lower() == 's':
            break
    
    while True:      
        idade = input("Digite a idade do aluno: ").strip()
        if not idade:
            if perfil_atual["idade"]:
                print(f"Manter idade atual '{perfil_atual['idade']}' para o perfil? (s/n): ")
                if input().strip().lower() == 's':
                    idade = perfil_atual["idade"]
                    break
            else:
                print("A idade do perfil não pode ser vazia. Por favor, digite uma idade.")
        elif idade.isdigit():
            idade = int(idade)
            if input(f"Confirma a idade '{idade}' para o perfil? (s/n): ").strip().lower() == 's':
                break
        else:
            print("Idade inválida. Por favor, digite um número.")

    niveis = ["Iniciante", "Intermediário", "Avançado"]
    print("escolha o nível de conhecimento do aluno:")
    print("1. Iniciante")
    print("2. Intermediário")
    print("3. Avançado")
    
    while True:
        nivel = input("digite o número correspondente ao nível de conhecimento: ").strip()
        if not nivel:
            if perfil_atual["nivel"]:
                print(f"Manter nível atual '{perfil_atual['nivel']}' para o perfil? (s/n): ")
                if input().strip().lower() == 's':
                    nivel = perfil_atual["nivel"]
                    break
            else:
                print("O nível de conhecimento do perfil não pode ser vazio. Por favor, escolha um nível.")
        elif nivel in ['1', '2', '3']:
            nivel = niveis[int(nivel)-1]
            if input(f"Confirma o nível '{nivel}' para o perfil? (s/n): ").strip().lower() == 's':
                break
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

    estilos = ["Visual", "Auditivo", "Leitura-Escrita", "Cinestésico"]
    print("escolha o estilo de aprendizagem do aluno:")
    print("1. Visual")
    print("2. Auditivo")
    print("3. Leitura-Escrita")
    print("4. Cinestésico")

    while True:
        estilo_aprendizagem = input("digite o número correspondente ao estilo de aprendizagem: ").strip()
        
        if not estilo_aprendizagem:
            if perfil_atual["estilo_aprendizagem"]:
                print(f"Manter estilo de aprendizagem atual '{perfil_atual['estilo_aprendizagem']}' para o perfil? (s/n): ")
                if input().strip().lower() == 's':
                    estilo_aprendizagem = perfil_atual["estilo_aprendizagem"]
                    break
            else:
                print("O estilo de aprendizagem do perfil não pode ser vazio. Por favor, escolha um estilo.")
        elif estilo_aprendizagem in ['1', '2', '3', '4']:
            estilo_aprendizagem = estilos[int(estilo_aprendizagem)-1]
            if input(f"Confirma o estilo de aprendizagem '{estilo_aprendizagem}' para o perfil? (s/n): ").strip().lower() == 's':
                break
        else:
            print("Opção inválida. Por favor, escolha 1, 2, 3 ou 4.")

    perfil = {
        "nome": nome,
        "idade": idade,
        "nivel": nivel,
        "estilo_aprendizagem": estilo_aprendizagem
    }
    return perfil

def selecionar_topico():
    '''
    Permite ao usuário selecionar um tópico de interesse para aprender
    '''
    topico = input("Digite o tópico que deseja estudar: ").strip()

    return topico