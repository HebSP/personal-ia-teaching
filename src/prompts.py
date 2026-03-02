
def gerar_prompt_explicacao(topico, perfil):
    """
    Gera um prompt para explicação conceitual adaptado ao perfil do aluno.
    """
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "Visual")
    formato = _formatar_por_estilo(estilo)

    tarefa = f"analise passo a passo e encontre a melhor forma de explicar o tema '{topico}' para este aluno."

    prompt = f"""
{_persona_e_papel(perfil, topico)}

{tarefa}

{_diretrizes(perfil)}
""" ##criar prompt aqui
    return prompt.strip()


def gerar_prompt_exemplo(topico, perfil):
    """
    Gera um prompt para criar exemplos práticos adaptados ao perfil do aluno.
    """
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "Visual")
    formato = _formatar_por_estilo(estilo)
    prompt = f""" """ ##criar prompt aqui
    return prompt.strip()


def gerar_prompt_exercicio(topico, perfil):
    """
    Gera um prompt para criar exercícios de fixação adaptados ao perfil do aluno.
    """
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "Visual")
    formato = _formatar_por_estilo(estilo)
    prompt = f""" """ ##criar prompt aqui
    return prompt.strip()


def _formatar_por_estilo(estilo):
    """
    Retorna o formato da explicação baseado no estilo de aprendizagem.
    """
    formatos = {
        "Visual": "Use diagramas, esquemas e descrições visuais",
        "Auditivo": "Use uma linguagem fluida como se estivesse explicando verbalmente",
        "Leitura-Escrita": "Use listas, textos estruturados e definições formais",
        "Cinestésico": "Use exemplos prático com passos e atividades mãos-na-massa"
    }
    return formatos.get(estilo, "Linguagem clara e acessível")

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

    if nivel == "Iniciante":
        complementos.append("está começando a aprender")
    elif nivel == "Intermediário":
        complementos.append("já tem alguma experiência com")
    elif nivel == "Avançado":
        complementos.append("possui um conhecimento aprofundado")
    
    persona = f"Você é um tutor com boa didática especializado em ensino {complementos[0]}, e vai ensinar sobre {topico} para um aluno que {complementos[1]}, que tem {idade} anos e prefere um estilo de aprendizagem {estilo}."
    
    return persona

def _diretrizes(perfil):
    """
    Retorna diretrizes de ensino personalizadas com base no perfil do aluno e no tópico.
    """
    idade = perfil.get("idade", 0)
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "leitura-escrita")

    complementos = []

    formatos = {
        "Visual": "Use analogias visuais fortes, descreva cenas ou sugira diagramas simples.",
        "Auditivo": "Use um tom narrativo, conversacional e exemplos focados em explicações verbais.",
        "Leitura-Escrita": "Use listas estruturadas, tópicos, definições claras e textos organizados.",
        "Cinestésico": "Use analogias de movimento, ações físicas ou exemplos práticos."
    }

    complementos.append(formatos.get(estilo, "Use uma linguagem clara e acessível."))

    niveis = {
        "Iniciante": "Inicie com conceitos básicos e exemplos simples.",
        "Intermediário": "Incorpore desafios moderados e estimule a resolução de problemas.",
        "Avançado": "Promova discussões profundas e análise crítica."
    }
    complementos.append(niveis.get(nivel, "Use uma abordagem adequada ao nível do aluno."))


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

    

    complementos.append(f"Considere que o aluno {subcomplemento[0]}possui um conhecimento {nivel.lower()}, use vocabulário e exemplos adequados.")
    diretrizes = f"Diretrizes de ensino: {' '.join(complementos)}"
    return diretrizes