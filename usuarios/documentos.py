from usuarios.notificacoes import adicionar_notificacao

def mostrar_documentos(usuario):
    """
    Mostra os exames/documentos do paciente com status e permite
    simular ações: baixar PDF ou visualizar.
    """

    # Filtra apenas os exames da agenda
    documentos = []
    for c in usuario.get("agenda", []):
        if c["tipo_compromisso"].lower() == "exame":
            status = c.get("status", "Pendente liberação")
            documentos.append({
                "nome": c.get("exame", "Exame genérico"),
                "status": status
            })

    if not documentos:
        print("\n📂 Nenhum documento disponível.")
        return

    while True:
        print("\n📂 Meus documentos")
        for idx, doc in enumerate(documentos, 1):
            if doc["status"].lower() == "disponível":
                print(f"{idx} - {doc['nome']} – Disponível – [⬇️ Baixar PDF] / [👁️ Visualizar]")
            else:
                print(f"{idx} - {doc['nome']} – Pendente liberação")

        print("0 - Voltar ao menu")
        escolha = input("Escolha um documento para ação ou 0 para voltar: ").strip()

        if escolha == "0":
            break

        if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > len(documentos):
            print("❌ Opção inválida.")
            continue

        doc_escolhido = documentos[int(escolha)-1]

        if doc_escolhido["status"].lower() != "disponível":
            print(f"⚠️       O exame '{doc_escolhido['nome']}' ainda não está disponível para download ou visualização.")
            continue

        print(f"\nVocê escolheu: {doc_escolhido['nome']}")
        print("1 - ⬇️ Baixar PDF")
        print("2 - 👁️ Visualizar")
        acao = input("Escolha uma ação: ").strip()

        if acao == "1":
            # Simulação de download
            print(f"✅ PDF de '{doc_escolhido['nome']}' baixado com sucesso!")
        elif acao == "2":
            # Simulação de visualização
            print(f"👁️ Exibindo '{doc_escolhido['nome']}' no visualizador...")
        else:
            print("❌ Ação inválida.")

def liberar_exame(usuario, exame):
    # lógica para liberar exame
    adicionar_notificacao(
        "Novo documento disponível",
        f"O resultado do exame '{exame['nome']}' já está disponível para visualização.",
        "novos_documentos"
    )