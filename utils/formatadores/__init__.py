import datetime

def formatar_cpf(cpf: str) -> str:
    """Formata o CPF no padrão 000.000.000-00"""
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"


def formatar_telefone(telefone: str) -> str:
    """Formata telefone com DDD no padrão (XX) XXXXX-XXXX"""
    if len(telefone) == 11:
        return f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone


def validar_cpf(cpf: str) -> bool:
    """Verifica se o CPF tem 11 dígitos numéricos"""
    return cpf.isdigit() and len(cpf) == 11


def validar_telefone(telefone: str) -> bool:
    """Verifica se o telefone tem 11 dígitos numéricos"""
    return telefone.isdigit() and len(telefone) == 11


def validar_email(email: str) -> bool:
    """Validação simples de e-mail"""
    return "@" in email and "." in email

def limpar_formatacao_cpf(cpf_formatado: str) -> str:
    """Remove pontos e traço do CPF formatado"""
    return cpf_formatado.replace(".", "").replace("-", "")


def limpar_formatacao_telefone(telefone_formatado: str) -> str:
    """Remove parênteses, espaço e traço do telefone formatado"""
    return telefone_formatado.replace("(", "").replace(")", "").replace(" ", "").replace("-", "")

