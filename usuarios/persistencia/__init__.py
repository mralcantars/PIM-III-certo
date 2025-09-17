import json

def atualizar_usuario_no_arquivo(usuario_a_atualizar):
    usuarios_existentes = []
    try:
        with open("usuarios.json", "r") as f:
            for linha in f:
                usuarios_existentes.append(json.loads(linha))
    except FileNotFoundError:
        pass

    for i, u in enumerate(usuarios_existentes):
        if u["id"] == usuario_a_atualizar["id"]:
            usuarios_existentes[i] = usuario_a_atualizar
            break
    else:
        usuarios_existentes.append(usuario_a_atualizar)

    with open("usuarios.json", "w") as f:
        for u in usuarios_existentes:
            f.write(json.dumps(u) + "\n")
