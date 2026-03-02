# app.py
from flask import Flask, render_template, request, jsonify
from generator import gerar_exemplo, gerar_exercicio, gerar_explicacao
from storage import carregar_perfil, deletar_perfil, listar_perfis, salvar_perfil


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        # Pega os dados enviados pelo formulário HTML
        topico = request.form.get('topico')
        perfil = {
            "nome": request.form.get('nome'),
            "idade": request.form.get('idade'),
            "nivel": request.form.get('nivel'),
            "estilo_aprendizagem": request.form.get('estilo')
        }
        # Salva o perfil do aluno
        salvar_perfil(perfil)

        ### muitos codigos
        resultado = None

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)