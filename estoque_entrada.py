from src.database import Produto

def cadastrar_produto(db_session):
    
    print("\n" + "="*50)
    print("   MÓDULO 2: ENTRADA DE ESTOQUE")
    print("="*50)
    
    # ========================================================================
    # PASSO 1: DEFINIR QUANTOS PRODUTOS SERÃO CADASTRADOS
    # ========================================================================
    try:
        qtd_cadastro = int(input("\n Quantos produtos deseja cadastrar agora? "))

        if qtd_cadastro <= 0:
            print("\n Quantidade deve ser maior que zero!")
            return

    except ValueError:
        print("\n Erro: Digite apenas números inteiros!")
        return

    # ========================================================================
    # PASSO 2: PARA CADA PRODUTO, COLETAR DADOS E SALVAR
    # ========================================================================
    for i in range(1, qtd_cadastro + 1):
        print(f"\n Produto {i} de {qtd_cadastro}")

        # nome do produto (não vazio)
        while True:
            nome = input("  Nome do produto: ").strip()
            if nome:
                break
            print("  Nome não pode ser vazio.")

        # quantidade (inteiro)
        while True:
            try:
                quantidade = int(input("  Quantidade: "))
                if quantidade < 0:
                    print("  Quantidade não pode ser negativa.")
                    continue
                break
            except ValueError:
                print("  Digite um número inteiro válido para quantidade.")

        # preço (float)
        while True:
            try:
                preco_str = input("  Preço unitário (ex: 12.50): ").strip().replace(',', '.')
                preco = float(preco_str)
                if preco < 0:
                    print("  Preço não pode ser negativo.")
                    continue
                break
            except ValueError:
                print("  Digite um valor numérico válido para o preço.")

        # Tentar usar a classe Produto importada; caso não exista, armazenar em sessão como dicionário
        try:
            produto = Produto(nome=nome, quantidade=quantidade, preco=preco)
        except Exception:
            # Caso a classe Produto não exista ou tenha assinatura diferente, use dict
            produto = {"nome": nome, "quantidade": quantidade, "preco": preco}

        # Tentar persistir no banco ou sessão
        try:
            # se a sessão for do SQLAlchemy
            if hasattr(db_session, 'add') and hasattr(db_session, 'commit'):
                db_session.add(produto)
                db_session.commit()
            # se for uma lista simples
            elif hasattr(db_session, 'append'):
                db_session.append(produto)
            else:
                # fallback: tentar atribuir a uma lista chamada produtos
                if isinstance(db_session, dict) and 'produtos' in db_session and isinstance(db_session['produtos'], list):
                    db_session['produtos'].append(produto)
                else:
                    print("  Aviso: db_session não reconhecido, produto não foi persistido.")
        except Exception as e:
            print(f"  Erro ao persistir produto: {e}")
        else:
            print(f"  Produto '{nome}' cadastrado com sucesso (qtd={quantidade}, preco={preco:.2f}).")

    print("\n Cadastro concluído!")