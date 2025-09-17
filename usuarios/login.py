import json
import pwinput
from usuarios.cadastro import cadastro
from utils.formatadores import formatar_cpf


def login():
    while True:
        identificador = input("Digite seu CPF ou CRM: ").strip()
        senha = pwinput.pwinput("Senha: ", mask="*").strip()

        try:
            with open("usuarios.json", "r") as f:
                for linha in f:
                    usuario = json.loads(linha)
                    if usuario["id"] == identificador and usuario["senha"] == senha:
                        print(f"\n✅ Login realizado com sucesso! Bem-vindo(a), {usuario['nome']}.\n")
                        return usuario
        except FileNotFoundError:
            print("❌ Nenhum usuário cadastrado ainda. Vamos criar uma conta!\n")
            return cadastro()
        print("❌ Usuário ou senha incorretos. Tente novamente!\n")
