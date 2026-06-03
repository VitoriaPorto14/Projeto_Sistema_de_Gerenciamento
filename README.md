# StockFlow - Estoque de Restaurante

## **Design Thinking (Ideação e Briefing)**

_**Briefing:**_ "Trabalho com produtos perecíveis. Preciso cadastrar os ingredientes e a data de validade. Se um ingrediente vencer em menos de 3 dias, o sistema deve mostrar um alerta em destaque. Quando eu vender um 'Prato Feito', o sistema deve tirar automaticamente 200g de arroz e 100g de feijão do estoque."

___

**_Requisitos pedidos:_**
 - O progrma deve permitir o cadastro de ingredientes contendo, nome do produto/ingrediente, data de validade, quantidade (em gramas)
 - O programa deve analisar o menu para que se algum alimento estiver para vencer nos próximos 3 dias deve aparecer um alerta
 - Quando um pedido for registrado (definido como 'Prato Feito') deve ser retirado do estoque automaticamente:
    - 200g de Arooz
    - 100g de Feijão
- E o progrma deve proibir vendas se algum item faltar

___

**_Design:_** O design será simples, toda em CLI. Irá aparecer:
- **Nome ("StockFlow")**
- O sistema deve analisar as datas de validade de cada produto, **avisar de forma chamativa quando um produto estiver para vencer.** Exemplo:
    * "Vencimento Próximo: Feijão (Vence em: 2026-05-29)"
- O programa deve aceitar que o usuário digite números para "acessar" funções. 
Exemplo:
    - Digite 1 - Visualizar Estoque Atual
        * Dentre as opções que o usuário poderá utilizar é: Visualizar Estoque Atual, Cadastrar / Atualizar Ingrediente, Vender 'Prato Feito' (Baixa Automática) e Sair do Sistema
- Quando o usuário fizer a baixa de um pedido (Prato Feito), o sistema deve retirar automaticamente do estoque as quantidade específicas da receita (200g de arroz e 100g de feijão). Então quando o estoque de qualquer um dos itens estiver abaixo do necessário a venda deve ser bloqueada

___

## **Documentação de Requisitos**

| Opção | Funcionalidade | Requisito Relacionado |
| :--- | :---: | ---: |
| 1 | Visualizar Estoque Atual | RF02 |
| 2 | Cadastrar Ingrediente | RF01 |
| 3 | Vender 'Prato Feito' | RF05 / RN01 |
| 4 | Sair do Sistema | - |

### _1. Introdução e Visão Geral_

#### 1.1 Propósito

Este documento define as especificações de requisitos para o software *StockFlow*, servindo como diretriz de engenharia de software para o desenvolvimento, testes e validação da aplicação. O público-alvo deste documento engloba desenvolvedores e o professor avaliador.

#### 1.2 Escopo

O *StockFlow* é uma aplicação restrita ao terminal (CLI - *Command Line Interface*) projetada para mitigar o desperdício em restaurantes através do controle rigoroso de validade de insumos perecíveis e do abatimento automático e inteligente baseado nas receitas de vendas (baixa composta). O sistema limita-se à gestão interna de estoque e simulação de vendas, operando sem conexões externas nesta versão.

#### 1.3 Visão Geral

Restaurantes que lidam com ingredientes perecíveis sofrem com prejuízos financeiros causados pelo vencimento oculto de insumos e falhas humanas na contagem de estoque pós-venda. O *StockFlow* automatiza esses processos, alertando proativamente as datas críticas antes que as perdas ocorram e travando vendas cujos ingredientes estejam ausentes.

#### 1.4 Definições e Acrônimos

* **CLI:** *Command Line Interface* (Interface de Linha de Comando).
* **Baixa Composta:** Dedução simultânea de múltiplos ingredientes do estoque a partir de uma única ação de venda.
* **Insumo/Ingrediente:** Produto físico quantificado em gramas (g) utilizado no preparo dos pratos.


### _2. Descrição Geral do Usuário e das Partes Interessadas_

#### 2.1 Perfil do Usuário

O usuário principal é o operador do estoque ou gerente do restaurante. Possui familiaridade básica com computadores e executará comandos através de entradas numéricas em um terminal de texto estruturado.

#### 2.2 Partes Interessadas (Stakeholders)

* **Gerência/Dono do Restaurante:** Busca controle financeiro e eliminação do desperdício de insumos.
* **Operador de Estoque:** Necessita de agilidade no cadastro e alertas claros de validade.

### _3. Especificação dos Requisitos (Backlog do Produto)_

#### 3.1 Backlog em Histórias de Usuário (User Stories)

* **US01:** Como *Operador de Estoque*, eu quero *cadastrar ingredientes com nome, quantidade em gramas e data de validade*, para *manter o inventário atualizado*.
* **US02:** Como *Gerente do Restaurante*, eu quero *visualizar alertas em destaque no menu principal para itens que vencem em menos de 3 dias*, para *tomar decisões rápidas e evitar o descarte de produtos*.
* **US03:** Como *Operador de Caixa*, eu quero *registrar a venda de um 'Prato Feito' e ter o estoque reduzido de forma automática em 200g de arroz e 100g de feijão*, para *eliminar erros de contagem manual*.
* **US04:** Como *Gerente do Restaurante*, eu quero *que o sistema impeça a venda de um prato caso algum ingrediente esteja abaixo do peso necessário*, para *evitar faturar pedidos que não podem ser entregues*.

#### 3.2 Requisitos Funcionais (RF)

* **RF01 - Cadastro de Insumos:** O sistema deve permitir o cadastro de novos ingredientes ou atualização de existentes, capturando obrigatoriamente: Nome do produto, Quantidade (inteiro, convertido em gramas) e Data de Validade (no formato `AAAA-MM-DD`).
* **RF02 - Visualização de Estoque:** O sistema deve exibir uma listagem de todos os ingredientes cadastrados, apresentando o nome formatado em letra maiúscula, a quantidade atual seguida da unidade "g" e a data de validade formatada no padrão brasileiro (`DD/MM/AAAA`).
* **RF03 - Navegação por Menu Numérico:** O sistema deve disponibilizar um menu interativo e em loop no terminal, aceitando entradas numéricas de 1 a 4 para acessar as funções de Visualizar Estoque, Cadastrar Ingrediente, Vender Prato Feito e Sair do Sistema.
* **RF04 - Alerta Automatizado de Validade:** O sistema deve analisar as datas de validade no momento de carregamento do menu e projetar mensagens em destaque textuais (Ex: `PRODUTO VENCIDO:` ou `VENCIMENTO PRÓXIMO:`) para itens vencidos ou a vencer em um intervalo menor ou igual a 3 dias a partir da data corrente.
* **RF05 - Baixa Composta de Receita:** O sistema deve deduzir de forma automática e integrada os valores exatos de **200g de Arroz** e **100g de Feijão** do estoque ao processar a venda da opção fixa "Prato Feito".

#### 3.3 Requisitos Não Funcionais (RNF)

* **RNF01 - Tipo de Interface (Usabilidade):** O sistema deve operar exclusivamente via Interface de Linha de Comando (CLI), priorizando a simplicidade visual e independência de dependências de interface gráfica ou bibliotecas web.
* **RNF02 - Volatilidade e Performance (Armazenamento):** O sistema deve manter o banco de dados armazenado em memória dinâmica de tempo de execução (*In-Memory Runtime Data Structure*), garantindo tempo de resposta imediato ($<0.1$ segundos) para processamento das validações de estoque.

#### 3.4 Regras de Negócio (RN)

* **RN01 - Bloqueio de Venda por Inconsistência:** O sistema está terminantemente proibido de concluir a venda de um "Prato Feito" se a quantidade em estoque de qualquer ingrediente da receita (200g para arroz ou 100g para feijão) for inferior ao exigido. O sistema deve emitir uma mensagem explícita de recusa detalhando qual insumo gerou a quebra de estoque.
* **RN02 - Intervalo do Alerta de Perecíveis:** O critério temporal para disparo de alertas de atenção em destaque é restrito ao cálculo de:
Data de Validade / Data Atual + 3 dias
* **RN03 - Atendimento Prévio de Integridade:** Nenhuma baixa de estoque parcial deve ser efetuada se houver a falta de um dos itens. A verificação de suficiência de *todos* os ingredientes deve ocorrer antes de qualquer alteração de valores nos dicionários.



## **pro**