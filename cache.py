import json
import os
from datetime import datetime

CACHE_DIR = "cache"
CACHE_FILE = os.path.join(CACHE_DIR, "cache.json")

def _inicializar_cache():
    """
    Inicializa o diretório de cache se não existir.
    """
    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)
    
    if not os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def _carregar_cache():
    """
    Carrega o arquivo de cache em memória.
    """
    _inicializar_cache()
    with open(CACHE_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def _salvar_cache(dados):
    """
    Salva dados no arquivo de cache.
    """
    _inicializar_cache()
    with open(CACHE_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def buscar_na_cache(topico, perfil, tipo):
    """
    Busca uma resposta no cache baseado em topico, perfil e tipo de conteúdo.
    """
    cache = _carregar_cache()
    chave = f"{topico}_{str(perfil.get('idade', 0))}_{perfil.get('nivel', 'default')}_{perfil.get('estilo_aprendizagem', 'default')}_{tipo}"
    return cache.get(chave)

def salvar_na_cache(topico, perfil, tipo, resposta):
    """
    Salva uma resposta no cache.
    """
    cache = _carregar_cache()
    chave = f"{topico}_{str(perfil.get('idade', 0))}_{perfil.get('nivel', 'default')}_{perfil.get('estilo_aprendizagem', 'default')}_{tipo}"
    cache[chave] = {
        "resposta": resposta,
        "data": datetime.now().isoformat()
    }
    _salvar_cache(cache)

def limpar_cache():
    """
    Limpa todo o arquivo de cache.
    """
    _salvar_cache({})