# Versao Professor

print('\n -----------Heur�stica Principal 1-----------\n')

# Defina peso maximo mochila e uma lista de objetos
peso_max_mochila = 5000
objetos = [
    {"id": 0, "peso": 200, "utilidade": 6},
    {"id": 1, "peso": 1000, "utilidade": 9},
    {"id": 2, "peso": 400, "utilidade": 7},
    {"id": 3, "peso": 400, "utilidade": 3},
    {"id": 4, "peso": 200, "utilidade": 5},
    {"id": 5, "peso": 3000, "utilidade": 10},
    {"id": 6, "peso": 100, "utilidade": 2},
    {"id": 7, "peso": 500, "utilidade": 6},
]
'''
objetos = [
    {"id": 0, "peso": 450, "utilidade": 15},
    {"id": 1, "peso": 700, "utilidade": 20},
    {"id": 2, "peso": 600, "utilidade": 10},
    {"id": 3, "peso": 800, "utilidade": 12},
    {"id": 4, "peso": 700, "utilidade": 5},
    {"id": 5, "peso": 650, "utilidade": 18},
    {"id": 6, "peso": 1000, "utilidade": 25},
    {"id": 7, "peso": 900, "utilidade": 22},
    {"id": 8, "peso": 1000, "utilidade": 16},
]

'''


# METODO DE ORDENA��O 1 : ele ordena levado em conta o calculo de utilidade/peso
def calcular_relacao(objeto):
    return objeto["utilidade"] / objeto["peso"]


# Ordenar os objetos com base na rela��o utilidade/peso em ordem decrescente
objetos_ordenados = sorted(objetos, key=calcular_relacao, reverse=True)
# Exiba a lista ordenada
print('\nObjetos ordenados decrescentemente pela fu��o da rela��o de utilidade/peso dos objetos :\n')
for objeto in objetos_ordenados:
    print(f"ID: {objeto['id']} - Peso: {objeto['peso']} - Utilidade: {objeto['utilidade']}")

# Montando a Mochila
peso_mochila = 0
mochila = []
cama = []
utilidade_final = 0

print('\n -----------Montando a Mochila 1-----------\n')

for objeto in objetos_ordenados:
    peso_acrescimo = objeto["peso"] + peso_mochila

    if peso_acrescimo > peso_max_mochila:
        print(
            f"O objeto {objeto['id']} � pesado demais para entra na mochila Peso atual {peso_mochila} peso do objeto {objeto['peso']}")
        cama.append(objeto)

    elif peso_acrescimo < peso_max_mochila:
        peso_mochila = peso_acrescimo
        utilidade_final += objeto['utilidade']
        mochila.append(objeto)
        # print(f'Dentro da mochila: {mochila}')
        print(
            f"Objeto {objeto['id']} entra na mochila, pesso atual � de {peso_mochila} com utilidade {utilidade_final}")

    else:
        print('\n-------------MOCHILA CHEIA-------------')

print("\nObjetos dentro da mochila (IDs):", [objeto["id"] for objeto in mochila])
print("Objetos na cama (IDs):", [objeto["id"] for objeto in cama])
print("Utilidade da mochila:", utilidade_final)

# Heur�stica de Molhoramento

print('\n -----------Heur�stica de Melhoramento 1-----------\n')
print(
    'Faremos a tenatriva de almentar a utilidade total da nossa mochila, atravez da substitui��o dos objetos da mochila por aqueles que n�o colberam.')
print('Levando em conta o peso que a mochila ainda pode aguentar e o peso dos objetos sunbstituidos.\n')
sobra_peso = peso_max_mochila - peso_mochila

melhor_utilidade_final = utilidade_final
melhor_mochila = mochila.copy()

for objeto_mochila in mochila:
    for objeto_cama in cama:
        # Calcule o peso restante na mochila ap�s a troca
        peso_restante = peso_max_mochila - (peso_mochila - objeto_mochila["peso"] + objeto_cama["peso"])

        if peso_restante >= 0:  # Verifique se a troca � poss�vel em termos de peso
            # Calcule a utilidade total ap�s a troca
            utilidade_apos_troca = utilidade_final - objeto_mochila["utilidade"] + objeto_cama["utilidade"]

            if utilidade_apos_troca > melhor_utilidade_final:  # Verifique se a troca aumentaria a utilidade total
                # Realize a troca
                peso_mochila = peso_mochila - objeto_mochila["peso"] + objeto_cama["peso"]
                utilidade_final = utilidade_apos_troca
                mochila.remove(objeto_mochila)
                cama.remove(objeto_cama)
                mochila.append(objeto_cama)
                cama.append(objeto_mochila)

                # Atualize a melhor combina��o encontrada at� agora
                melhor_utilidade_final = utilidade_final
                melhor_mochila = mochila.copy()

# Exiba a melhor utilidade final e a lista de objetos na melhor combina��o
print("\nMelhor utilidade final ap�s as trocas:", melhor_utilidade_final)
print("Melhor combina��o de objetos na mochila ap�s as trocas (IDs):", [objeto["id"] for objeto in melhor_mochila])
print("Objetos sobre a cama (IDs):", [objeto["id"] for objeto in cama])

# Fim
print('\n -----------FINALIZANDO MOCHILA 1-----------\n')
print("Dentro da mochila:", [objeto["id"] for objeto in melhor_mochila])
print("Objetos sobre a cama (IDs):", [objeto["id"] for objeto in cama])
print(f"O pesso final � de {peso_mochila} com utilidade de {utilidade_final}\n")

# Versao Galieta e Garcia


print('\n -----------Heur�stica Principal 2-----------\n')
# METODO DE ORDENA��O 2 : ele ordena levando em conta a utilidade do maior para o menor
# Ordene a lista de objetos com base na utilidade (em ordem decrescente)
# e, em caso de colis�o na utilidade, ordene pelo peso (em ordem crescente)
objetos_ordenados = sorted(objetos, key=lambda x: (-x["utilidade"], x["peso"]))

# Exiba a lista ordenada
print('\nObjetos ordenados decrescentemente pela sua Utidildade e em caso de colis�o pele menor peso :\n')
for objeto in objetos_ordenados:
    print(f"ID: {objeto['id']} - Peso: {objeto['peso']} - Utilidade: {objeto['utilidade']}")

# Montando a Mochila 2
peso_mochila = 0
mochila = []
cama = []
utilidade_final = 0

print('\n -----------Montando a Mochila 2-----------\n')

for objeto in objetos_ordenados:
    peso_acrescimo = objeto["peso"] + peso_mochila

    if peso_acrescimo > peso_max_mochila:
        print(
            f"O objeto {objeto['id']} � pesado demais para entra na mochila Peso atual {peso_mochila} peso do objeto {objeto['peso']}")
        cama.append(objeto)

    elif peso_acrescimo < peso_max_mochila:
        peso_mochila = peso_acrescimo
        utilidade_final += objeto['utilidade']
        mochila.append(objeto)
        # print(f'Dentro da mochila: {mochila}')
        print(
            f"Objeto {objeto['id']} entra na mochila, pesso atual � de {peso_mochila} com utilidade {utilidade_final}")

    else:
        print('\n-------------MOCHILA CHEIA-------------')

print("\nObjetos dentro da mochila 2 (IDs):", [objeto["id"] for objeto in mochila])
print("Objetos dentro da cama 2 (IDs):", [objeto["id"] for objeto in cama])
print("Utilidade da mochila 2 :", utilidade_final)

# Fim
print('\n -----------FINALIZANDO MOCHILA 2-----------\n')
print("Dentro da mochila:", [objeto["id"] for objeto in melhor_mochila])
print("Objetos dentro da cama (IDs):", [objeto["id"] for objeto in cama])
print(f"O pesso final � de {peso_mochila} com utilidade de {utilidade_final}\n")
