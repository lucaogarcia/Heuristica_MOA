#Versao professor




# Definir as distâncias das cidades e criar um método para contar o número de cidades
distancias = [
    [0, 186, 105, 208, 177, 94],
    [187, 0, 86.8, 223, 255, 254],
    [99.9, 89, 0, 203, 204, 172],
    [206, 220, 203, 0, 377, 295],
    [168, 251, 201, 376, 0, 156],
    [86.8, 255, 173, 293, 159, 0]
]

num_cidades = len(distancias)

# Criar um método que verifica a cidade mais próxima que ainda não tenha passado

inicio = 5
num_cidades = len(distancias)
rota = [inicio]  # Começamos na cidade 0 (cidade de origem)
visitadas = []  # Cidades visitadas identificadas por índices
visitadas.append(rota[0])

# Criar um loop para encontrar a próxima cidade mais perto
while len(visitadas) < num_cidades:   
    cidade_atual = rota[len(rota)-1]
    distancia_menor = float('inf')
    cidade_vizinha = None
    

    for proxima_cidade in range(num_cidades):
        if proxima_cidade not in visitadas and distancias[cidade_atual][proxima_cidade] < distancia_menor:
                if distancias[cidade_atual][proxima_cidade] != 0:
                    distancia_menor = distancias[cidade_atual][proxima_cidade]
                    cidade_vizinha = proxima_cidade
                

    if cidade_vizinha is not None:
        rota.append(cidade_vizinha)
        visitadas.append(cidade_vizinha)

# Adicione o retorno para a cidade de origem
rota.append(inicio)
#return rota

#rota = cidade_mais_proxima(distancias)

# Calcule a distância total da rota
distancia_total = sum(distancias[rota[i]][rota[i + 1]] for i in range(num_cidades))
print("Rota:", rota)
print("Distância total percorrida:", distancia_total)




#Versao Par Impar




def encontrar_menor_valor_na_coluna(matriz, coluna, cidades_visitadas):
    menor_valor = float('inf')
    cidade_escolhida = -1

    for linha in range(len(matriz)):
        if linha not in cidades_visitadas and matriz[linha][coluna] < menor_valor:
            menor_valor = matriz[linha][coluna]
            cidade_escolhida = linha

    print("Menor valor na coluna:", menor_valor, "Cidade escolhida:", cidade_escolhida)
    return cidade_escolhida, menor_valor


def encontrar_menor_valor_na_linha(matriz, linha, cidades_visitadas):
    menor_valor = float('inf')
    cidade_escolhida = -1

    for coluna, valor in enumerate(matriz[linha]):
        if coluna not in cidades_visitadas and valor < menor_valor:
            menor_valor = valor
            cidade_escolhida = coluna

    print("Menor valor na linha:", menor_valor, "Cidade escolhida:", cidade_escolhida)
    return cidade_escolhida, menor_valor


def caminho_intercalado(matriz, cidade_inicial=0):
    num_cidades = len(matriz)
    caminho = [cidade_inicial]
    cidades_visitadas = {cidade_inicial}
    coordenadas_caminho = []

    while len(caminho) < num_cidades:
        cidade_atual = caminho[-1]
        if cidade_atual % 2 == 0:  # Se o índice da cidade atual for par, encontre na linha
            cidade_linha, menor_valor_linha = encontrar_menor_valor_na_linha(matriz, cidade_atual, cidades_visitadas)
            if cidade_linha is not None:
                caminho.append(cidade_linha)
                cidades_visitadas.add(cidade_linha)
                coordenadas_caminho.append((cidade_atual, cidade_linha))
        else:  # Caso contrário, encontre na coluna
            cidade_coluna, menor_valor_coluna = encontrar_menor_valor_na_coluna(matriz, cidade_atual, cidades_visitadas)
            if cidade_coluna is not None:
                caminho.append(cidade_coluna)
                cidades_visitadas.add(cidade_coluna)
                coordenadas_caminho.append((cidade_coluna, cidade_atual))

    # Voltar a cidade inicial
    coordenadas_caminho.append((caminho[-1], cidade_inicial))

    # Soma dos valores
    soma = sum(
        matriz[linha][coluna] for linha, coluna in coordenadas_caminho if matriz[linha][coluna] > 0)

    return soma, caminho, coordenadas_caminho


# Exemplo de matriz
matriz = [
    [0, 186, 105, 208, 177, 94],
    [187, 0, 86.8, 223, 255, 254],
    [99.9, 89, 0, 203, 204, 172],
    [206, 220, 203, 0, 377, 295],
    [168, 251, 201, 376, 0, 156],
    [86.8, 255, 173, 293, 159, 0]
]

cidade_origem = int(input(f"Digite a cidade de origem (0 a {len(matriz) - 1}): "))

if cidade_origem < 0 or cidade_origem >= len(matriz):
    print("Cidade de origem inválida.")
else:
    soma, caminho, coordenadas = caminho_intercalado(matriz, cidade_origem)
    print("Soma dos valores no caminho:", soma)
    print("Caminho no formato de índices de cidades:")
    print(caminho)
