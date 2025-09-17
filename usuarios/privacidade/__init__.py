import json
import os

USUARIOS_DB = "usuarios.json"

# ================================
# Funções de persistência
# ================================
def carregar_usuarios():
    """
    Lê o arquivo usuarios.json linha por linha,
    devolvendo um dicionário com ID como chave.
    """
    usuarios = {}
    if os.path.exists(USUARIOS_DB):
        with open(USUARIOS_DB, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    usuario = json.loads(line)
                    usuarios[usuario["id"]] = usuario
    return usuarios

def salvar_usuarios(usuarios):
    """
    Salva os usuários no arquivo usuarios.json,
    cada registro em uma linha separada (mesmo formato atual).
    """
    with open(USUARIOS_DB, "w", encoding="utf-8") as f:
        for usuario in usuarios.values():
            json.dump(usuario, f, ensure_ascii=False)
            f.write("\n")

# ================================
# Funções de privacidade
# ================================
def mostrar_politica_privacidade():
    print("\n📜 Política de Privacidade")
    print("- Seus dados serão usados apenas para agendamentos, exames e notificações.")
    print("- Não compartilhamos suas informações com terceiros sem autorização.")
    print("- Você pode solicitar exclusão de seus dados a qualquer momento.")
    print("- Mantemos medidas de segurança para proteger suas informações.\n")

def excluir_conta(usuario):
    usuarios = carregar_usuarios()
    usuario_id = usuario["id"]  # pega apenas o ID/CPF
    if usuario_id in usuarios:
        del usuarios[usuario_id]
        salvar_usuarios(usuarios)
        print("✅ Sua conta foi excluída com sucesso.")
    else:
        print("❌ Usuário não encontrado.")

def menu_privacidade(usuario):
    while True:
        print("\n⚙️ Menu de Privacidade")
        print("1 - Ver Política de Privacidade")
        print("2 - Excluir minha conta")
        print("3 - Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            mostrar_politica_privacidade()
        elif opcao == "2":
            confirmacao = input("Deseja realmente excluir sua conta? (s/n): ").lower()
            if confirmacao == "s":
                certeza = input("⚠️ Tem certeza absoluta que deseja excluir sua conta? Essa ação não pode ser desfeita. (s/n): ").lower()
                if certeza == "s":
                    excluir_conta(usuario)
                    break
                else:
                    print("❌ Exclusão cancelada.")
            else:
                print("❌ Exclusão cancelada.")
        elif opcao == "3":
            break
        else:
            print("Opção inválida.")
