import json
import os
from datetime import datetime

STORAGE_DIR = "storage"
PROFILES_FILE = os.path.join(STORAGE_DIR, "profiles.json")

def _inicializar_storage():
    """
    Inicializa o diretório de storage se não existir.
    """
    if not os.path.exists(STORAGE_DIR):
        os.makedirs(STORAGE_DIR)
    
    if not os.path.exists(PROFILES_FILE):
        with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
            json.dump({}, f)

def _carregar_perfis():
    """
    Carrega todos os perfis do arquivo JSON.
    """
    _inicializar_storage()
    with open(PROFILES_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def _salvar_perfis(dados):
    """
    Salva os perfis no arquivo JSON.
    """
    _inicializar_storage()
    with open(PROFILES_FILE, 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)

def salvar_perfil(perfil):
    """
    Salva um novo perfil de usuário.
    """
    perfis = _carregar_perfis()
    nome = perfil.get('nome')
    perfis[nome] = {
        **perfil,
        "data_criacao": datetime.now().isoformat()
    }
    _salvar_perfis(perfis)

def carregar_perfil(nome):
    """
    Carrega um perfil específico pelo nome.
    """
    perfis = _carregar_perfis()
    return perfis.get(nome)

def listar_perfis():
    """
    Retorna lista de todos os perfis disponíveis.
    """
    perfis = _carregar_perfis()
    return list(perfis.keys())

def deletar_perfil(nome):
    """
    Deleta um perfil existente.
    """
    perfis = _carregar_perfis()
    if nome in perfis:
        del perfis[nome]
        _salvar_perfis(perfis)
        return True
    return False

def atualizar_perfil(nome, dados_atualizados):
    """
    Atualiza dados de um perfil existente.
    """
    perfis = _carregar_perfis()
    if nome in perfis:
        perfis[nome].update(dados_atualizados)
        _salvar_perfis(perfis)
        return True
    return False