import os
import json
from datetime import datetime

# Configurações do sistema
DATA_FILE = "doacoes.json"
BACKUP_FOLDER = "backups"

# Cria diretório de backups se não existir
if not os.path.exists(BACKUP_FOLDER):
    os.makedirs(BACKUP_FOLDER)

# Função para fazer backup dos dados
def fazer_backup():
    if os.path.exists(DATA_FILE):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = os.path.join(BACKUP_FOLDER, f"backup_{timestamp}.json")
        
        with open(DATA_FILE, "r") as original:
            data = original.read()
            with open(backup_file, "w") as backup:
                backup.write(data)
        
        print(f"Backup criado: {backup_file}")

# Função para carregar dados existentes
def carregar_dados():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Função para salvar dados
def salvar_dados(dados):
    with open(DATA_FILE, "w") as file:
        json.dump(dados, file, indent=2)
    fazer_backup()

# Função básica para ofuscar dados (não é criptografia real)
def ofuscar_dado(dado):
    return ''.join([chr(ord(c) + 1) for c in str(dado)])

# Função para cadastrar doação
def cadastrar_doacao():
    print("\n--- Cadastro de Doação ---")
    
    # Validação do nome
    while True:
        nome = input("Nome completo: ").strip()
        if nome:
            break
        print("Nome é obrigatório!")
    
    # Validação da idade
    while True:
        idade = input("Idade: ")
        if idade.isdigit() and int(idade) > 0:
            idade = int(idade)
            break
        print("Digite uma idade válida (número positivo)!")
    
    # Validação do valor
    while True:
        valor = input("Valor da doação R$: ").replace(",", ".")
        try:
            valor = float(valor)
            if valor > 0:
                break
            print("O valor deve ser positivo!")
        except ValueError:
            print("Digite um valor numérico válido!")
    
    # Cria novo registro
    nova_doacao = {
        "nome_ofuscado": ofuscar_dado(nome),
        "idade": idade,
        "valor": valor,
        "data": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    
    # Salva os dados
    dados = carregar_dados()
    dados.append(nova_doacao)
    salvar_dados(dados)
    
    print("\nDoação registrada com sucesso!")

# Função para calcular estatísticas básicas
def calcular_estatisticas(dados):
    if not dados:
        return None
    
    total = len(dados)
    soma_valores = sum(item["valor"] for item in dados)
    media_valores = soma_valores / total
    idades = [item["idade"] for item in dados]
    media_idades = sum(idades) / total
    
    return {
        "total_doacoes": total,
        "total_arrecadado": soma_valores,
        "media_doacao": media_valores,
        "maior_doacao": max(item["valor"] for item in dados),
        "menor_doacao": min(item["valor"] for item in dados),
        "media_idade": media_idades,
        "doador_mais_novo": min(idades),
        "doador_mais_velho": max(idades)
    }

# Função para exibir relatórios
def gerar_relatorios():
    dados = carregar_dados()
    
    if not dados:
        print("\nNenhuma doação registrada ainda.")
        return
    
    stats = calcular_estatisticas(dados)
    
    print("\n=== RELATÓRIO ESTATÍSTICO ===")
    print(f"Total de doações: {stats['total_doacoes']}")
    print(f"Total arrecadado: R$ {stats['total_arrecadado']:.2f}")
    print(f"Média por doação: R$ {stats['media_doacao']:.2f}")
    print(f"Maior doação: R$ {stats['maior_doacao']:.2f}")
    print(f"Menor doação: R$ {stats['menor_doacao']:.2f}")
    print(f"\nIdade média dos doadores: {stats['media_idade']:.1f} anos")
    print(f"Doador mais novo: {stats['doador_mais_novo']} anos")
    print(f"Doador mais velho: {stats['doador_mais_velho']} anos")

# Menu principal
def main():
    while True:
        print("\n=== SISTEMA DE DOAÇÕES ===")
        print("1. Cadastrar nova doação")
        print("2. Gerar relatórios")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ").strip()
        
        if opcao == "1":
            cadastrar_doacao()
        elif opcao == "2":
            gerar_relatorios()
        elif opcao == "3":
            print("Obrigado por usar o sistema!")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
