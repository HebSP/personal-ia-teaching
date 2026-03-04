# Notas de Prompt Engineering — personal-ia-teaching

Este documento descreve o processo utilizado para projetar, validar e iterar os prompts do projeto personal-ia-teaching. O foco aqui é explicar *como* as decisões foram tomadas, quais experimentos foram feitos e quais práticas foram adotadas para garantir saídas previsíveis e fáceis de parsear.

## Objetivo do processo
- Produzir prompts que gerem: explicações, exemplos, exercícios e mapas mentais adaptados ao perfil do aluno.
- Garantir consistência entre interfaces (web/CLI).
- Maximizar a confiabilidade do formato da saída para facilitar pós-processamento (parsing, cache, renderização).

## Principais decisões de design (resumo)
- Idioma: Português (pt-BR) — padronização para consistência.
- Saída restrita: sempre que possível pedir "De apenas X sem nenhum texto adicional." para reduzir ruído.
- Formatos específicos: texto estruturado com markdown/asteriscos para web; ASCII limitado para CLI; HTML completo (style/body/script) para mapas visuais.
- Indexação de cache: topico+idade+nivel+estilo+tipo — contrato que assume formato estável.

## Metodologia passo a passo
1. Pesquisa e definição de requisitos
   - Mapear saídas esperadas por tipo (explicação, exemplo, exercício, visual).
   - Identificar restrições técnicas do app (como o parser de mapas HTML e o limite de largura ASCII).

2. Definição de personas e variáveis do perfil
   - Variáveis usadas: idade, nível (Iniciante/Intermediário/Avançado), estilo de aprendizagem.
   - Traduzir essas variáveis em instruções concretas (ex.: "usar analogias visuais" para estilo Visual).

3. Estrutura do template-base do prompt
   - Persona
   - Tarefa
   - Diretrizes
   - Pedido de formato estrito
   - Modelo de saida (quando necessário)

4. Implementação iterativa
   - Gerar amostras com variações (temperatura, formulação do prompt) e coletar saídas.
   - Medir: conformidade de formato, legibilidade, adequação ao nível do aluno, minimização de conteúdo irrelevante.

5. Validação
   - Regras simples para checar formato:
     - Mapas HTML: procurar por tags.
     - ASCII: verificar largura máxima e níveis de indentação.
     - Texto estruturado: presença de bullets, negrito (**) quando solicitado.
   - Aprimorar os prompts para garatir que as respostas cheguem no formato esperado

6. Integração com cache e interface
   - Manter o contrato de saída: mudanças de formato exigem invalidar cache.
   - Expor no app instruções mínimas para o parser (por ex., formatos de marcação aceitos).

## Decisões concretas e justificativas
- Pedir saídas restritas ("De apenas...") reduz texto introdutório do modelo e facilita parsing automático.
- Separar persona e diretrizes nos helpers (_persona_e_papel, _diretrizes*) torna o prompt modular e testável.
- Usar exemplos de HTML completo nos prompts de mapa visual reduz a chance do modelo retornar mapas em formatos estranhos.
- Limitar tamanho (número de bullets, largura ASCII) evita conteúdo truncado e melhora usabilidade em telas.

## Exemplos de templates finais
### Prompts de exemplo — aluno: 25 anos, conhecimento avançado, estilo Visual

A seguir estão os prompts organizados e formatados. Os textos dos prompts montados para esse aluno em especifico; comentários explicativos e a estruturação foram aprimorados para leitura.

#### Persona e papel
Descrição: esta primeira parte define a persona da IA e o papel a ser desempenhado, específica para um aluno de 25 anos, nível avançado e preferência visual. essa parte é igual em todos os prompts e varia pra cada perfil de aluno.

```

Você é um tutor com boa didática especializado em ensino superior,e vai ensinar sobre topico para um aluno que possui um conhecimento aprofundado, que tem 25 anos e prefere um estilo de aprendizagem Visual.
```

#### Observação sobre a tarefa
Cada tarefa sempre inicia pedindo para analisar passo a passo como a resposta deve ser montada; a formulação específica varia conforme o tipo de saída desejada.

#### Sobre as diretrizes
Esta parte especifica o tom, o formato, as regras e as restrições que a resposta deve obedecer. Direta objetiva e reutilizável entre prompts, normalmente apenas acrescentando uma ou duas linhas as diretrises ficam completas para cada tipo de prompt, exceto os visuais que precisam de diretrizes mais especificas.

---

#### Exemplo (tarefa + diretrizes)
Tarefa: analisar e criar um exemplo prático; primeiro descreve-se o cenário, depois fornece-se o exemplo estruturado.

```
Analise passo a passo e encontre a melhor forma de criar um exemplo prático sobre o tema 'topico' para este aluno.
Primeiro, descreva brevemente o cenário que você vai criar para o exemplo, e depois forneça o exemplo prático estruturado.
```

Diretrizes: formato, estilo e restrições finais.

```
Diretrizes de ensino: Use analogias visuais fortes, descreva cenas ou sugira diagramas simples.
Promova discussões profundas e análise crítica.
Estruture a resposta usando bullet points, negrito para destacar palavras-chave e tópicos bem organizados.
Considere que o aluno é um adulto e possui um conhecimento avançado, use vocabulário e exemplos adequados.

De apenas o exemplo prático sem nenhum texto adicional.
```

---

#### Exercício (tarefa + diretrizes)
Tarefa: criar exercício de fixação que estimule pensamento crítico.

```
Analise passo a passo e encontre a melhor forma de criar um exercício de fixação sobre o tema 'topico' para este aluno, com perguntas que estimulem o pensamento crítico.
```

Diretrizes: formato e tom.

```
Diretrizes de ensino: Use analogias visuais fortes, descreva cenas ou sugira diagramas simples.
Promova discussões profundas e análise crítica.
Estruture a resposta usando bullet points, negrito para destacar palavras-chave e tópicos bem organizados.
Considere que o aluno é um adulto e possui um conhecimento avançado, use vocabulário e exemplos adequados.

O exercicio deve estimular o pensamento critico.
De apenas o exercício de fixação sem nenhum texto adicional.
```

---

#### Explicação (tarefa + diretrizes)
Tarefa: explicar o tema; incluir uma frase breve justificando a analogia visual.

```
Analise passo a passo e encontre a melhor forma de explicar o tema 'topico' para este aluno.
Explique sua lógica de escolha da analogia visual em uma frase breve, e depois forneça a explicação estruturada.
```

Diretrizes: estilo e formato.

```
Diretrizes de ensino: Use analogias visuais fortes, descreva cenas ou sugira diagramas simples.
Promova discussões profundas e análise crítica.
Estruture a resposta usando bullet points, negrito para destacar palavras-chave e tópicos bem organizados.
Considere que o aluno é um adulto e possui um conhecimento avançado, use vocabulário e exemplos adequados.

De apenas a explicação sem nenhum texto adicional.
```

---

#### Mapa mental em ASCII (tarefa + diretrizes)
Tarefa: revisar conceitos e ligações; fornecer mapa mental em ASCII com largura adequada.

```
Analise passo a passo e encontre a melhor forma de criar um mapa mental sobre o tema 'topico' para este aluno.
Primeiro, revise cada conceito e suas ligações no mapa que você vai criar, e depois forneça a representação visual estruturada.
```

Diretrizes: layout espacial, hierarquia e limite de largura.

```
Diretrizes de ensino: Foque em um layout espacial claro, usando símbolos para mostrar hierarquia.
Crie um mapa mental denso, mostrando interconexões complexas entre os vários conceitos relacionados.
Considere que o aluno é um adulto e possui um conhecimento avançado, use vocabulário e conceitos adequados.
Lembre-se de que o mapa mental deve ter largura adequada ao tamanho de uma tela comum de computador com 200 caracteres de largura.
De apenas a representação visual como um mapa mental em ascii sem nenhum texto adicional.
```

---

#### Mapa mental em HTML (tarefa + diretrizes)
Tarefa: revisar conceitos e ligações; fornecer mapa mental em HTML completo.

```
Analise passo a passo e encontre a melhor forma de criar um mapa mental sobre o tema 'topico' para este aluno.
Primeiro, revise cada conceito e suas ligações no mapa que você vai criar, e depois forneça a representação visual estruturada usando recursos de HTML.
```

Diretrizes: usar modelo base, escolher tamanho, quantidade de itens e esquema de cores adequados.

```
Diretrizes de ensino: Foque em um layout espacial claro, usando símbolos para mostrar hierarquia.
Crie um mapa mental denso, mostrando interconexões complexas entre os vários conceitos relacionados.
Considere que o aluno é um adulto e possui um conhecimento avançado, use vocabulário e conceitos adequados.
use o seguinte modelo como base para a criação do mapa, o tamanho, a quantidade de itens e o esquema de cores devem ser escolhidos para se adequar melhor ao tema

{exemplo em HTML}
De apenas a representação visual como um mapa mental em html sem nenhum texto adicional.
```

## Testes e checklist de validação
- Formato
  - [x] HTML contém as tags adequadas quando solicitado.
  - [x] ASCII respeita largura máxima definida.
  - [x] Texto estruturado usa bullets e **negrito** quando exigido.
- Conteúdo
  - [x] Adequado ao nível/idade do perfil.
  - [x] Não há texto introdutório adicional (ex: "Segue abaixo:").
  - [x] Exatidão básica do conteúdo (checagem manual ou por prompts de verificação).
- Operacional
  - [x] Resultado indexado no cache com a chave correta.
  - [x] Parser do app consegue extrair e renderizar o conteúdo sem erros.


## Riscos, limitações e mitigação
- Risco: modelos podem ignorar instruções estritas — mitigação: usar exemplos de saída e heurísticas de validação; re-enviar prompt com instruções de correção.
- Risco: mudança de modelo ou configuração (p.ex. temperatura) altera comportamento — mitigação: revalidar e, se necessário, ajustar templates e invalidar cache.
- Limitação: heurísticas não substituem revisão humana; manter amostras manuais para avaliação qualitativa.

## Conclusão
O processo adotado prioriza um contrato de saída estável, iteração rápida e validações heurísticas que permitem ao app integrar respostas automatizadas de forma confiável. Ajustes devem acompanhar mudanças de modelo, requisitos de UI ou novos formatos de saída.
