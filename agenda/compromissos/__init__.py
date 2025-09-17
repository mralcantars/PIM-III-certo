from dados.medicos import medicos
from dados.exames import exames
from usuarios.persistencia import atualizar_usuario_no_arquivo
from usuarios.notificacoes import adicionar_notificacao

def menu_agenda(usuario):
    while True:
        print("\n MENU DA AGENDA ")
        print("1 - Mostrar compromissos")
        print("2 - Adicionar compromisso")
        print("3 - Voltar ao menu principal")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            mostrar_agenda(usuario)
        elif opcao == "2":
            adicionar_compromisso_paciente(usuario)
        elif opcao == "3":
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

def mostrar_agenda(usuario):
    if not usuario.get("agenda"):
        print("📅 Nenhum compromisso agendado.")
        return

    consultas = [c for c in usuario["agenda"] if c["tipo_compromisso"].lower() == "consulta"]
    exames_agendados = [c for c in usuario["agenda"] if c["tipo_compromisso"].lower() == "exame"]

    print("\n📌 Consultas")
    if consultas:
        for c in consultas:
            hora = c.get("hora", "")
            print(f"   {c['data']} {hora} – {c['especialidade']} – Status: {c['status']}")
    else:
        print("   Nenhuma consulta agendada.")

    print("\n📌 Exames")
    if exames_agendados:
        for c in exames_agendados:
            hora = c.get("hora", "")
            print(f"   {c['data']} {hora} – {c['especialidade']} – Status: {c['status']}")
    else:
        print("   Nenhum exame agendado.")


def adicionar_compromisso_paciente(usuario):
    print("\nAgendamento")
    print("1 - Consulta")
    print("2 - Exame")
    escolha = input("Escolha uma opção: ")

    # CONSULTA
    if escolha == "1":
        print("\nEspecialidades disponíveis para CONSULTA:")
        especialidades = list({m["especialidade"] for m in medicos})
        for i, esp in enumerate(especialidades, 1):
            print(f"{i} - {esp}")

        try:
            escolha_esp = int(input("\nDigite o número da especialidade desejada: ").strip())
            especialidade = especialidades[escolha_esp - 1]
        except (ValueError, IndexError):
            print("❌ Opção inválida.")
            return

        medico = next((m for m in medicos if m["especialidade"].lower() == especialidade.lower()), None)

        if not medico:
            print("❌ Especialidade não encontrada.")
            return

        print(f"\nHorários disponíveis para {medico['nome']} ({medico['especialidade']}):")
        for i, h in enumerate(medico["horarios_disponiveis"], 1):
            print(f"{i} - {h}")

        try:
            escolha_horario = int(input("\nEscolha o número do horário: ").strip())
            horario = medico["horarios_disponiveis"][escolha_horario - 1]
        except (ValueError, IndexError):
            print("❌ Opção inválida.")
            return

        medico["horarios_disponiveis"].remove(horario)

        if "agenda" not in usuario:
            usuario["agenda"] = []

        usuario["agenda"].append({
            "tipo_compromisso": "Consulta",
            "data": horario.split()[0],
            "hora": horario.split()[1],
            "especialidade": medico["especialidade"],
            "medico": medico["nome"],
            "status": "Confirmada"
        })

        print(f"✅ Consulta marcada com {medico['nome']} em {horario}.")
        atualizar_usuario_no_arquivo(usuario)

    # EXAME
    elif escolha == "2":
        print("\nEspecialidades disponíveis para EXAME:")
        especialidades = list({e["especialidade"] for e in exames})
        for i, esp in enumerate(especialidades, 1):
            print(f"{i} - {esp}")

        try:
            escolha_esp = int(input("\nDigite o número da especialidade desejada: ").strip())
            especialidade = especialidades[escolha_esp - 1]
        except (ValueError, IndexError):
            print("❌ Opção inválida.")
            return

        exame = next((e for e in exames if e["especialidade"].lower() == especialidade.lower()), None)

        if not exame:
            print("❌ Especialidade não encontrada.")
            return

        print(f"\nHorários disponíveis para {exame['nome']} ({exame['especialidade']}):")
        for i, h in enumerate(exame["horarios_disponiveis"], 1):
            print(f"{i} - {h}")

        try:
            escolha_horario = int(input("\nEscolha o número do horário: ").strip())
            horario = exame["horarios_disponiveis"][escolha_horario - 1]
        except (ValueError, IndexError):
            print("❌ Opção inválida.")
            return

        exame["horarios_disponiveis"].remove(horario)

        if "agenda" not in usuario:
            usuario["agenda"] = []

        usuario["agenda"].append({
            "tipo_compromisso": "Exame",
            "data": horario.split()[0],
            "hora": horario.split()[1],
            "especialidade": exame["especialidade"],
            "exame": exame["nome"],
            "status": "Agendado"
        })

        print(f"✅ Exame {exame['nome']} marcado em {horario}.")
        atualizar_usuario_no_arquivo(usuario)

    else:
        print("❌ Opção inválida.")
        
def agendar_consulta(usuario, medico, data, hora):
    # lógica do agendamento
    adicionar_notificacao(
        "Consulta marcada",
        f"Sua consulta com Dr(a). {medico['nome']} foi agendada para {data} às {hora}.",
        "lembretes_consultas"
    )

def cancelar_consulta(usuario, data, hora):
    # lógica do cancelamento
    adicionar_notificacao(
        "Consulta cancelada",
        f"A consulta marcada para {data} às {hora} foi cancelada.",
        "lembretes_consultas"
    )