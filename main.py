from usuarios.login import login
from usuarios.cadastro import cadastro
from usuarios.perfil import configurar_perfil_paciente
from usuarios.documentos import mostrar_documentos
from usuarios.mensagens import mostrar_mensagens
from agenda.compromissos import menu_agenda
from usuarios.notificacoes import mostrar_notificacoes
from usuarios.privacidade import menu_privacidade
from plataforma_medicos.medicos import autenticar_medico, exibir_quadro_acompanhamento


print("Bem-vindo a Clínica VitalCode\n"
      "Integre, acompanhe e registre cada etapa com segurança.\n"
      "➡️  Acesse o painel e comece agora.\n")

usuario_encontrado = None

# Menu inicial
while True:
    print("Acesso ao login: Digite 1")
    print("Criar uma conta: Digite 2")
    opcao_inicial = input("Escolha uma opção (1 para login, 2 para criar conta): ").strip()
    if opcao_inicial in ["1", "2"]:
        break
    else:
        print("❌ Opção inválida! Tente novamente.\n")

# Fluxo de login ou cadastro
if opcao_inicial == "2":
    usuario_encontrado = cadastro()
elif opcao_inicial == "1":
    usuario_encontrado = login()

# Menu principal do paciente
if usuario_encontrado and usuario_encontrado["tipo"] == "paciente":
    while True:
        print("\nMENU PACIENTE")
        print("1 - Perfil pessoal")
        print("2 - Agenda")
        print("3 - Resultados e documentos ")
        print("4 - Comunicação segura ")
        print("5 - Módulos educacionais")
        print("6 - Notificações")
        print("7 - Privacidade")
        print("0 - Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == "1":
            configurar_perfil_paciente(usuario_encontrado)
        elif escolha == "2":
            menu_agenda(usuario_encontrado)
        elif escolha == "3":
            mostrar_documentos(usuario_encontrado)
        elif escolha =="4":
            mostrar_mensagens(usuario_encontrado)
        elif escolha =="5":
            print
        elif escolha =="6":
            mostrar_notificacoes(usuario_encontrado)
        elif escolha =="7":
            menu_privacidade(usuario_encontrado)
        elif escolha == "0":
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("❌ Opção inválida.")

def main():
    medico = autenticar_medico()  # chama a função do módulo medicos.py
    if medico:
        exibir_quadro_acompanhamento(medico)  # exibe quadro do médico

if __name__ == "__main__":
    main()