import json
import os
from datetime import datetime

CAMINHO_ARQUIVO = "dados/mensagens.json"


def carregar_mensagens():
    """Carrega mensagens do arquivo JSON ou cria estrutura inicial."""
    if not os.path.exists(CAMINHO_ARQUIVO):
        return {}
    with open(CAMINHO_ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_mensagens(mensagens):
    """Salva mensagens no arquivo JSON."""
    with open(CAMINHO_ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(mensagens, f, ensure_ascii=False, indent=4)


def mostrar_mensagens(usuario):
    """Menu de comunicação segura do paciente (vinculado ao usuário)."""
    mensagens = carregar_mensagens()
    paciente_id = usuario["id"]  # cada paciente deve ter um campo "id"

    # Se não existir ainda, cria espaço para este paciente
    if paciente_id not in mensagens:
        mensagens[paciente_id] = {"recebidas": [], "enviadas": []}
        salvar_mensagens(mensagens)

    while True:
        print("\nCOMUNICAÇÃO SEGURA 📨")
        print("1 - Ver mensagens recebidas")
        print("2 - Ver mensagens enviadas")
        print("3 - Nova mensagem")
        print("0 - Voltar")
        opcao = input("Escolha: ").strip()

        mensagens = carregar_mensagens()

        if opcao == "1":
            print("\n📥 Mensagens recebidas:")
            if mensagens[paciente_id]["recebidas"]:
                for msg in mensagens[paciente_id]["recebidas"]:
                    print(f"[{msg['remetente']}] – \"{msg['texto']}\" – {msg['data']}")
            else:
                print("Nenhuma mensagem recebida.")

        elif opcao == "2":
            print("\n📤 Mensagens enviadas:")
            if mensagens[paciente_id]["enviadas"]:
                for msg in mensagens[paciente_id]["enviadas"]:
                    print(f"[Você → {msg['destinatario']}] – \"{msg['texto']}\" – {msg['data']}")
            else:
                print("Nenhuma mensagem enviada.")

        elif opcao == "3":
            destinatario = input("Destinatário: ")
            texto = input("Digite sua mensagem: ")
            nova_msg = {
                "destinatario": destinatario,
                "texto": texto,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M")
            }
            mensagens[paciente_id]["enviadas"].append(nova_msg)
            salvar_mensagens(mensagens)
            print(f"\n✅ Mensagem enviada para {destinatario}!")

        elif opcao == "0":
            break
        else:
            print("❌ Opção inválida.")
