# Projeto 01

## Identificação

| | |
|---|---|
| **Nome da equipe** | Projeto 01 |
| **Integrantes** | Victor Cavalcante da Silva |
| **Mentor** | |
| **Tema** | Radar de Fracionamento |
| **Repositório GitHub** | https://github.com/Victor-CSilva/Projeto01-Next |

---

## 1. Problema de negócio

Escreva em 2–4 frases. Tema não é problema: o problema diz **quem decide, o que decide, e com que informação decidiria melhor**. Evite "analisar X" — prefira "a organização Y precisa decidir Z, mas hoje decide sem W".

"A secretaria estadual de saúde de PE precisa decidir onde reforçar equipes antes da próxima temporada de dengue, mas hoje decide sem histórico consolidado de internações por município."_

```
A Neoenergia Pernambuco precisa decidir quais titulares abrir a fiscalização para verificar o descumprimento da REN ANEEL nº 1.000/2021, que proíbe dividir uma central geradora para obter benefício indevido. Precisa-se definir uma ordem de prioridade de fiscalização, mas hoje depende de análise manual e de cruzamento complexo.
```

---

## 2. Público / decisor

Quem usa o dashboard e toma a decisão? Cargo ou papel concreto (secretário, gerente de logística, comandante de policiamento), não "a sociedade". É para essa pessoa que o pitch "vende a solução".

```
Os fiscais e analistas utilizarão o dashboard para verificar a ordem de prioridade de fiscalização.
```

---

## 3. Perguntas analíticas

No mínimo 3, respondíveis com os dados escolhidos. Uma pergunta respondível tem recorte claro (onde, quando, o quê) e o dado necessário existe na fonte. O CP1 verifica que ao menos 3 continuam respondíveis com os dados **reais**.

| # | Pergunta | Que decisão ela informa? | Respondível com os dados? (verificado na amostra) |
|---|---|---|---|
| 1 | Quais titulares concentram múltiplos empreendimentos no mesmo município, com potência somada cruzando o limiar de microgeração? | Quais titulares estão descumprindo a Resolução Normativa da ANEEL nº1000/2021 | Sim |
| 2 | As conexões aparecem próximas ao tempo - o fracionamento tem assinatura temporal? | Caso as centrais geradoras tenham sido conectadas juntas | Sim |
| 3 | Que fonte, classe e subgrupo concentram os casos? | Qual o tipo de fonte de energia, classe e subgrupo tem os maiores volumes de casos. | Sim |
| 4 (opcional) | Quanta potência está sob suspeita em PE, e como isso se compara às outras distribuidoras? | O quanto Pernambuco está descumprindo a regra imposta pela ANEEL em comparação com outros estados e concessionárias de energia | Sim |
| 5 (opcional) | | | |

---

## 4. Fontes de dados

Uma linha por fonte. A amostra precisa ter sido **baixada e aberta hoje** — coluna a coluna. Lembrete: se a fonte tiver API, a coleta usa API (requisito do M3). Troca de fonte é livre até o E3 (21/09); depois, só com a coordenação.

| Fonte | Link | Formato | Volume estimado | Licença/acesso | Amostra baixada e aberta? (sim/não) | Colunas-chave confirmadas na amostra |
|---|---|---|---|---|---|---|
| Dados Abertos ANEEL | dadosabertos.aneel.gov.br/dataset/relacao-de-empreendimentos-de-geracao-distribuida | CSV | | | | |
| | | | | | | |

---

## 5. Escopo e entregáveis — a regra do fatiável

Defina primeiro a fatia mínima: o menor recorte que ainda exercita o ciclo completo (banco → pipeline → análise → dashboard). Ela é o compromisso da equipe. As extensões só entram se a fatia mínima estiver pronta — e nada entra após o congelamento de escopo (05/10).

**Fatia mínima (compromisso):**

```
(ex.: internações por dengue em PE, 2021–2025, com dashboard de evolução e custo por município)
```

**Extensões desejáveis (apenas se sobrar tempo):**

```
(ex.: ampliar para o Nordeste; incluir cobertura vacinal)
```

**Fora de escopo (o que decidimos NÃO fazer):**

```
(ex.: previsão com machine learning; dados de outros agravos)
```

---

## 6. Riscos e mitigação

Ao menos 3 riscos do **seu** projeto (não genéricos). Consulte a tabela de riscos comuns no [`guia-do-projeto.md`](guia-do-projeto.md).

| Risco | Sinal precoce | Mitigação | Responsável por monitorar |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

---

## 7. Divisão de papéis

Todos codificam — papéis distribuem responsabilidade de acompanhamento, não exclusividade de execução. Cada papel tem uma pessoa sombra (backup). Em equipes de 4, coordenação acumula com outro papel; em equipes de 5–6, dados/pipeline e análise podem ser duplicados.

| Papel | Titular | Sombra |
|---|---|---|
| Coordenação de projeto | | |
| Dados / pipeline | | |
| Análise | | |
| Visualização / pitch | | |

**Canal de comunicação da equipe (fora do horário de aula):**

```
(ex.: grupo no WhatsApp + board no GitHub Projects)
```

---

## Validação do mentor (preenchida pelo mentor no E2)

| | |
|---|---|
| **Status** | ( ) Aprovado ( ) Aprovado com ajustes ( ) Devolvido com pendências |
| **Data** | |
| **Amostra baixada e aberta verificada?** | ( ) Sim ( ) Não |
| **Pendências (com prazo até o E3 — seg 21/09)** | |
