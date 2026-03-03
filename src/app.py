import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, session, redirect, url_for, flash
from storage import listar_perfis, carregar_perfil, salvar_perfil
from generator import configurar_cliente, gerar_exemplo, gerar_exercicio, gerar_explicacao, gerar_visual

load_dotenv()

app = Flask(__name__)
app.secret_key = "uma_chave_secreta_qualquer"

@app.route("/", methods=["GET", "POST"])
def index():
    
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:    
        flash("GEMINI_API_KEY não encontrada no arquivo .env", "error")
        return render_template("index.html", perfis=perfis, resultado=None)
    client = configurar_cliente(api_key)


    perfis = listar_perfis()
    resultado = None
    criando_perfil = request.args.get('novo_perfil') == '1'

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
            salvar_perfil(novo_p)
            session['perfil'] = novo_p
            return redirect(url_for('index'))

        # Ação: Gerar Conteúdo
        elif acao in ["explicação", "exemplo", "exercício", "visual"]:
            topico = request.form.get("topico")
            perfil = session.get('perfil')
            if acao == "explicação":
                resultado = gerar_explicacao(client, topico, perfil)
            elif acao == "exemplo":
                resultado = gerar_exemplo(client, topico, perfil)
            elif acao == "exercício":
                resultado = gerar_exercicio(client, topico, perfil)
            elif acao == "visual":
                resultado = gerar_visual(client, topico, perfil)

    return render_template("index.html", 
                           perfis=perfis, 
                           perfil_ativo=session.get('perfil'), 
                           criando_perfil=criando_perfil,
                           resultado=resultado)

@app.route("/limpar")
def limpar():
    session.pop('perfil', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)