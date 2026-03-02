
def gerar_prompt_explicacao(topico, perfil):
    """
    Gera um prompt para explicação conceitual adaptado ao perfil do aluno.
    """
    nivel = perfil.get("nivel", "Iniciante")
    estilo = perfil.get("estilo_aprendizagem", "Visual")
    formato = _formatar_por_estilo(estilo)
    prompt = f""" """ ##criar prompt aqui
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