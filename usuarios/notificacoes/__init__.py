import datetime

# Preferências globais de notificações (poderia ser salvo por usuário)
preferencias = {
    "lembretes_consultas": True,
    "novos_documentos": True,
    "mensagens_nao_lidas": True,
    "convites_modulos": True,
}

# Lista de notificações do usuário
notificacoes_db = []

def adicionar_notificacao(titulo, mensagem, categoria):
    """Adiciona uma notificação se a categoria estiver ativada"""
    if preferencias.get(categoria, True):
        notificacoes_db.append({
            "titulo": titulo,
            "mensagem": mensagem,
            "categoria": categoria,
            "data": datetime.date.today().isoformat(),
            "lida": False
        })

def mostrar_notificacoes(usuario):
    while True:
        print("\n🔔 NOTIFICAÇÕES")
        print("1 - Ver todas")
        print("2 - Ver apenas não lidas")
        print("3 - Marcar todas como lidas")
        print("4 - Configurar preferências")
        print("0 - Voltar")
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar_notificacoes()
        elif opcao == "2":
            listar_notificacoes(filtrar_nao_lidas=True)
        elif opcao == "3":
            marcar_todas_como_lidas()
        elif opcao == "4":
            configurar_preferencias()
        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")

def listar_notificacoes(filtrar_nao_lidas=False):
    if not notificacoes_db:
        print("\n📭 Nenhuma notificação disponível.")
        return
    print("\n📩 Lista de notificações:")
    for notif in notificacoes_db:
        if filtrar_nao_lidas and notif["lida"]:
            continue
        status = "✅ Lida" if notif["lida"] else "📌 Não lida"
        print(f"- {notif['titulo']} ({notif['data']}) [{status}]")
        print(f"   {notif['mensagem']}\n")

def marcar_todas_como_lidas():
    for notif in notificacoes_db:
        notif["lida"] = True
    print("✔ Todas as notificações foram marcadas como lidas!\n")

def configurar_preferencias():
    print("\n⚙️ CONFIGURAÇÕES DE NOTIFICAÇÕES")
    for key, ativo in preferencias.items():
        status = "Ativado ✅" if ativo else "Desativado ❌"
        print(f"- {key}: {status}")

    escolha = input("\nDigite o nome da categoria para alternar (ou ENTER para sair): ").strip()
    if escolha in preferencias:
        preferencias[escolha] = not preferencias[escolha]
        print(f"🔄 Preferência '{escolha}' agora está: {'Ativada ✅' if preferencias[escolha] else 'Desativada ❌'}")
