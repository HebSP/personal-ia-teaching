
def gerar_prompt_explicacao(topico, perfil):
    """
    Gera um prompt para explicação conceitual adaptado ao perfil do aluno.
    """

    tarefa = f"Analise passo a passo e encontre a melhor forma de explicar o tema '{topico}' para este aluno.\nExplique sua lógica de escolha da analogia visual em uma frase breve, e depois forneça a explicação estruturada.\n"

    prompt = f"""
{_persona_e_papel(perfil, topico)}
{tarefa}
{_diretrizes(perfil)}
De apenas a explicação sem nenhum texto adicional.
"""
    return prompt.strip()


def gerar_prompt_exemplo(topico, perfil):
    """
    Gera um prompt para criar exemplos práticos adaptados ao perfil do aluno.
    """

    tarefa = f"Analise passo a passo e encontre a melhor forma de criar um exemplo prático sobre o tema '{topico}' para este aluno.\nPrimeiro, descreva brevemente o cenário que você vai criar para o exemplo, e depois forneça o exemplo prático estruturado.\n"

    prompt = f"""
{_persona_e_papel(perfil, topico)}
{tarefa}
{_diretrizes(perfil)}
De apenas o exemplo prático sem nenhum texto adicional.
"""
    return prompt.strip()


def gerar_prompt_exercicio(topico, perfil):
    """
    Gera um prompt para criar exercícios de fixação adaptados ao perfil do aluno.
    """

    tarefa = f"Analise passo a passo e encontre a melhor forma de criar um exercício de fixação sobre o tema '{topico}' para este aluno.\n"
    
    prompt = f"""
{_persona_e_papel(perfil, topico)}
{tarefa}
{_diretrizes(perfil)}
O exercicio deve estimular o pensamento critico.
De apenas o exercício de fixação sem nenhum texto adicional.
"""
    return prompt.strip()

def gerar_prompt_visual_cli(topico, perfil):
    """
    Gera um prompt para criar representações visuais adaptadas ao perfil do aluno.
    """

    tarefa = f"Analise passo a passo e encontre a melhor forma de criar um mapa mental sobre o tema '{topico}' para este aluno.\nPrimeiro, revise cada conceito e suas ligações no mapa que você vai criar, e depois forneça a representação visual estruturada.\n"

    prompt = f"""
{_persona_e_papel(perfil, topico)}
{tarefa}
{_diretrizes_visual_cli(perfil)}
De apenas a representação visual como um mapa mental em ascii sem nenhum texto adicional.
"""
    return prompt.strip()

def gerar_prompt_visual_html(topico, perfil):
    """
    Gera um prompt para criar representações visuais adaptadas ao perfil do aluno.
    """

    tarefa = f"Analise passo a passo e encontre a melhor forma de criar um mapa mental sobre o tema '{topico}' para este aluno.\nPrimeiro, revise cada conceito e suas ligações no mapa que você vai criar, e depois forneça a representação visual estruturada usando recursos de HTML.\n"

    prompt = f"""
{_persona_e_papel(perfil, topico)}
{tarefa}
{_diretrizes_visual_html(perfil)}
De apenas a representação visual como um mapa mental em html sem nenhum texto adicional.
"""
    return prompt.strip()

def _persona_e_papel(perfil, topico):
    """
    Retorna uma descrição da persona e do papel do tutor com base no perfil do aluno.
    """
    idade = perfil.get("idade", 0) #caso de exceção
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "leitura-escrita")


    complementos = []
    
    if idade <= 0:
        if nivel == "Iniciante":
            complementos.append("fundamental")
        elif nivel == "Intermediário":
            complementos.append("medio")
        else:
            complementos.append("superior")
    elif idade < 6:
        complementos.append("infantil")
    elif idade < 12:
        complementos.append("fundamental")
    elif idade < 18:
        complementos.append("medio")
    else:
        if nivel == "Iniciante":
            complementos.append("fundamental e medio para adultos")
        else:
            complementos.append("superior")

    niveis = {
        "Iniciante": "está começando a aprender",
        "Intermediário": "já tem alguma experiência",
        "Avançado": "possui um conhecimento aprofundado"
    }

    complementos.append(niveis.get(nivel, "tem interesse em aprender"))

    persona = f"Você é um tutor com boa didática especializado em ensino {complementos[0]}, e vai ensinar sobre {topico} para um aluno que {complementos[1]}, que tem {idade} anos e prefere um estilo de aprendizagem {estilo}.\n"
    
    return persona

def _diretrizes(perfil):
    """
    Retorna diretrizes de ensino personalizadas com base no perfil do aluno e no tópico.
    """
    idade = perfil.get("idade", 0)
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "leitura-escrita")

    complementos = []

    estilos = {
        "Visual": "Use analogias visuais fortes, descreva cenas ou sugira diagramas simples.\n",
        "Auditivo": "Use um tom narrativo, conversacional e exemplos focados em explicações verbais e perguntas para reflexão.\n",
        "Leitura-Escrita": "Use listas estruturadas, tópicos, definições claras e textos organizados.\n",
        "Cinestésico": "Use analogias de movimento, ações físicas ou exemplos práticos.\n"
    }

    complementos.append(estilos.get(estilo, "Use uma linguagem clara e acessível.\n"))

    niveis = {
        "Iniciante": "Inicie com conceitos básicos e exemplos simples.\n",
        "Intermediário": "Incorpore desafios moderados e estimule a resolução de problemas.\n",
        "Avançado": "Promova discussões profundas e análise crítica.\n"
    }
    complementos.append(niveis.get(nivel, "Use uma abordagem adequada ao nível do aluno.\n"))

    formatos = {
        "Visual": "Estruture a resposta usando bullet points, negrito para destacar palavras-chave e tópicos bem organizados.\n",
        "Auditivo": "Estruture a resposta como um roteiro de conversa ou um podcast curto. Use frases mais longas e fluidas, e inclua perguntas retóricas para o aluno refletir enquanto 'ouve' mentalmente.\n",
        "Leitura-Escrita": "Estruture a resposta com títulos claros, parágrafos bem definidos e listas numeradas para passos sequenciais. Foque em definições precisas.\n",
        "Cinestésico": "Estruture a resposta focando em 'passo a passo' ou um roteiro. Use verbos de ação e apresente o conteúdo de forma prática.\n"
    }

    complementos.append(formatos.get(estilo, "apresente um texto coerente em paragrafos de facil leitura\n"))

    subcomplemento = []

    if idade <= 0:
        subcomplemento.append("") # caso de exceção
    elif idade < 6:
        subcomplemento.append("está no inicio da infancia e ")
    elif idade < 12:
        subcomplemento.append("está na fase final da infancia e ")
    elif idade < 18:
        subcomplemento.append("está na fase adolescente e ")
    else:
        subcomplemento.append("é um adulto e ")

    

    complementos.append(f"Considere que o aluno {subcomplemento[0]}possui um conhecimento {nivel.lower()}, use vocabulário e exemplos adequados.\n")
    diretrizes = f"Diretrizes de ensino: {' '.join(complementos)}"
    return diretrizes

def _diretrizes_visual_cli(perfil):
    """
    Retorna diretrizes de ensino personalizadas com base no perfil do aluno e no tópico, apenas para representações visuais sem texto solto.
    """
    idade = perfil.get("idade", 0)
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "leitura-escrita")

    complementos = []

    estilos = {
        "Visual": "Foque em um layout espacial claro, usando símbolos para mostrar hierarquia.\n",
        "Auditivo": "Foque em uma estrutura hierárquica que conte uma história lógica. Use palavras-chave numa estrutura de perguntas e respostas entre os nós.\n",
        "Leitura-Escrita": "foque em definições claras e textos organizados nas ramificações.\n",
        "Cinestésico": "Use analogias de 'fluxo de ação' ou 'processos'. O mapa deve mostrar como algo funciona passo a passo.\n"
    }

    complementos.append(estilos.get(estilo, "Use uma linguagem clara e acessível.\n"))

    niveis = {
        "Iniciante": "Crie um mapa mental simples, explicando os conceitos fundamentais de forma simples.\n",
        "Intermediário": "Crie um mapa mental elaborado, com exemplos e detalhes mais importantes.\n",
        "Avançado": "Crie um mapa mental denso, mostrando interconexões complexas entre os vários conceitos relacionados.\n"
    }
    complementos.append(niveis.get(nivel, "crie um mapa mental apresentando o tema de forma clara e organizada.\n"))

    subcomplemento = []

    if idade <= 0:
        subcomplemento.append("") # caso de exceção
    elif idade < 6:
        subcomplemento.append("está no inicio da infancia e ")
    elif idade < 12:
        subcomplemento.append("está na fase final da infancia e ")
    elif idade < 18:
        subcomplemento.append("está na fase adolescente e ")
    else:
        subcomplemento.append("é um adulto e ")

    

    complementos.append(f"Considere que o aluno {subcomplemento[0]}possui um conhecimento {nivel.lower()}, use vocabulário e conceitos adequados.\n")

    complementos.append("Lembre-se de que o mapa mental deve ter largura adequada ao tamanho de uma tela comum de computador com 200 caracteres de largura.")
    diretrizes = f"Diretrizes de ensino: {' '.join(complementos)}"
    return diretrizes

def _diretrizes_visual_html(perfil):
    """
    Retorna diretrizes de ensino personalizadas com base no perfil do aluno e no tópico, apenas para representações visuais sem texto solto.
    """
    idade = perfil.get("idade", 0)
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "leitura-escrita")

    complementos = []

    estilos = {
        "Visual": "Foque em um layout espacial claro, usando símbolos para mostrar hierarquia.\n",
        "Auditivo": "Foque em uma estrutura hierárquica que conte uma história lógica. Use palavras-chave numa estrutura de perguntas e respostas entre os nós.\n",
        "Leitura-Escrita": "foque em definições claras e textos organizados nas ramificações.\n",
        "Cinestésico": "Use analogias de 'fluxo de ação' ou 'processos'. O mapa deve mostrar como algo funciona passo a passo.\n"
    }

    complementos.append(estilos.get(estilo, "Use uma linguagem clara e acessível.\n"))

    niveis = {
        "Iniciante": "Crie um mapa mental simples, explicando os conceitos fundamentais de forma simples.\n",
        "Intermediário": "Crie um mapa mental elaborado, com exemplos e detalhes mais importantes.\n",
        "Avançado": "Crie um mapa mental denso, mostrando interconexões complexas entre os vários conceitos relacionados.\n"
    }
    complementos.append(niveis.get(nivel, "crie um mapa mental apresentando o tema de forma clara e organizada em forma de Lista Aninhada HTML.\n O tópico principal deve ser a raiz.\n organize a estrutura de tópicos para garantir que os objetos não vão se sobrepor.\n todo style da pagina deve ser feito por meio de classes\n"))

    subcomplemento = []

    if idade <= 0:
        subcomplemento.append("") # caso de exceção
    elif idade < 6:
        subcomplemento.append("está no inicio da infancia e ")
    elif idade < 12:
        subcomplemento.append("está na fase final da infancia e ")
    elif idade < 18:
        subcomplemento.append("está na fase adolescente e ")
    else:
        subcomplemento.append("é um adulto e ")

    

    complementos.append(f"Considere que o aluno {subcomplemento[0]}possui um conhecimento {nivel.lower()}, use vocabulário e conceitos adequados.\n")

    diretrizes = f"Diretrizes de ensino: {' '.join(complementos)}"
    return diretrizes