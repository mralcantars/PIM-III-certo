import json
import pwinput
from utils.formatadores import formatar_cpf
from usuarios.notificacoes import adicionar_notificacao

def cadastro():
    nome = input("Nome completo: ").strip()
    while True:
        cpf = input("CPF (11 dígitos): ").strip()
        if cpf.isdigit() and len(cpf) == 11:
            identificador = formatar_cpf(cpf)
            tipo_usuario = "paciente"
            break
        else:
            print("❌ CPF inválido! Digite apenas 11 números.")

    while True:
        senha = pwinput.pwinput("Crie uma senha: ", mask="*").strip()
        confirma = pwinput.pwinput("Confirme a senha: ", mask="*").strip()
        if senha == confirma:
            print("✅ Senha criada com sucesso!")
            break
        else:
            print("❌ As senhas não conferem. Tente novamente!")

    usuario = {
        "nome": nome,
        "id": identificador,
        "senha": senha,
        "tipo": tipo_usuario,
        "perfil": {},
        "agenda": []
    }

    with open("usuarios.json", "a") as f:
        f.write(json.dumps(usuario) + "\n")

    print(f"\n✅ Conta criada com sucesso! Bem-vindo(a), {nome}.\n")
    return usuario

def cadastrar_usuario(usuario):
    # lógica do cadastro
    adicionar_notificacao(
        "Cadastro realizado",
        f"Bem-vindo(a) {usuario['nome']}! Seu cadastro foi concluído.",
        "mensagens_nao_lidas"
    )