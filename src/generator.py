from prompts import gerar_prompt_exemplo, gerar_prompt_exercicio, gerar_prompt_explicacao, gerar_prompt_visual_html
from cache import buscar_na_cache, salvar_na_cache
from google import genai

def configurar_cliente(api_key):
    """
    Configura o cliente da API Gemini com a chave fornecida.
    """
    return genai.Client(api_key=api_key)

def call_api(client, prompt):
    """
    Chama a API Gemini com o prompt gerado e retorna a resposta.
    """
    resposta = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt
        )
    return resposta.text

def gerar_explicacao(client, topico, perfil):
    """
    Gera uma explicação conceitual usando a API.
    """
    cache_result = buscar_na_cache(topico, perfil, "explicacao")
    if cache_result:
        return cache_result['resposta']
    prompt = gerar_prompt_explicacao(topico, perfil)
    resposta = call_api(client, prompt)
    salvar_na_cache(topico, perfil, "explicacao", resposta)
    return resposta


def gerar_exemplo(client, topico, perfil):
    """
    Gera um exemplo prático usando a API.
    """
    cache_result = buscar_na_cache(topico, perfil, "exemplo")
    if cache_result:
        return cache_result['resposta']
    prompt = gerar_prompt_exemplo(topico, perfil)
    resposta = call_api(client, prompt)
    salvar_na_cache(topico, perfil, "exemplo", resposta)
    return resposta

def gerar_exercicio(client, topico, perfil):
    """
    Gera um exercício de fixação usando a API.
    """
    cache_result = buscar_na_cache(topico, perfil, "exercicio")
    if cache_result:
        return cache_result['resposta']
    prompt = gerar_prompt_exercicio(topico, perfil)
    resposta = call_api(client, prompt)
    salvar_na_cache(topico, perfil, "exercicio", resposta)
    return resposta

def gerar_visual(client, topico, perfil):
    """
    Gera um recurso visual usando a API.
    """
    cache_result = buscar_na_cache(topico, perfil, "visual")
    if cache_result:
        return cache_result['resposta']
    prompt = gerar_prompt_visual_html(topico, perfil)
    resposta = call_api(client, prompt)
    salvar_na_cache(topico, perfil, "visual", resposta)
    return resposta