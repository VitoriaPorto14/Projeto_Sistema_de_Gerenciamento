from datetime import datetime, timedelta

# --- 1. BANCO DE DADOS EM MEMÓRIA (Dicionários básicos) ---
# Quantidades em gramas. Validades configuradas para o ano de 2026.
estoque = {
    "arroz": {"quantidade": 1000, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")},
    "feijao": {"quantidade": 500, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")}, # Vence em breve
    "carne": {"quantidade": 2000, "validade": datetime.strptime("2026-06-16", "%Y-%m-%d")}
}

# Receita fixa do Prato Feito
ingredientes_pf = {
    "arroz": 200,
    "feijao": 100
}

# --- 2. LOOP PRINCIPAL DO PROGRAMA (Menu no Terminal) ---
while True:
    print("\n=========================================")
    print("        STOCKFLOW - MENU PRINCIPAL       ")
    print("=========================================")

    # --- REQUISITO: ALERTAS DE VALIDADE EM DESTAQUE ---
    hoje = datetime.today()
    limite_alerta = hoje + timedelta(days=3)

    print("\n      SISTEMA DE ALERTAS DE VALIDADE:")
    tem_alerta = False

    for produto in estoque:
        data_val = estoque[produto]["validade"]

        # Se a data de hoje for maior ou igual à validade -> Vencido
        if hoje.date() >= data_val.date():
            print(f"   PRODUTO VENCIDO: {produto.upper()} (Venceu em: {data_val.strftime('%d/%m/%Y')})")
            tem_alerta = True
        # Se vencer nos próximos 3 dias -> Alerta de vencimento próximo
        elif hoje.date() < data_val.date() <= limite_alerta.date():
            print(f"   VENCIMENTO PRÓXIMO (menos de 3 dias): {produto.upper()} (Vence em: {data_val.strftime('%d/%m/%Y')})")
            tem_alerta = True

    if not tem_alerta:
        print("Todos os produtos estão com a validade em dia.")

    print("-----------------------------------------")
    print("1 - Visualizar Estoque Atual")
    print("2 - Cadastrar / Atualizar Ingrediente")
    print("3 - Vender 'Prato Feito' (Baixa Automática)")
    print("4 - Sair do Sistema")
    print("=========================================")

    opcao = input("Escolha uma opção (1-4): ")

    # --- OPÇÃO 1: VISUALIZAR ESTOQUE ---
    if opcao == "1":
        print("\n↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓=↓")
        print("\n--- ESTOQUE ATUAL ---")
        for produto in estoque:
            qtd = estoque[produto]["quantidade"]
            val = estoque[produto]["validade"].strftime("%d/%m/%Y")
            print(f"• {produto.capitalize()}: {qtd}g | Validade: {val}")


    #Opçao 2: cadastrar/ e atualizar produtos GAzolA AQUI
    if opcao == "2":
        print("\n--- CADASTRO / ATUALIZAÇÂO DE ITEM ---")
        novo_item = input("Nome do novo ingrediente: ").strip().lower()
        try:
            qtd_input = int(input("Quantidade (em gramas): "))
            if qtd_input < 0:
                print("Error: A quantidade não pode ser negativa!")
                continue
        except ValueError:
            print("Error: Digite um número inteiro válido para a quantidade.")
            continue

        data_input = input("Data de validade (AAAA-MM-DD): ").strip()
        try:
            validade_dt = datetime.strptime(data_input, "%Y-%m-%d") 
        except ValueError:
            print("Erro: formato de data invalido, use AAAA-MM-DD.")
            continue

        if novo_item in estoque:
                estoque[novo_item]["quantidade"] += qtd_input
                estoque[novo_item]["validade"] = validade_dt
                print(f"{novo_item.upper()} atualizado com sucesso!")
        else:
            estoque[novo_item] = {"quantidade": qtd_input, "validade": validade_dt}
            print(f"{novo_item.upper()} cadastrado com sucesso!")

        
    #opção 3 venda prato (baixa) gazola
    if opcao == "3":
        print("\n--- PROCESSANDO VENDA: PRATO FEITO ---")

        pode_vender = True
        faltando = []

        for ingrediente, qtd_necessaria in ingredientes_pf.items():
            if ingrediente not in estoque or estoque[ingrediente]["quantidade"] < qtd_necessaria:
                pode_vender = False
                faltando.append(ingrediente.upper())

        if not pode_vender:
            print("VENDA RECUSADA: Estoque insuficiente para a receita do PF")
            print(f"Faltando no estoque:", *faltando)
        else:
            for ingrediente, qnt_neces in ingredientes_pf.items():
                estoque[ingrediente]["quantidade"] -= qtd_necessaria
            print("VENDA REALIZADA! Baixa de 200g de Arroz e 100g de Feijão aplicada.")

    #opção 4 saida

        if opcao == "4":
            print("\nSaindo do StockFlow.")
            break
        else:
            print("opção invalida! Escolha de um numero de 1 a ")
            



    



    

