import os
import re
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, flash
from storage import atualizar_perfil, deletar_perfil, listar_perfis, carregar_perfil, salvar_perfil
from generator import configurar_cliente, gerar_exemplo, gerar_exercicio, gerar_explicacao, gerar_visual

load_dotenv()

app = Flask(__name__)
app.secret_key = "uma_chave_secreta_qualquer"

@app.route("/", methods=["GET", "POST"])
def index():
    
    perfis = listar_perfis()
    resultado = None
    criando_perfil = request.args.get('novo_perfil') == '1'
    deletar_solicitado = request.args.get('deletar_perfil') == '1'

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:    
        flash("GEMINI_API_KEY não encontrada no arquivo .env", "error")
        return render_template("index.html", perfis=perfis, resultado=None)
    client = configurar_cliente(api_key)


    if deletar_solicitado:
        perfil = session.get('perfil')
        if perfil:
            nome_para_deletar = perfil.get('nome')
            deletar_perfil(nome_para_deletar)
            session.pop('perfil', None)
        return redirect(url_for('index'))

    if request.method == "POST":
        acao = request.form.get("acao")

        # Ação: Selecionar Perfil Existente
        if acao == "selecionar":
            nome_perfil = request.form.get("perfil_selecionado")
            session['perfil'] = carregar_perfil(nome_perfil)
        
        # Ação: Salvar Novo Perfil
        elif acao == "salvar_novo":

            novo_p = {
                "nome": request.form.get("nome"),
                "idade": int(request.form.get("idade")),
                "nivel": request.form.get("nivel"),
                "estilo_aprendizagem": request.form.get("estilo")
            }

            if session.get('perfil'):
                atualizar_perfil(session['perfil']['nome'], novo_p)
            else:
                salvar_perfil(novo_p)

            session['perfil'] = novo_p
            return redirect(url_for('index'))

        elif acao == "deletar_perfil":
            if session.get('perfil'):
                deletar_perfil(session['perfil']['nome'])
                session.pop('perfil', None)

        # Ação: Gerar Conteúdo
        elif acao in ["explicação", "exemplo", "exercício", "visual"]:
            topico = request.form.get("topico")
            perfil = session.get('perfil')
            if acao == "explicação":
                resultado = formatar_resultado(gerar_explicacao(client, topico, perfil))
            elif acao == "exemplo":
                resultado = formatar_resultado(gerar_exemplo(client, topico, perfil))
            elif acao == "exercício":
                resultado = formatar_resultado(gerar_exercicio(client, topico, perfil))
            elif acao == "visual":
                resultado = formatar_mapa(gerar_visual(client, topico, perfil))

    return render_template("index.html", 
                           perfis=perfis, 
                           perfil_ativo=session.get('perfil'), 
                           criando_perfil=criando_perfil,
                           resultado=resultado)

@app.route("/limpar")
def limpar():
    session.pop('perfil', None)
    return redirect(url_for('index'))

def formatar_resultado(texto):
    # 1. Transforma Negrito: **texto** em <strong>texto</strong>
    texto = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', texto)
    
    # 2. Sub-tópicos (identados com 4 espaços):     * item -> <li class="sub-item">
    # Procuramos por 4 espaços seguidos de asterisco
    texto = re.sub(r'(?m)^ {4}[*|-]\s+(.*)$', r'<li class="sub-item">\1</li>', texto)
    
    # 3. Tópicos principais (sem espaço no início): * item -> <li class="main-item">
    texto = re.sub(r'(?m)^[*|-]\s+(.*)$', r'<li class="main-item">\1</li>', texto)

    return texto

def formatar_mapa(texto):
    texto = texto.replace("body {", ".mapa-mental {")
    estilo = re.search(r'<style>(.*?)</style>', texto, re.DOTALL)
    # Extrai apenas o conteúdo do mapa
    corpo = re.search(r'<body>.*?</body>', texto, re.DOTALL)
    # Extrai o Script
    script = re.search(r'<script>(.*?)</script>', texto, re.DOTALL)

    res = ""
    if estilo: res += f"<style>{estilo.group(1)}</style>"
    
    # Envolvemos em uma div com overflow para o scroll funcionar
    if corpo: res += f'<div class="mapa-container">{corpo.group(0)}</div>'
    if script: res += f"<script>{script.group(1)}</script>"

    return res

if __name__ == "__main__":
    app.run(debug=True)