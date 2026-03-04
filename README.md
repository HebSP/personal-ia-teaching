# personal-ia-teaching

An educational platform that uses artificial intelligence and prompt engineering to provide individualized instruction based on the student's profile.

## Visão geral

personal-ia-teaching é uma pequena aplicação Python que gera conteúdo educativo (explicações, exemplos, exercícios e mapas mentais) adaptados ao perfil do aluno usando a API Gemini (Google GenAI). A aplicação oferece:

- Interface web com Flask ([`app.index`](src/app.py), template em [src/templates/index.html](src/templates/index.html)).
- Interface CLI interativa ([`cli.main`](src/cli.py)).
- Gerador de prompts personalizados ([`prompts.gerar_prompt_explicacao`](src/prompts.py), [`prompts.gerar_prompt_exemplo`](src/prompts.py), [`prompts.gerar_prompt_exercicio`](src/prompts.py), [`prompts.gerar_prompt_visual_html`](src/prompts.py), [`prompts.gerar_prompt_visual_cli`](src/prompts.py)).
- Comunicação com Gemini via cliente em [`generator.configurar_cliente`](src/generator.py) e chamadas em [`generator.call_api`](src/generator.py).
- Cache local para respostas geradas ([`cache.buscar_na_cache`](src/cache.py), [`cache.salvar_na_cache`](src/cache.py)).
- Armazenamento simples de perfis em JSON ([`storage.salvar_perfil`](src/storage.py), [`storage.carregar_perfil`](src/storage.py), [`storage.listar_perfis`](src/storage.py), [`storage.deletar_perfil`](src/storage.py), [`storage.atualizar_perfil`](src/storage.py)).

## Instalação

1. Clone o repositório (já está no workspace).
2. Crie um ambiente virtual e instale dependências:

```bash
python -m venv .venv
source .venv/bin/activate    # Linux / macOS
# .venv\Scripts\activate     # Windows (PowerShell)
pip install -r requirements.txt
```

Arquivos de dependência:
- [requirements.txt](requirements.txt)

## Variáveis de ambiente

Copie o exemplo e preencha suas chaves:

```bash
cp .env.example .env
# edite .env e adicione sua chave GEMINI_API_KEY e FLASK_SECRET_KEY
```

Arquivos relevantes:
- [.env.example](.env.example)
- [.env](.env) (NÃO commite este arquivo com suas chaves)

Variáveis esperadas:
- GEMINI_API_KEY — chave para a API Gemini (usada por [`generator.configurar_cliente`](src/generator.py)).
- FLASK_SECRET_KEY — segredo do Flask para sessões.

## Executando

Web (Flask)
```bash
python src/app.py
# Acesse http://127.0.0.1:5000
```

CLI
```bash
python src/cli.py
```

Principais pontos de entrada:
- [`app.index`](src/app.py) — rota web principal.
- [`cli.main`](src/cli.py) — modo CLI interativo.

## Estrutura do projeto

Arquivos e diretórios principais:
- [.env](.env)
- [.env.example](.env.example)
- [.gitignore](.gitignore)
- [LICENSE](LICENSE)
- [README.md](README.md)
- [requirements.txt](requirements.txt)
- [cache/cache.json](cache/cache.json) — arquivo de cache gerado em runtime.
- [storage/profiles.json](storage/profiles.json) — armazenamento de perfis (criado/alterado em runtime).
- [src/app.py](src/app.py) — aplicação Flask e renderização.
- [src/cli.py](src/cli.py) — interface de linha de comando.
- [src/generator.py](src/generator.py) — integra prompts, chamadas à API e cache (`generator.configurar_cliente`, `generator.call_api`, `generator.gerar_explicacao`, `generator.gerar_exemplo`, `generator.gerar_exercicio`, `generator.gerar_visual_cli`, `generator.gerar_visual_html`).
- [src/prompts.py](src/prompts.py) — criação de prompts personalizados (`prompts.gerar_prompt_explicacao`, `prompts.gerar_prompt_exemplo`, `prompts.gerar_prompt_exercicio`, `prompts.gerar_prompt_visual_CLI`, `prompts.gerar_prompt_visual_HTML`).
- [src/cache.py](src/cache.py) — funções de cache (`cache.buscar_na_cache`, `cache.salvar_na_cache`, `cache.limpar_cache`).
- [src/storage.py](src/storage.py) — CRUD de perfis (`storage.salvar_perfil`, `storage.carregar_perfil`, `storage.listar_perfis`, `storage.deletar_perfil`, `storage.atualizar_perfil`).
- [src/templates/index.html](src/templates/index.html) — template principal.
- [src/static/style.css](src/static/style.css) — estilos da interface.

## Como funciona (fluxo curto)

1. O usuário cria ou seleciona um perfil (idade, nível, estilo de aprendizagem).
2. O usuário solicita um tópico e escolhe tipo de conteúdo (explicação, exemplo, exercício, visual).
3. O módulo de prompts gera um prompt adaptado ao perfil ([`prompts.*`](src/prompts.py)).
4. O [`generator`](src/generator.py) verifica o cache ([`cache.buscar_na_cache`](src/cache.py]); se não houver, chama a API Gemini ([`generator.call_api`](src/generator.py]) e salva o resultado no cache ([`cache.salvar_na_cache`](src/cache.py]).
5. Resultado é formatado e apresentado na interface web ou CLI.

## Observações de desenvolvimento

- Ao editar prompts, veja [src/prompts.py](src/prompts.py).
- Para ajustar mapeamento de formatos e parsing do resultado veja [`app.formatar_resultado`](src/app.py) e [`app.formatar_mapa`](src/app.py).
- Cache e storage são persistidos localmente em `cache/cache.json` e `storage/profiles.json`. Cuidado ao compartilhar estes arquivos.

## Segurança e boas práticas

- Nunca commit suas chaves API no repositório (.env está no .gitignore).
- Limite uso e trate erros de chamadas externas (a implementação atual assume sucesso da API).
- Proteja o FLASK_SECRET_KEY em ambientes de produção.

## Licença

Este projeto usa a licença MIT. Veja [LICENSE](LICENSE).

## Contato e contribuição

Bug reports e pull requests são bem-vindos. Ao contribuir, mantenha chaves e dados sensíveis
