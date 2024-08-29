import pandas as pd
import os

# Carregar o Arquivo CSV
dataFrame = pd.read_csv('top250-00-19.csv')

# Agrupa por clube e apresenta os 10 clubes com maior número de compras
def top10ClubesCompras(dataFrame):
    topClubes = dataFrame['Team_to'].value_counts().head(10)          # Conta a quantidade de vezes um clube aparece na coluna 'Team_to'
    print("| Top 10 clubes com maior número de compras:        |")
    for club, count in topClubes.items():
        print(f"| {club.ljust(30)}: {count} compras        |")

# Classifica por valor e apresenta os 10 maiores
def top10Transferencias(dataFrame):
    dataFrame_sorted = dataFrame.sort_values(by='Transfer_fee', ascending=False).head(10).reset_index(drop=True)  # Classifica pelo valor e pega os 10 maiores, reseta o index para não apresentar a linha e sim o top 10
    dataFrame_sorted.index += 1
    
    dataFrame_sorted = dataFrame_sorted.rename(columns={'Name': 'Nome', 'Team_to': 'Time', 'Transfer_fee': 'Transferência'}) # Renomeia as colunas para ficar tudo em português
    dataFrame_sorted['Transferência'] = dataFrame_sorted['Transferência'].map('${:,.2f}'.format) # Formata a coluna de transferência para exibir em formato de moeda
    
    print("| Top 10 maiores transações:                        |")
    print(dataFrame_sorted[['Nome', 'Time', 'Transferência']])

# Compara a quantidade de jogadores comprados por 2 clubes
def compararClubes(dataFrame, clube1, clube2):
    clube1Count = dataFrame[dataFrame['Team_to'] == clube1].shape[0]
    clube2Count = dataFrame[dataFrame['Team_to'] == clube2].shape[0]

    os.system('cls' if os.name == 'nt' else 'clear')

    print(interfacemenu)
    print("| Comparação de clubes:                             |")
    print(f"| {clube1.ljust(18)}: Possui {clube1Count} jogadores comprados |")
    print(f"| {clube2.ljust(18)}: Possui {clube2Count} jogadores comprados |")


# Pesquisa por nome do jogador
def buscarJogadorNome(dataFrame, playerNome):
    players = dataFrame[dataFrame['Name'].str.contains(playerNome, case=False, na=False)].reset_index(drop=True) # Procura todas as ocorrencias do nome escrito na coluna 'Name' ignorando maiúsculas e minúsculas
    players.index += 1

    players = players.rename(columns={'Name': 'Nome', 'Team_to': 'Time', 'Transfer_fee': 'Transferência'})
    players['Transferência'] = players['Transferência'].map('${:,.2f}'.format)
    if not players.empty:
        print("| Jogadores encontrados:                            |")
        print(players[['Nome', 'Time', 'Transferência']])
    else:
        print(f"| Nenhum jogador encontrado com o nome '{playerNome}' |")

# Agrupa jogadores por idade
def jogadoresPorIdade(dataFrame):
    grupoIdade = dataFrame['Age'].value_counts().sort_index()
    print("Número de jogadores negociados por idade:")
    for idade, count in grupoIdade.items():
        print(f"Idade: {idade} - Número de jogadores: {count}")

# Tinha um jogador com a idade 0, então foi necessário corrigir o arquivo CSV.

interfacemenu = '|---------------------- Menu -----------------------|'
interfaceFinal = '|---------------------------------------------------|'


while(True):
    os.system('cls' if os.name == 'nt' else 'clear')

    print (interfacemenu)
    print ('| 1 - Top 10 clubes com maior número de compras     |')
    print ('| 2 - Top 10 maiores transações                     |')
    print ('| 3 - Comparar 2 clubes (Transações)                |')
    print ('| 4 - Pesquisar jogador por nome                    |')
    print ('| 5 - Agrupar jogadores por idade                   |')
    print ('| 0 - Sair                                          |')
    print (interfaceFinal)
    opcao = input('Digite a opção desejada: ')

    if opcao == '1':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(interfacemenu)
        top10ClubesCompras(dataFrame)
        print(interfaceFinal)
        
        input('Pressione Enter para continuar')
    elif opcao == '2':
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(interfacemenu)
        top10Transferencias(dataFrame)
        print(interfaceFinal)

        input('Pressione Enter para continuar')
    elif opcao == '3':
        os.system('cls' if os.name == 'nt' else 'clear')

        print(interfacemenu)
        clube1 = input('Digite o nome do clube 1: ')
        clube2 = input('Digite o nome do clube 2: ')
        compararClubes(dataFrame, clube1, clube2)
        print(interfaceFinal)

        input('Pressione Enter para continuar')
    elif opcao == '4':
        os.system('cls' if os.name == 'nt' else 'clear')

        print(interfacemenu)
        playerNome = input('Digite o nome do jogador: ')
        buscarJogadorNome(dataFrame, playerNome)
        print(interfaceFinal)

        input('Pressione Enter para continuar')
    elif opcao == '5':
        os.system('cls' if os.name == 'nt' else 'clear')

        print(interfacemenu)
        jogadoresPorIdade(dataFrame)
        print(interfaceFinal)

        input('Pressione Enter para continuar')
    elif opcao == '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        break
    else:
        print('Opção inválida!')
        input('Pressione Enter para continuar')
        os.system('cls' if os.name == 'nt' else 'clear')
    

