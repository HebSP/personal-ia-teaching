
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

    example = "<!DOCTYPE html>\n<html lang=\"pt-BR\">\n    <head>\n        <meta charset=\"UTF-8\">\n        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n        <title>Mapa Mental: <!--TEMA--> </title>\n        <style>\n            body {\n                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;\n                background-color: #f0f2f5;\n                display: flex;\n                justify-content: center;\n                align-items: center;\n                min-height: 100vh;\n                margin: 0;\n                overflow: hidden; /* Prevent scrollbars from the SVG overlay */\n            }\n            .mind-map-container {\n                position: relative;\n                width: 1800px; /* ajust width for map size */\n                height: 2400px; /* ajust height for map size */\n                background-color: #ffffff;\n                border-radius: 15px;\n                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.15);\n                margin: 20px;\n                overflow: hidden; /* Ensure nodes are within bounds */\n            }\n            .node {\n                position: absolute;\n                padding: 8px 15px;\n                border-radius: 25px;\n                text-align: center;\n                line-height: 1.3;\n                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);\n                transition: all 0.3s ease;\n                cursor: default;\n                color: #333;\n                font-size: 13px; /* Base font size */\n            }\n            .node:hover {\n                transform: translateY(-2px);\n                box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);\n            }\n            /* Central Node */\n            .node-central {\n                background-color: #888888; /* choose better for theme */\n                color: #fff;\n                font-size: 30px;\n                font-weight: bold;\n                padding: 15px 30px;\n                border-radius: 50px;\n                z-index: 10;\n            }\n            /* Main Branch Nodes */\n            .node-main-branch {\n                font-size: 18px;\n                font-weight: bold;\n                padding: 12px 20px;\n                border-radius: 35px;\n                z-index: 9;\n            }\n            /* create a consistent color theme for main branches in that model, can add or remove more branches as needed, that is a example */\n\n            .branch-mainbranch1 { background-color: #e6e6fa; border: 2px solid #6a0572; color: #6a0572; } /* Lavender */\n            .branch-mainbranch2 { background-color: #d1f7e9; border: 2px solid #28a745; color: #28a745; } /* Mint green */\n            .branch-mainbranch3 { background-color: #ffe0b2; border: 2px solid #ff8c00; color: #ff8c00; } /* Light orange */\n            .branch-mainbranch4 { background-color: #b3e5fc; border: 2px solid #007bff; color: #007bff; } /* Light blue */\n            .branch-mainbranch5 { background-color: #ffcdd2; border: 2px solid #dc3545; color: #dc3545; } /* Light red */\n            .branch-mainbranch6 { background-color: #d7ccc8; border: 2px solid #6c757d; color: #6c757d; } /* Grey-brown */\n\n            /* Sub-Branch Nodes */\n            .node-sub-branch {\n                font-size: 15px;\n                font-weight: 600;\n                padding: 10px 18px;\n                border-radius: 30px;\n                box-shadow: 0 3px 6px rgba(0, 0, 0, 0.1);\n            }\n\n            /*create a consistent color theme for sub-branches, that is a example consistent with main branches*/\n            .sub-sub_branch9 { background-color: #fff3e0; border: 1px solid #ffb74d; color: #ff8c00; } /* Lighter orange */\n            .sub-sub_branch10 { background-color: #e1f5fe; border: 1px solid #4fc3f7; color: #007bff; } /* Lighter blue */\n            .sub-sub_branch11 { background-color: #e8f5e9; border: 1px solid #81c784; color: #28a745; } /* Lighter green */\n            .sub-sub_branch12 { background-color: #fce4ec; border: 1px solid #f06292; color: #dc3545; } /* Lighter pink */\n            .sub-sub_branch13 { background-color: #ede7f6; border: 1px solid #9575cd; color: #6a0572; } /* Lighter purple */\n            .sub-mainbranch2 { background-color: #dcf2e1; border: 1px solid #8fd9a8; color: #28a745; }\n            .sub-mainbranch1 { background-color: #f7e6f8; border: 1px solid #b7a1cf; color: #6a0572; }\n            .sub-mainbranch4 { background-color: #e0f2f7; border: 1px solid #82b1ff; color: #007bff; }\n            .sub-mainbranch5 { background-color: #ffebee; border: 1px solid #ef9a9a; color: #dc3545; }\n            .sub-mainbranch6 { background-color: #f5f5f5; border: 1px solid #bdbdbd; color: #6c757d; }\n            /* Leaf Nodes */\n            .node-leaf {\n                font-size: 12px;\n                padding: 6px 12px;\n                border-radius: 20px;\n                background-color: #f8f9fa;\n                border: 1px solid #ced4da;\n                color: #555;\n                box-shadow: none;\n            }\n            .node-leaf-concept {\n                background-color: #e9ecef;\n                border: 1px solid #adb5bd;\n            }\n            /* SVG for connections */\n            .connections-svg {\n                position: absolute;\n                top: 0;\n                left: 0;\n                width: 100%;\n                height: 100%;\n                pointer-events: none; /* Allows clicks to pass through to nodes */\n                z-index: 1; /* Below nodes */\n            }\n            .line {\n                stroke-width: 2px;\n                fill: none;\n                stroke-linecap: round;\n                transition: stroke 0.3s ease;\n            }\n\n            /*choose colors that are distinct but harmonious, a looks good with the nodes*/\n            .line-main { stroke: #6a0572; stroke-width: 3px; } /* Main branch lines */\n            .line-sub { stroke: #5e6472; } /* Sub-branch lines */\n            .line-detail { stroke: #9e9e9e; stroke-width: 1px; } /* Leaf lines */\n            .line-conceptual { stroke: #555; stroke-dasharray: 4 2; stroke-width: 1.5px; } /* Dashed for cross-cutting concepts */\n            /* Define node IDs for JS connection calculations */\n            /* For CSS, we just need to position them. */\n        </style>\n    </head>\n    <body>\n        <div class=\"mind-map-container\" id=\"mindMapContainer\">\n            <!-- SVG for connections (will be populated by JS or manually positioned) -->\n            <svg class=\"connections-svg\" id=\"mindMapSVG\">\n                <!-- Lines will be dynamically generated or manually placed here -->\n                <!-- Example line: <path class=\"line line-main\" d=\"M 800 450 C 700 350, 450 180, 250 150\" /> -->\n            </svg>\n            <!-- Nodes -->\n            <!-- Central Topic -->\n            <div id=\"topic\" class=\"node node-central\" style=\"left: 50%; top: 50%; transform: translate(-50%, -50%);\">topic(main theme)</div>\n            <!-- Main Branches -->\n            <div id=\"mainbranch1\" class=\"node node-main-branch branch-mainbranch1\" style=\"left: 15%; top: 15%;\">Main Branch 1 texto</div>\n            <div id=\"mainbranch2\" class=\"node node-main-branch branch-mainbranch2\" style=\"left: 15%; top: 85%; transform: translateY(-100%);\">Main Branch 2 texto</div>\n            <div id=\"mainbranch3\" class=\"node node-main-branch branch-mainbranch3\" style=\"left: 50%; top: 10%; transform: translateX(-50%);\">Main Branch 3 texto</div>\n            <div id=\"mainbranch4\" class=\"node node-main-branch branch-mainbranch4\" style=\"left: 85%; top: 50%; transform: translateY(-50%);\">Main Branch 4 texto</div>\n            <div id=\"mainbranch5\" class=\"node node-main-branch branch-mainbranch5\" style=\"left: 30%; top: 50%; transform: translateY(-50%);\">Main Branch 5 texto</div>\n            <div id=\"mainbranch6\" class=\"node node-main-branch branch-mainbranch6\" style=\"left: 70%; top: 85%; transform: translateY(-100%);\">Main Branch 6 texto</div>\n            <!-- mainbranch1 Sub-branches & Leaves -->\n            <div id=\"sub_branch1\" class=\"node node-sub-branch sub-mainbranch1\" style=\"left: 5%; top: 5%;\">Sub branch 1 texto</div>\n            <div id=\"sub_branch2\" class=\"node node-sub-branch sub-mainbranch1\" style=\"left: 10%; top: 25%;\">Sub branch 2 texto</div>\n            <div id=\"sub_branch3\" class=\"node node-sub-branch sub-mainbranch1\" style=\"left: 25%; top: 5%;\">Sub branch 3 texto</div>\n            <div id=\"sub_branch4\" class=\"node node-sub-branch sub-mainbranch1\" style=\"left: 30%; top: 20%;\">Sub branch 4 texto</div>\n            <div id=\"leaf1\" class=\"node node-leaf node-leaf-concept\" style=\"left: 0%; top: 0%;\">Leaf 1 texto</div>\n            <div id=\"leaf2\" class=\"node node-leaf node-leaf-concept\" style=\"left: 5%; top: 10%;\">Leaf 2 texto</div>\n            <div id=\"leaf3\" class=\"node node-leaf node-leaf-concept\" style=\"left: 10%; top: 0%;\">Leaf 3 texto</div>\n            <div id=\"leaf4\" class=\"node node-leaf node-leaf-concept\" style=\"left: 0%; top: 30%;\">Leaf 4 texto</div>\n            <div id=\"leaf5\" class=\"node node-leaf node-leaf-concept\" style=\"left: 15%; top: 35%;\">Leaf 5 texto</div>\n            <div id=\"leaf6\" class=\"node node-leaf node-leaf-concept\" style=\"left: 35%; top: 0%;\">Leaf 6 texto</div>\n            <div id=\"leaf7\" class=\"node node-leaf node-leaf-concept\" style=\"left: 20%; top: 10%;\">Leaf 7 texto</div>\n            <div id=\"leaf8\" class=\"node node-leaf node-leaf-concept\" style=\"left: 40%; top: 15%;\">Leaf 8 texto</div>\n            <div id=\"leaf9\" class=\"node node-leaf node-leaf-concept\" style=\"left: 25%; top: 25%;\">Leaf 9 texto</div>\n            <!-- mainbranch2 Sub-branches & Leaves -->\n            <div id=\"sub_branch5\" class=\"node node-sub-branch sub-mainbranch2\" style=\"left: 5%; top: 75%;\">Sub Branch 5 texto</div>\n            <div id=\"sub_branch6\" class=\"node node-sub-branch sub-mainbranch2\" style=\"left: 10%; top: 90%;\">Sub Branch 6 texto</div>\n            <div id=\"sub_branch7\" class=\"node node-sub-branch sub-mainbranch2\" style=\"left: 25%; top: 80%;\">Sub Branch 7 texto</div>\n            <div id=\"sub_branch8\" class=\"node node-sub-branch sub-mainbranch2\" style=\"left: 30%; top: 95%;\">Sub Branch 8 texto</div>\n            <div id=\"leaf10\" class=\"node node-leaf node-leaf-concept\" style=\"left: 0%; top: 70%;\">Leaf 10 texto</div>\n            <div id=\"leaf11\" class=\"node node-leaf node-leaf-concept\" style=\"left: 10%; top: 80%;\">Leaf 11 texto</div>\n            <div id=\"leaf12\" class=\"node node-leaf node-leaf-concept\" style=\"left: 0%; top: 95%;\">Leaf 12 texto</div>\n            <div id=\"leaf13\" class=\"node node-leaf node-leaf-concept\" style=\"left: 20%; top: 90%;\">Leaf 13 texto</div>\n            <div id=\"leaf14\" class=\"node node-leaf node-leaf-concept\" style=\"left: 35%; top: 75%;\">Leaf 14 texto</div>\n            <div id=\"leaf15\" class=\"node node-leaf node-leaf-concept\" style=\"left: 25%; top: 85%;\">Leaf 15 texto</div>\n            <div id=\"leaf16\" class=\"node node-leaf node-leaf-concept\" style=\"left: 40%; top: 90%;\">Leaf 16 texto</div>\n            <!-- mainbranch3 & Técnicas Sub-branches & Leaves -->\n            <div id=\"sub_branch9\" class=\"node node-sub-branch sub-sub_branch9\" style=\"left: 45%; top: 18%;\">Sub Branch 9 texto</div>\n            <div id=\"sub_branch10\" class=\"node node-sub-branch sub-sub_branch10\" style=\"left: 55%; top: 18%;\">Sub Branch 10 texto</div>\n            <div id=\"sub_branch11\" class=\"node node-sub-branch sub-sub_branch11\" style=\"left: 65%; top: 18%;\">Sub Branch 11 texto</div>\n            <div id=\"sub_branch12\" class=\"node node-sub-branch sub-sub_branch12\" style=\"left: 75%; top: 18%;\">Sub Branch 12 texto</div>\n            <div id=\"sub_branch13\" class=\"node node-sub-branch sub-sub_branch13\" style=\"left: 85%; top: 18%;\">Sub Branch 13 texto</div>\n            <!-- sub_branch9 -->\n            <div id=\"leaf17\" class=\"node node-leaf sub-sub_branch9\" style=\"left: 40%; top: 25%;\">Leaf 17 texto</div>\n            <div id=\"leaf18\" class=\"node node-leaf sub-sub_branch9\" style=\"left: 48%; top: 25%;\">Leaf 18 texto</div>\n            <div id=\"leaf19\" class=\"node node-leaf sub-sub_branch9\" style=\"left: 44%; top: 30%;\">Leaf 19 texto</div>\n            <div id=\"leaf20\" class=\"node node-leaf node-leaf-concept\" style=\"left: 38%; top: 21%;\">Leaf 20 texto</div>\n            <div id=\"leaf21\" class=\"node node-leaf node-leaf-concept\" style=\"left: 50%; top: 21%;\">Leaf 21 texto</div>\n            <div id=\"leaf22\" class=\"node node-leaf node-leaf-concept\" style=\"left: 40%; top: 34%;\">Leaf 22 texto</div>\n            <!-- sub_branch10 -->\n            <div id=\"leaf23\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 54%; top: 25%;\">Leaf 23 texto</div>\n            <div id=\"leaf24\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 60%; top: 25%;\">Leaf 24 texto</div>\n            <div id=\"leaf25\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 54%; top: 30%;\">Leaf 25 texto</div>\n            <div id=\"leaf26\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 60%; top: 30%;\">Leaf 26 texto</div>\n            <div id=\"leaf27\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 57%; top: 35%;\">Leaf 27 texto</div>\n            <div id=\"leaf28\" class=\"node node-leaf sub-sub_branch10\" style=\"left: 63%; top: 35%;\">Leaf 28 texto</div>\n            <!-- sub_branch11 -->\n            <div id=\"leaf29\" class=\"node node-leaf sub-sub_branch11\" style=\"left: 67%; top: 25%;\">Leaf 29 texto</div>\n            <div id=\"leaf30\" class=\"node node-leaf sub-sub_branch11\" style=\"left: 72%; top: 25%;\">Leaf 30 texto</div>\n            <div id=\"leaf31\" class=\"node node-leaf sub-sub_branch11\" style=\"left: 70%; top: 30%;\">Leaf 31 texto</div>\n            <div id=\"leaf32\" class=\"node node-leaf sub-sub_branch11\" style=\"left: 68%; top: 35%;\">Leaf 32 texto</div>\n            <!-- sub_branch12 -->\n            <div id=\"leaf33\" class=\"node node-leaf sub-sub_branch12\" style=\"left: 77%; top: 25%;\">Leaf 33 texto</div>\n            <div id=\"leaf34\" class=\"node node-leaf sub-sub_branch12\" style=\"left: 82%; top: 25%;\">Leaf 34 texto</div>\n            <div id=\"leaf35\" class=\"node node-leaf sub-sub_branch12\" style=\"left: 79%; top: 30%;\">Leaf 35 texto</div>\n            <div id=\"leaf36\" class=\"node node-leaf sub-sub_branch12\" style=\"left: 77%; top: 35%;\">Leaf 36 texto</div>\n            <!-- sub_branch13 -->\n            <div id=\"leaf37\" class=\"node node-leaf sub-sub_branch13\" style=\"left: 87%; top: 25%;\">Leaf 37 texto</div>\n            <div id=\"leaf38\" class=\"node node-leaf sub-sub_branch13\" style=\"left: 92%; top: 25%;\">Leaf 38 texto</div>\n            <div id=\"leaf39\" class=\"node node-leaf sub-sub_branch13\" style=\"left: 89%; top: 30%;\">Leaf 39 texto</div>\n            <div id=\"leaf40\" class=\"node node-leaf sub-sub_branch13\" style=\"left: 87%; top: 35%;\">Leaf 40 texto</div>\n            <!-- mainbranch4 Sub-branches & Leaves -->\n            <div id=\"sub_branch14\" class=\"node node-sub-branch sub-mainbranch4\" style=\"left: 80%; top: 40%;\">Sub Branch 14 texto</div>\n            <div id=\"sub_branch15\" class=\"node node-sub-branch sub-mainbranch4\" style=\"left: 90%; top: 45%;\">Sub Branch 15 texto</div>\n            <div id=\"sub_branch16\" class=\"node node-sub-branch sub-mainbranch4\" style=\"left: 80%; top: 60%;\">Sub Branch 16 texto</div>\n            <div id=\"sub_branch17\" class=\"node node-sub-branch sub-mainbranch4\" style=\"left: 90%; top: 65%;\">Sub Branch 17 texto</div>\n            <div id=\"sub_branch18\" class=\"node node-sub-branch sub-mainbranch4\" style=\"left: 85%; top: 52%;\">Sub Branch 18 texto</div>\n            <div id=\"leaf41\" class=\"node node-leaf node-leaf-concept\" style=\"left: 75%; top: 36%;\">Leaf 41 texto</div>\n            <div id=\"leaf42\" class=\"node node-leaf node-leaf-concept\" style=\"left: 85%; top: 36%;\">Leaf 42 texto</div>\n            <div id=\"leaf43\" class=\"node node-leaf node-leaf-concept\" style=\"left: 90%; top: 40%;\">Leaf 43 texto</div>\n            <div id=\"leaf44\" class=\"node node-leaf node-leaf-concept\" style=\"left: 85%; top: 50%;\">Leaf 44 texto</div>\n            <div id=\"leaf45\" class=\"node node-leaf node-leaf-concept\" style=\"left: 75%; top: 65%;\">Leaf 45 texto</div>\n            <div id=\"leaf46\" class=\"node node-leaf node-leaf-concept\" style=\"left: 90%; top: 70%;\">Leaf 46 texto</div>\n            <div id=\"leaf47\" class=\"node node-leaf node-leaf-concept\" style=\"left: 85%; top: 75%;\">Leaf 47 texto</div>\n            <div id=\"leaf48\" class=\"node node-leaf node-leaf-concept\" style=\"left: 75%; top: 45%;\">Leaf 48 texto</div>\n            <div id=\"leaf49\" class=\"node node-leaf node-leaf-concept\" style=\"left: 70%; top: 55%;\">Leaf 49 texto</div>\n            <!-- mainbranch5 Sub-branches & Leaves -->\n            <div id=\"sub_branch19\" class=\"node node-sub-branch sub-mainbranch5\" style=\"left: 20%; top: 40%;\">Sub Branch 19 texto</div>\n            <div id=\"sub_branch20\" class=\"node node-sub-branch sub-mainbranch5\" style=\"left: 10%; top: 55%;\">Sub Branch 20 texto</div>\n            <div id=\"sub_branch21\" class=\"node node-sub-branch sub-mainbranch5\" style=\"left: 25%; top: 60%;\">Sub Branch 21 texto</div>\n            <div id=\"sub_branch22\" class=\"node node-sub-branch sub-mainbranch5\" style=\"left: 35%; top: 45%;\">Sub Branch 22 texto</div>\n            <div id=\"sub_branch23\" class=\"node node-sub-branch sub-mainbranch5\" style=\"left: 40%; top: 55%;\">Sub Branch 23 texto</div>\n            <div id=\"leaf50\" class=\"node node-leaf node-leaf-concept\" style=\"left: 15%; top: 35%;\">Leaf 50 texto</div>\n            <div id=\"leaf51\" class=\"node node-leaf node-leaf-concept\" style=\"left: 25%; top: 35%;\">Leaf 51 texto</div>\n            <div id=\"leaf52\" class=\"node node-leaf node-leaf-concept\" style=\"left: 30%; top: 40%;\">Leaf 52 texto</div>\n            <div id=\"leaf53\" class=\"node node-leaf node-leaf-concept\" style=\"left: 40%; top: 40%;\">Leaf 53 texto</div>\n            <div id=\"leaf54\" class=\"node node-leaf node-leaf-concept\" style=\"left: 35%; top: 60%;\">Leaf 54 texto</div>\n            <!-- mainbranch6 Sub-branches & Leaves -->\n            <div id=\"sub_branch24\" class=\"node node-sub-branch sub-mainbranch6\" style=\"left: 55%; top: 75%;\">Sub Branch 24 texto</div>\n            <div id=\"sub_branch25\" class=\"node node-sub-branch sub-mainbranch6\" style=\"left: 65%; top: 70%;\">Sub Branch 25 texto</div>\n            <div id=\"sub_branch26\" class=\"node node-sub-branch sub-mainbranch6\" style=\"left: 75%; top: 75%;\">Sub Branch 26 texto</div>\n            <div id=\"sub_branch27\" class=\"node node-sub-branch sub-mainbranch6\" style=\"left: 60%; top: 85%;\">Sub Branch 27 texto</div>\n            <div id=\"sub_branch28\" class=\"node node-sub-branch sub-mainbranch6\" style=\"left: 70%; top: 90%;\">Sub Branch 28 texto</div>\n            <div id=\"leaf55\" class=\"node node-leaf node-leaf-concept\" style=\"left: 50%; top: 70%;\">Leaf 55 texto</div>\n            <div id=\"leaf56\" class=\"node node-leaf node-leaf-concept\" style=\"left: 60%; top: 65%;\">Leaf 56 texto</div>\n            <div id=\"leaf57\" class=\"node node-leaf node-leaf-concept\" style=\"left: 70%; top: 80%;\">Leaf 57 texto</div>\n            <div id=\"leaf58\" class=\"node node-leaf node-leaf-concept\" style=\"left: 55%; top: 90%;\">Leaf 58 texto</div>\n            <div id=\"leaf59\" class=\"node node-leaf node-leaf-concept\" style=\"left: 75%; top: 95%;\">Leaf 59 texto</div>\n\n            <!--\n            estes são apenas exemplo de formatação\n            use a quantidade necessaria para fazer o mapa\n            nomeando branches e leaves da forma que achar mais adequada\n            -->\n        </div>\n        <script>\n            // Function to get the center coordinates of a node\n            function getNodeCenter(nodeId) {\n                const node = document.getElementById(nodeId);\n                if (!node) return { x: 0, y: 0 };\n                const rect = node.getBoundingClientRect();\n                const containerRect = document.getElementById('mindMapContainer').getBoundingClientRect();\n                return {\n                    x: rect.left + rect.width / 2 - containerRect.left,\n                    y: rect.top + rect.height / 2 - containerRect.top\n                };\n            }\n            // Function to draw a line between two nodes\n            function drawLine(startNodeId, endNodeId, className, svgElement, isCurved = true) {\n                const start = getNodeCenter(startNodeId);\n                const end = getNodeCenter(endNodeId);\n                let pathData;\n                if (isCurved) {\n                    // Use a cubic bezier curve for a more organic feel\n                    const controlPointFactor = 0.5; // Adjust for more/less curve\n                    const cp1x = start.x + (end.x - start.x) * controlPointFactor;\n                    const cp1y = start.y;\n                    const cp2x = end.x - (end.x - start.x) * controlPointFactor;\n                    const cp2y = end.y;\n                    pathData = `M ${start.x} ${start.y} C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${end.x} ${end.y}`;\n                } else {\n                    pathData = `M ${start.x} ${start.y} L ${end.x} ${end.y}`;\n                }\n                const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');\n                path.setAttribute('d', pathData);\n                path.setAttribute('class', `line ${className}`);\n                svgElement.appendChild(path);\n            }\n            // Connect all nodes after the DOM is loaded\n            window.addEventListener('load', () => {\n                const svg = document.getElementById('mindMapSVG');\n                // Topic to Main Branches\n                drawLine('topic', 'mainbranch1', 'line-main', svg);\n                drawLine('topic', 'mainbranch2', 'line-main', svg);\n                drawLine('topic', 'mainbranch3', 'line-main', svg);\n                drawLine('topic', 'mainbranch4', 'line-main', svg);\n                drawLine('topic', 'mainbranch5', 'line-main', svg);\n                drawLine('topic', 'mainbranch6', 'line-main', svg);\n                // mainbranch1 to Sub-branches\n                drawLine('mainbranch1', 'sub_branch1', 'line-sub', svg, false);\n                drawLine('mainbranch1', 'sub_branch2', 'line-sub', svg, false);\n                drawLine('mainbranch1', 'sub_branch3', 'line-sub', svg, false);\n                drawLine('mainbranch1', 'sub_branch4', 'line-sub', svg, false);\n                drawLine('sub_branch1', 'leaf1', 'line-detail', svg, false);\n                drawLine('sub_branch1', 'leaf2', 'line-detail', svg, false);\n                drawLine('sub_branch1', 'leaf3', 'line-detail', svg, false);\n                drawLine('sub_branch2', 'leaf4', 'line-detail', svg, false);\n                drawLine('sub_branch2', 'leaf5', 'line-detail', svg, false);\n                drawLine('sub_branch3', 'leaf6', 'line-detail', svg, false);\n                drawLine('sub_branch3', 'leaf7', 'line-detail', svg, false);\n                drawLine('sub_branch4', 'leaf8', 'line-detail', svg, false);\n                drawLine('sub_branch4', 'leaf9', 'line-detail', svg, false);\n                // mainbranch2 to Sub-branches\n                drawLine('mainbranch2', 'sub_branch5', 'line-sub', svg, false);\n                drawLine('mainbranch2', 'sub_branch6', 'line-sub', svg, false);\n                drawLine('mainbranch2', 'sub_branch7', 'line-sub', svg, false);\n                drawLine('mainbranch2', 'sub_branch8', 'line-sub', svg, false);\n                drawLine('sub_branch5', 'leaf10', 'line-detail', svg, false);\n                drawLine('sub_branch5', 'leaf11', 'line-detail', svg, false);\n                drawLine('sub_branch6', 'leaf12', 'line-detail', svg, false);\n                drawLine('sub_branch6', 'leaf13', 'line-detail', svg, false);\n                drawLine('sub_branch7', 'leaf14', 'line-detail', svg, false);\n                drawLine('sub_branch8', 'leaf15', 'line-detail', svg, false);\n                drawLine('sub_branch8', 'leaf16', 'line-detail', svg, false);\n                // mainbranch3 to Sub-branches\n                drawLine('mainbranch3', 'sub_branch9', 'line-sub', svg, false);\n                drawLine('mainbranch3', 'sub_branch10', 'line-sub', svg, false);\n                drawLine('mainbranch3', 'sub_branch11', 'line-sub', svg, false);\n                drawLine('mainbranch3', 'sub_branch12', 'line-sub', svg, false);\n                drawLine('mainbranch3', 'sub_branch13', 'line-sub', svg, false);\n                // sub_branch9\n                drawLine('sub_branch9', 'leaf17', 'line-detail', svg, false);\n                drawLine('sub_branch9', 'leaf18', 'line-detail', svg, false);\n                drawLine('sub_branch9', 'leaf19', 'line-detail', svg, false);\n                drawLine('leaf17', 'leaf20', 'line-detail', svg, false);\n                drawLine('leaf18', 'leaf21', 'line-detail', svg, false);\n                drawLine('leaf19', 'leaf22', 'line-detail', svg, false);\n                // sub_branch10\n                drawLine('sub_branch10', 'leaf23', 'line-detail', svg, false);\n                drawLine('sub_branch10', 'leaf24', 'line-detail', svg, false);\n                drawLine('sub_branch10', 'leaf25', 'line-detail', svg, false);\n                drawLine('sub_branch10', 'leaf26', 'line-detail', svg, false);\n                drawLine('sub_branch10', 'leaf27', 'line-detail', svg, false);\n                drawLine('sub_branch10', 'leaf28', 'line-detail', svg, false);\n                // sub_branch11\n                drawLine('sub_branch11', 'leaf29', 'line-detail', svg, false);\n                drawLine('sub_branch11', 'leaf30', 'line-detail', svg, false);\n                drawLine('sub_branch11', 'leaf31', 'line-detail', svg, false);\n                drawLine('sub_branch11', 'leaf32', 'line-detail', svg, false);\n                // sub_branch12\n                drawLine('sub_branch12', 'leaf33', 'line-detail', svg, false);\n                drawLine('sub_branch12', 'leaf34', 'line-detail', svg, false);\n                drawLine('sub_branch12', 'leaf35', 'line-detail', svg, false);\n                drawLine('sub_branch12', 'leaf36', 'line-detail', svg, false);\n                // sub_branch13\n                drawLine('sub_branch13', 'leaf37', 'line-detail', svg, false);\n                drawLine('sub_branch13', 'leaf38', 'line-detail', svg, false);\n                drawLine('sub_branch13', 'leaf39', 'line-detail', svg, false);\n                drawLine('sub_branch13', 'leaf40', 'line-detail', svg, false);\n                // mainbranch4\n                drawLine('mainbranch4', 'sub_branch14', 'line-sub', svg, false);\n                drawLine('mainbranch4', 'sub_branch15', 'line-sub', svg, false);\n                drawLine('mainbranch4', 'sub_branch16', 'line-sub', svg, false);\n                drawLine('mainbranch4', 'sub_branch17', 'line-sub', svg, false);\n                drawLine('mainbranch4', 'sub_branch18', 'line-sub', svg, false);\n                drawLine('sub_branch14', 'leaf41', 'line-detail', svg, false);\n                drawLine('sub_branch14', 'leaf42', 'line-detail', svg, false);\n                drawLine('sub_branch15', 'leaf43', 'line-detail', svg, false);\n                drawLine('sub_branch15', 'leaf44', 'line-detail', svg, false);\n                drawLine('sub_branch16', 'leaf45', 'line-detail', svg, false);\n                drawLine('sub_branch17', 'leaf46', 'line-detail', svg, false);\n                drawLine('sub_branch17', 'leaf47', 'line-detail', svg, false);\n                drawLine('sub_branch18', 'leaf48', 'line-detail', svg, false);\n                drawLine('sub_branch18', 'leaf49', 'line-detail', svg, false);\n                // mainbranch5\n                drawLine('mainbranch5', 'sub_branch19', 'line-sub', svg, false);\n                drawLine('mainbranch5', 'sub_branch20', 'line-sub', svg, false);\n                drawLine('mainbranch5', 'sub_branch21', 'line-sub', svg, false);\n                drawLine('mainbranch5', 'sub_branch22', 'line-sub', svg, false);\n                drawLine('mainbranch5', 'sub_branch23', 'line-sub', svg, false);\n                drawLine('sub_branch19', 'leaf50', 'line-detail', svg, false);\n                drawLine('sub_branch19', 'leaf51', 'line-detail', svg, false);\n                drawLine('sub_branch22', 'leaf52', 'line-detail', svg, false);\n                drawLine('sub_branch22', 'leaf53', 'line-detail', svg, false);\n                drawLine('sub_branch23', 'leaf54', 'line-detail', svg, false);\n                // mainbranch6\n                drawLine('mainbranch6', 'sub_branch24', 'line-sub', svg, false);\n                drawLine('mainbranch6', 'sub_branch25', 'line-sub', svg, false);\n                drawLine('mainbranch6', 'sub_branch26', 'line-sub', svg, false);\n                drawLine('mainbranch6', 'sub_branch27', 'line-sub', svg, false);\n                drawLine('mainbranch6', 'sub_branch28', 'line-sub', svg, false);\n                drawLine('sub_branch24', 'leaf55', 'line-detail', svg, false);\n                drawLine('sub_branch25', 'leaf56', 'line-detail', svg, false);\n                drawLine('sub_branch26', 'leaf57', 'line-detail', svg, false);\n                drawLine('sub_branch27', 'leaf58', 'line-detail', svg, false);\n                drawLine('sub_branch28', 'leaf59', 'line-detail', svg, false);\n                // Complex Interconnections (lines between different branches)\n                drawLine('sub_branch10', 'sub_branch11', 'line-conceptual', svg);\n                drawLine('sub_branch10', 'sub_branch12', 'line-conceptual', svg);\n                drawLine('sub_branch10', 'sub_branch13', 'line-conceptual', svg);\n                drawLine('leaf19', 'sub_branch13', 'line-conceptual', svg);\n                drawLine('sub_branch23', 'mainbranch6', 'line-conceptual', svg);\n                drawLine('sub_branch22', 'mainbranch6', 'line-conceptual', svg);\n                drawLine('sub_branch21', 'sub_branch28', 'line-conceptual', svg);\n                drawLine('leaf31', 'sub_branch18', 'line-conceptual', svg);\n                drawLine('leaf31', 'leaf30', 'line-conceptual', svg);\n                drawLine('leaf24', 'leaf33', 'line-conceptual', svg);\n                drawLine('leaf26', 'leaf31', 'line-conceptual', svg);\n                drawLine('leaf27', 'leaf49', 'line-conceptual', svg);\n                drawLine('mainbranch1', 'mainbranch2', 'line-conceptual', svg);\n                drawLine('mainbranch3', 'mainbranch4', 'line-conceptual', svg);\n                drawLine('mainbranch5', 'mainbranch3', 'line-conceptual', svg);\n                drawLine('mainbranch6', 'mainbranch4', 'line-conceptual', svg);\n            });\n        </script>\n    </body>\n</html>"
    complementos.append("use o seguinte modelo como base para a criação do mapa, o tamanho, a quantidade de itens e o esquema de cores devem ser escolhidos para se adequar melhor ao tema\n\n")

    complementos.append(example)
    diretrizes = f"Diretrizes de ensino: {' '.join(complementos)}"
    return diretrizes