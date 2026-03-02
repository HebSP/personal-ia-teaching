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
        
        ### lista de oopções do menu

        opcao = input("\nEscolha uma opção (1-n): ").strip()
        
        ### seleção de opções do menu


def selecionar_perfil():
    '''
    Permite ao usuário selecionar ou criar um perfil de aluno, ou criar um novo
    '''
    perfil = {}
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
    perfil = obter_valores_perfil(perfis, perfil_atual = perfil_atual)
    salvar_perfil(perfil)
    return perfil

def obter_valores_perfil(perfis, perfil_atual=None):

    if not perfil_atual:
            perfil_atual = {
                "nome": "",
                "idade": "",
                "nivel": "",
                "estilo_aprendizagem": ""
            }

    niveis = ["Iniciante", "Intermediário", "Avançado"]
    
    estilos = ["Visual", "Auditivo", "Leitura-Escrita", "Cinestésico"]
    perfil = {}
    
    return perfil

def selecionar_topico():
    '''
    Permite ao usuário selecionar um tópico de interesse para aprender
    '''
    topico = input("Digite o tópico que deseja estudar: ").strip()

    return topico