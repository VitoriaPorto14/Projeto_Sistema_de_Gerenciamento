from datetime import datetime, timedelta
import os

# --- 1. BANCO DE DADOS EM MEMÓRIA (Dicionários básicos) ---
# Aqui criamos o estoque inicial com nome do item, gramas e a data de validade.
estoque = {
    "arroz": {"quantidade": 1000, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")},
    "feijao": {"quantidade": 500, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")}, # Vence em breve
    "carne": {"quantidade": 2000, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")}
}

# Aqui definimos a receita padrão do Prato Feito (quanto gasta de cada item)
ingredientes_pf = {
    "arroz": 200,
    "feijao": 100
}

# Função simples para limpar o console e não deixar o menu entulhado de texto
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

# --- 2. LOOP PRINCIPAL DO PROGRAMA (Menu no Terminal) ---
# Início do laço infinito para manter o programa rodando até o usuário mandar sair
while True:
    print("\n=========================================")
    print("        STOCKFLOW - MENU PRINCIPAL       ")
    print("=========================================")

    # --- REQUISITO: ALERTAS DE VALIDADE EM DESTAQUE ---
    # Pega a data de hoje e calcula a data limite de alerta (daqui a 3 dias)
    hoje = datetime.today()
    limite_alerta = hoje + timedelta(days=3)

    print("\n      SISTEMA DE ALERTAS DE VALIDADE:")
    tem_alerta = False

    # Varre o estoque conferindo as datas de validade de cada ingrediente
    for produto in estoque:
        data_val = estoque[produto]["validade"]

        # Se a data de hoje passou ou é igual à validade, avisa que venceu
        if hoje.date() >= data_val.date():
            print(f"   PRODUTO VENCIDO: {produto.upper()} (Venceu em: {data_val.strftime('%d/%m/%Y')})")
            tem_alerta = True
        # Se a validade estiver dentro da janela dos próximos 3 dias, solta o alerta crítico
        elif hoje.date() < data_val.date() <= limite_alerta.date():
            print(f"   VENCIMENTO PRÓXIMO (menos de 3 dias): {produto.upper()} (Vence em: {data_val.strftime('%d/%m/%Y')})")
            tem_alerta = True

    # Se nenhum item disparou os ifs acima, exibe a mensagem de sucesso
    if not tem_alerta:
        print("Todos os produtos estão com a validade em dia.")

    print("-----------------------------------------")
    print("1 - Visualizar Estoque Atual")
    print("2 - Cadastrar / Atualizar Ingrediente")
    print("3 - Vender 'Prato Feito' (Baixa Automática)")
    print("4 - Sair do Sistema")
    print("=========================================")

    # Captura o número digitado pelo usuário
    opcao = input("Escolha uma opção (1-4): ")

    # --- OPÇÃO 1: VISUALIZAR ESTOQUE ---
    if opcao == "1":
        print("\n↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓")
        print("\n--- ESTOQUE ATUAL ---")
        # Passa por todo o estoque printando o nome formatado, a quantidade em g e a data convertida para BR
        for produto in estoque:
            qtd = estoque[produto]["quantidade"]
            val = estoque[produto]["validade"].strftime("%d/%m/%Y")
            print(f"• {produto.capitalize()}: {qtd}g | Validade: {val}")

        # Trava a tela com um input para o usuário ler as informações antes do menu reiniciar
        input("\nAperte ENTER para voltar ao menu...")


    #Opçao 2: cadastrar/ e atualizar produtos GAzolA AQUI
    elif opcao == "2":
        print("\n--- CADASTRO / ATUALIZAÇÂO DE ITEM ---")
        novo_item = input("Nome do novo item: ").strip().lower()
        
        # Bloco try/except para impedir que o programa trave se o usuário digitar letras na quantidade
        try:
            qtd_input = int(input("Quantidade (em gramas): "))
            # Validação para não aceitar peso negativo no sistema
            if qtd_input < 0:
                print("Error: A quantidade não pode ser negativa!")
                input("\nAperte ENTER para voltar ao menu...")
                continue
        except ValueError:
            print("Error: Digite um número inteiro válido para a quantidade.")
            input("\nAperte ENTER para voltar ao menu...")
            continue

        data_input = input("Data de validade (AAAA-MM-DD): ").strip()
        # Bloco try/except para forçar o usuário a digitar a data no formato correto separado por hifens
        try:
            validade_dt = datetime.strptime(data_input, "%Y-%m-%d") 
        except ValueError:
            print("Erro: formato de data invalido, use AAAA-MM-DD.")
            input("\nAperte ENTER para voltar ao menu...")
            continue

        # Se o item já estiver no dicionário, apenas soma o peso novo e atualiza a validade
        if novo_item in estoque:
                estoque[novo_item]["quantidade"] += qtd_input
                estoque[novo_item]["validade"] = validade_dt
                print(f"{novo_item.upper()} atualizado com sucesso!")
        # Se for um item inédito, cria a chave nova e adiciona no dicionário
        else:
            estoque[novo_item] = {"quantidade": qtd_input, "validade": validade_dt}
            print(f"{novo_item.upper()} cadastrado com sucesso!")

        input("\nAperte ENTER para voltar ao menu...")

        
    #opção 3 venda prato (baixa) gazola
    elif opcao == "3":
        print("\n--- PROCESSANDO VENDA: PRATO FEITO ---")

        pode_vender = True
        faltando = []

        # PASSO 1 DE SEGURANÇA: Confere se todos os ingredientes da receita existem e têm peso suficiente
        for ingrediente, qtd_necessaria in ingredientes_pf.items():
            if ingrediente not in estoque or estoque[ingrediente]["quantidade"] < qtd_necessaria:
                pode_vender = False
                faltando.append(ingrediente.upper()) # Guarda o nome do que está faltando para avisar

        # Se faltar qualquer coisa, cancela o processo e joga o erro na tela
        if not pode_vender:
            print("VENDA RECUSADA: Estoque insuficiente para a receita do PF")
            print(f"Faltando no estoque:", *faltando)
        # Se estiver tudo certo, roda o PASSO 2 diminuindo os ingredientes do estoque real de forma automática
        else:
            for ingrediente, qtd_necessaria in ingredientes_pf.items():
                estoque[ingrediente]["quantidade"] -= qtd_necessaria
            print("VENDA REALIZADA! Baixa de 200g de Arroz e 100g de Feijão aplicada.")

        input("\nAperte ENTER para voltar ao menu...")

    #opção 4 saida
    elif opcao == "4":
        print("\nSaindo do STOCKFLOW.")
        break # Quebra o laço while principal e encerra a execução do script
    
    # Tratamento de erro caso o usuário digite um número fora de 1-4 ou letras no menu
    else:
        print("opção invalida! Escolha de um numero de 1 a 4")
        input("\nAperte ENTER para tentar novamente...")