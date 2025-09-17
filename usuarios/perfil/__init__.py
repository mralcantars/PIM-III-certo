from usuarios.persistencia import atualizar_usuario_no_arquivo

def configurar_perfil_paciente(usuario):
    print("\nConfigurar Perfil Pessoal")
    perfil = usuario.get("perfil", {})

    print(f"Nome completo: {usuario['nome']}")
    print(f"CPF: {usuario['id']}")

    idade = input(f"Idade ({perfil.get('idade', )}): ").strip()
    perfil['idade'] = int(idade) if idade.isdigit() else perfil.get('idade')

    genero_atual = perfil.get('genero', )
    genero = input(f"Gênero ({genero_atual}): ").strip().title()
    perfil['genero'] = genero if genero else genero_atual

    endereco_atual = perfil.get('endereco', )
    endereco = input(f"Endereço ({endereco_atual}): ").strip().title()
    perfil['endereco'] = endereco if endereco else endereco_atual

    while True:
        contato_atual = perfil.get('contato_formatado', )
        contato = input(f"Telefone para contato (11 dígitos, ex: 11987654321) ({contato_atual}): ").strip()
        if contato.isdigit() and len(contato) == 11:
            perfil['contato_raw'] = contato
            perfil['contato_formatado'] = f"({contato[:2]}) {contato[2:7]}-{contato[7:]}"
            print("📞 Telefone salvo:", perfil['contato_formatado'])
            break
        elif not contato:
            print("Telefone não alterado.")
            break
        else:
            print("❌ Telefone inválido! Digite apenas números e use 11 dígitos.")

    medicamentos_str = perfil.get('medicamentos', 'Nenhum')
    usa_medicamentos = input(
        f"Faz uso de medicamentos contínuos? (sim/não) ({'sim' if medicamentos_str != 'Nenhum' else 'não'}): "
    ).strip().lower()

    if usa_medicamentos == "sim":
        medicamentos = input(f"Quais medicamentos você utiliza? ({medicamentos_str if medicamentos_str != 'Nenhum' else ''}): ").strip()
        perfil['medicamentos'] = medicamentos if medicamentos else medicamentos_str
    else:
        perfil['medicamentos'] = "Nenhum"

    preferencia_atual = perfil.get('preferencia_de_contato', )
    preferencia_de_contato = input(
        f"Por onde devemos entrar em contato (e-mail, telefone ou app) ({preferencia_atual or 'Não informado'}): "
    ).strip().lower()

    if preferencia_de_contato in ["e-mail", "email"]:
        while True:
            email_contato = input(f"Digite seu e-mail para contato ({perfil.get('email_contato', )}): ").strip()
            if "@" in email_contato and "." in email_contato:
                perfil['email_contato'] = email_contato
                perfil['meio_contato_detalhado'] = f"E-mail: {email_contato}"
                perfil['preferencia_de_contato'] = "E-mail"
                print("📩 Preferência de contato registrada:", perfil['meio_contato_detalhado'])
                break
            elif not email_contato:
                print("E-mail não alterado.")
                break
            else:
                print("❌ E-mail inválido! Certifique-se de incluir '@' e '.'.")
    elif preferencia_de_contato == "telefone":
        if perfil.get('contato_formatado'):
            perfil['meio_contato_detalhado'] = f"Telefone: {perfil['contato_formatado']}"
            perfil['preferencia_de_contato'] = "Telefone"
            print("📩 Preferência de contato registrada:", perfil['meio_contato_detalhado'])
        else:
            print("⚠️ Telefone não informado no perfil. Por favor, preencha o telefone primeiro.")
    elif preferencia_de_contato == "app":
        perfil['meio_contato_detalhado'] = "App (notificações internas)"
        perfil['preferencia_de_contato'] = "App"
        print("📩 Preferência de contato registrada:", perfil['meio_contato_detalhado'])
    elif not preferencia_de_contato:
        print("Preferência de contato não alterada.")

    while True:
        print("\n🔒 Termos de privacidade: Seus dados serão usados apenas para fins clínicos, conforme a LGPD.\n")
        aceitou_termos = input("Você aceita os termos de privacidade (sim/não): ").strip().lower()
        if aceitou_termos == "sim":
            perfil['aceitou_termos'] = True
            print("✅ Termos aceitos! Vamos continuar...")
            break
        else:
            print("⚠️ Você deve aceitar os termos para continuar.\n")
            perfil['aceitou_termos'] = False

    usuario["perfil"] = perfil
    atualizar_usuario_no_arquivo(usuario)

    print("\n--- Dados do Perfil ---")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['id']}")
    for key, value in perfil.items():
        if key not in ['contato_raw', 'aceitou_termos']:
            print(f"{key.replace('_', ' ').title()}: {value if value else 'Não informado'}")

    print("\n✅ Perfil finalizado e salvo com sucesso! Voltando ao MENU PACIENTE...")
