import bcrypt
import random

# ======== DADOS COMPLETOS DOS MÉDICOS E PACIENTES ========
medicos = [
    {
        "nome": "Dr. Marcos Vieira",
        "especialidade": "Pneumologia",
        "crm": "123456",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "Ana Paula Ribeiro", "condicao": "Asma brônquica leve", "remedio": "Budesonida 200mcg",
             "resultado": "Espirometria normal",
             "comunicacao": "Qual o melhor horário para usar o Budesonida 200mcg inalador?"},
            {"nome": "Lucas Ferreira", "condicao": "Asma brônquica leve", "remedio": "Salbutamol inalador",
             "resultado": "Pico de fluxo dentro do esperado",
             "comunicacao": "Preciso saber se posso usar Salbutamol antes de correr."},
            {"nome": "Mariana Silva", "condicao": "Bronquite leve", "remedio": "Fluticasona 125mcg",
             "resultado": "Exame de pulmão normal",
             "comunicacao": "Posso suspender a Fluticasona 125mcg temporariamente?"},
            {"nome": "Rafael Costa", "condicao": "Asma brônquica leve", "remedio": "Montelucaste 10mg",
             "resultado": "Pico de fluxo adequado", "comunicacao": "É seguro tomar Montelucaste 10mg à noite?"},
            {"nome": "Sofia Lima", "condicao": "Asma brônquica leve", "remedio": "Formoterol 12mcg",
             "resultado": "Espirometria normal", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Gabriel Santos", "condicao": "Bronquite leve", "remedio": "Budesonida 100mcg",
             "resultado": "Exame de pulmão sem alterações", "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "09:00 – Ana Paula Ribeiro (Asma brônquica leve / Budesonida 200mcg)",
            "10:00 – Lucas Ferreira (Asma brônquica leve / Salbutamol inalador)",
            "11:00 – Mariana Silva (Bronquite leve / Fluticasona 125mcg)",
            "12:00 – Rafael Costa (Asma brônquica leve / Montelucaste 10mg)",
            "13:00 – Sofia Lima (Asma brônquica leve / Formoterol 12mcg)",
            "14:00 – Gabriel Santos (Bronquite leve / Budesonida 100mcg)"
        ],
        "estudos": ["Estudo de Asma brônquica leve", "Pesquisa de Bronquite leve"]
    },
    {
        "nome": "Dra. Patrícia Mendes",
        "especialidade": "Dermatologia",
        "crm": "234567",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "Bruno Souza Lima", "condicao": "Dermatite atópica leve", "remedio": "Hidrocortisona 1%",
             "resultado": "Melhora da pele", "comunicacao": "Posso usar Hidrocortisona 1% diariamente?"},
            {"nome": "Laura Oliveira", "condicao": "Dermatite seborreica leve", "remedio": "Cetoconazol 2% shampoo",
             "resultado": "Melhora da pele", "comunicacao": "É seguro usar Cetoconazol 2% duas vezes por semana?"},
            {"nome": "Felipe Martins", "condicao": "Eczema leve", "remedio": "Mometasona 0,1% creme",
             "resultado": "Melhora da pele", "comunicacao": "Quanto tempo devo aplicar Mometasona 0,1%?"},
            {"nome": "Camila Rocha", "condicao": "Psoríase leve", "remedio": "Calcipotriol 0,005% pomada",
             "resultado": "Estável", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Pedro Almeida", "condicao": "Dermatite de contato leve", "remedio": "Dexametasona 0,05% creme",
             "resultado": "Estável", "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "10:00 – Bruno Souza Lima (Dermatite leve / Hidrocortisona 1%)",
            "11:00 – Laura Oliveira (Dermatite seborreica leve / Cetoconazol 2% shampoo)",
            "12:00 – Felipe Martins (Eczema leve / Mometasona 0,1% creme)",
            "13:00 – Camila Rocha (Psoríase leve / Calcipotriol 0,005% pomada)",
            "14:00 – Pedro Almeida (Dermatite de contato leve / Dexametasona 0,05% creme)"
        ],
        "estudos": ["Pesquisa de Dermatite leve", "Estudo de Eczema e Psoríase leve"]
    },
    {
        "nome": "Dr. André Moreira",
        "especialidade": "Neurologia",
        "crm": "345678",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "Carlos Mendes Silva", "condicao": "Epilepsia controlada", "remedio": "Fenitoína 100mg",
             "resultado": "EEG dentro do esperado",
             "comunicacao": "Há alguma restrição alimentar para Fenitoína 100mg?"},
            {"nome": "Mariana Figueiredo", "condicao": "Epilepsia parcial", "remedio": "Carbamazepina 200mg",
             "resultado": "Crises sob controle", "comunicacao": "Posso tomar Carbamazepina 200mg à noite?"},
            {"nome": "Tiago Nunes", "condicao": "Epilepsia generalizada", "remedio": "Valproato 500mg",
             "resultado": "Crises sob controle", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Vanessa Costa", "condicao": "Crises focais", "remedio": "Levetiracetam 500mg",
             "resultado": "Crises sob controle", "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "11:30 – Carlos Mendes Silva (Epilepsia controlada / Fenitoína 100mg)",
            "12:30 – Mariana Figueiredo (Epilepsia parcial / Carbamazepina 200mg)",
            "13:30 – Tiago Nunes (Epilepsia generalizada / Valproato 500mg)",
            "14:30 – Vanessa Costa (Crises focais / Levetiracetam 500mg)"
        ],
        "estudos": ["Pesquisa de Epilepsia controlada e parcial"]
    },
    {
        "nome": "Dra. Luciana Castro",
        "especialidade": "Gastroenterologia",
        "crm": "456789",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "Maria Oliveira Costa", "condicao": "Gastrite crônica moderada", "remedio": "Omeprazol 20mg",
             "resultado": "Exames dentro do esperado",
             "comunicacao": "Devo evitar algum alimento enquanto tomo Omeprazol 20mg?"},
            {"nome": "Bruno Carvalho", "condicao": "Refluxo gastroesofágico moderado", "remedio": "Esomeprazol 40mg",
             "resultado": "Melhora com medicação", "comunicacao": "Posso tomar Esomeprazol 40mg em jejum?"},
            {"nome": "Juliana Lima", "condicao": "Gastrite erosiva moderada", "remedio": "Pantoprazol 40mg",
             "resultado": "Melhora com medicação", "comunicacao": "Qual horário é melhor para Pantoprazol 40mg?"},
            {"nome": "Rafael Mendes", "condicao": "Dispepsia funcional moderada", "remedio": "Domperidona 10mg",
             "resultado": "Exames normais", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Carolina Souza", "condicao": "Gastrite moderada", "remedio": "Ranitidina 150mg",
             "resultado": "Exames normais", "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "14:00 – Maria Oliveira Costa (Gastrite crônica moderada / Omeprazol 20mg)",
            "15:00 – Bruno Carvalho (Refluxo gastroesofágico moderado / Esomeprazol 40mg)",
            "15:30 – Juliana Lima (Gastrite erosiva moderada / Pantoprazol 40mg)",
            "16:00 – Rafael Mendes (Dispepsia funcional moderada / Domperidona 10mg)",
            "16:30 – Carolina Souza (Gastrite moderada / Ranitidina 150mg)"
        ],
        "estudos": ["Pesquisa de Gastrite crônica e erosiva", "Estudo de Refluxo gastroesofágico"]
    },
    {
        "nome": "Dr. Ricardo Alves",
        "especialidade": "Nefrologia",
        "crm": "789012",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "João Silva Martins", "condicao": "Insuficiência renal crônica grave", "remedio": "Losartana 50mg",
             "resultado": "Creatinina elevada", "comunicacao": "Doutor, posso ajustar a dose do Losartana 50mg?"},
            {"nome": "Felipe Santos", "condicao": "Insuficiência renal leve", "remedio": "Captopril 25mg",
             "resultado": "Função renal estável", "comunicacao": "É seguro tomar Captopril 25mg à noite?"},
            {"nome": "Mariana Rodrigues", "condicao": "Insuficiência renal moderada", "remedio": "Enalapril 10mg",
             "resultado": "Creatinina levemente elevada",
             "comunicacao": "Devo monitorar dieta enquanto tomo Enalapril 10mg?"},
            {"nome": "Rafael Lima", "condicao": "Insuficiência renal grave", "remedio": "Furosemida 40mg",
             "resultado": "Creatinina elevada, risco de progressão", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Ana Beatriz Costa", "condicao": "Insuficiência renal grave", "remedio": "Espironolactona 25mg",
             "resultado": "Função renal comprometida", "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Lucas Martins", "condicao": "Insuficiência renal grave", "remedio": "Metolazona 5mg",
             "resultado": "Função renal crítica", "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "16:00 – João Silva Martins (Insuficiência renal grave / Losartana 50mg)",
            "16:30 – Felipe Santos (Insuficiência renal leve / Captopril 25mg)",
            "17:00 – Mariana Rodrigues (Insuficiência renal moderada / Enalapril 10mg)",
            "17:30 – Rafael Lima (Insuficiência renal grave / Furosemida 40mg)",
            "18:00 – Ana Beatriz Costa (Insuficiência renal grave / Espironolactona 25mg)",
            "18:30 – Lucas Martins (Insuficiência renal grave / Metolazona 5mg)"
        ],
        "estudos": ["Acompanhamento de Insuficiência renal crônica leve a grave"]
    },
    {
        "nome": "Dra. Renata Fonseca",
        "especialidade": "Cardiologia",
        "crm": "567890",
        "senha": bcrypt.hashpw("Medico@2025".encode(), bcrypt.gensalt()).decode(),
        "pacientes": [
            {"nome": "Fernanda Lima Alves", "condicao": "Insuficiência cardíaca congestiva grave",
             "remedio": "Furosemida 40mg + Enalapril 10mg", "resultado": "Eletrocardiograma alterado",
             "comunicacao": "Preciso de orientação sobre a medicação Furosemida 40mg + Enalapril 10mg."},
            {"nome": "Carla Souza", "condicao": "Insuficiência cardíaca leve", "remedio": "Captopril 25mg",
             "resultado": "Exames dentro do esperado", "comunicacao": "É seguro usar Captopril 25mg diariamente?"},
            {"nome": "Tiago Ferreira", "condicao": "Insuficiência cardíaca grave",
             "remedio": "Metoprolol 50mg + Furosemida 40mg", "resultado": "Exames com sinais de insuficiência",
             "comunicacao": "Posso ajustar o horário do Metoprolol 50mg?"},
            {"nome": "Juliana Martins", "condicao": "Insuficiência cardíaca grave",
             "remedio": "Carvedilol 25mg + Espironolactona 25mg", "resultado": "Alterações no ECG, risco alto",
             "comunicacao": "Sem dúvida clínica adicional."},
            {"nome": "Pedro Lima", "condicao": "Insuficiência cardíaca grave",
             "remedio": "Enalapril 10mg + Furosemida 40mg", "resultado": "Função cardíaca comprometida",
             "comunicacao": "Sem dúvida clínica adicional."},
        ],
        "agenda": [
            "17:30 – Fernanda Lima Alves (Insuficiência cardíaca grave / Furosemida 40mg + Enalapril 10mg)",
            "18:00 – Carla Souza (Insuficiência cardíaca leve / Captopril 25mg)",
            "18:30 – Tiago Ferreira (Insuficiência cardíaca grave / Metoprolol 50mg + Furosemida 40mg)",
            "19:00 – Juliana Martins (Insuficiência cardíaca grave / Carvedilol 25mg + Espironolactona 25mg)",
            "19:30 – Pedro Lima (Insuficiência cardíaca grave / Enalapril 10mg + Furosemida 40mg)"
        ],
        "estudos": ["Acompanhamento de Insuficiência cardíaca leve a grave"]
    }
]


# ======== FUNÇÕES DE AUTENTICAÇÃO ========
def autenticar_medico():
    crm_input = input("Digite seu CRM: ")
    senha_input = input("Digite sua senha: ")

    for medico in medicos:
        if medico["crm"] == crm_input:
            if bcrypt.checkpw(senha_input.encode(), medico["senha"].encode()):
                print("Senha correta!")
                # MFA simples
                codigo_mfa = str(random.randint(100000, 999999))
                print(f"Código MFA enviado (simulado): {codigo_mfa}")
                codigo_input = input("Digite o código MFA: ")
                if codigo_input == codigo_mfa:
                    print(f"Bem-vindo(a) {medico['nome']}!\n")
                    return medico
                else:
                    print("Código MFA incorreto.")
                    return None
            else:
                print("Senha incorreta.")
                return None
    print("CRM não encontrado.")
    return None


# ======== FUNÇÃO PARA EXIBIR DADOS DO MÉDICO ========
def exibir_quadro_acompanhamento(medico):
    pacientes_hoje = len(medico["agenda"])
    grau_leve = sum(1 for p in medico["pacientes"] if "leve" in p["condicao"].lower())
    grau_moderado = sum(1 for p in medico["pacientes"] if "moderado" in p["condicao"].lower())
    grau_alto = sum(1 for p in medico["pacientes"] if "grave" in p["condicao"].lower())

    print("🔹 Quadro de Acompanhamento")
    print(f"Pacientes hoje: {pacientes_hoje}")
    print(f"Grau leve: {grau_leve}")
    print(f"Grau moderado: {grau_moderado}")
    print(f"Grau alto: {grau_alto}")
    print("Alertas: nenhum\n")

    print("2️⃣ Perfil do Especialista")
    print(f"👤 {medico['nome']}")
    print(f"Especialidade: {medico['especialidade']}")
    print(f"CRM: {medico['crm']}")
    print(f"Pacientes sob acompanhamento: {len(medico['pacientes'])}\n")

    print("Pacientes e condições:")
    for p in medico["pacientes"]:
        print(f"{p['nome']} – {p['condicao']} ({p['remedio']})")

    print("\n3️⃣ Agenda")
    for a in medico["agenda"]:
        print(a)

    print("\n4️⃣ Estudos Clínicos 🧪")
    for e in medico["estudos"]:
        print(e)

    print("\n5️⃣ Resultados e Relatórios 📄")
    for p in medico["pacientes"]:
        print(f"{p['nome']} – {p['resultado']}")

    print("\n6️⃣ Comunicação 💬")
    for p in medico["pacientes"]:
        print(f"{p['nome']}: \"{p['comunicacao']}\"")
    print("\n========================\n")


# ======== LOOP PRINCIPAL ========
def main():
    medico = autenticar_medico()
    if medico:
        exibir_quadro_acompanhamento(medico)


if __name__ == "__main__":
    main()
