# coding: utf-8

import csv
import matplotlib.pyplot as plt

print("""
      ------__o
    -------_\ <,_
----------(_)/ (_)

BIKESHARE - ANÁLISE DE DADOS
Udacity - Fundamentos de AI e ML
Renato César
""")

print("Carregando os dados. Por favor, aguarde...")
#C:\ferramentas-desenvolvimento\Workspace-python\chicago.csv
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)

print("Número de linhas: {}".format(len(data_list)))
print("Linha 0: {}".format(data_list[0]))
print("Linha 1: {}".format(data_list[1]))

input("\n\nAperte ENTER para continuar...")

data_list = data_list[1:]

# TAREFA 1
# Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for data in data_list[:20]:
    print(data)

input("\n\nAperte ENTER para continuar...")

# TAREFA 2
# Imprima o `gênero` das primeiras 20 linhas
print("\n\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for data in data_list[:20]:
    gender = data[6]
    print('{} Gênero {}'.format(data_list.index(data), gender))

input("\n\nAperte ENTER para continuar...")

# TAREFA 3
# Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
       Função para retornar uma coluna como lista
       Argumentos:
          data: Lista com os dados
          index: Indíce da coluna
       Retorno:
          column_list: Lista com os dados da coluna indexada
    """
    column_list = []
    for line in data:
        column_list.append(line[index])
    return column_list

# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("\n\nAperte ENTER para continuar...")

# TAREFA 4
# Conte cada gênero. Você não deveria usar uma função para isso.
genders = column_to_list(data_list, -2)
male = genders.count('Male')
female = genders.count('Female')

print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("\n\nAperte ENTER para continuar...")

# TAREFA 5
# Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
       Função para calcular o total de cada gênero da lista
       Argumentos:
          data_list: Lista de registros de bicicletas compartilhadas
       Retorno:
          Retorna uma lista onde o primeiro indíce é quantidade do gênero Masculino
          e o segundo índice é a quantidade do gênero Feminino

          Exemplo: [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
    """
    genders = column_to_list(data_list, -2)
    male = genders.count("Male")
    female = genders.count("Female")
    return [male, female]

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("\n\nAperte ENTER para continuar...")

# TAREFA 6
# Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
       Calcula o gênero mais popular de uma lista
       Através da função count_gender obtém a quantidade de cada gênero
       Argumento:
          data_list: Lista de registros de bicicletas compartilhadas
       Retorno:
          answer: Retorna uma string com o gênero mais popular (Masculino ou Feminino)
          Caso a quantidade seja idêntica, retorna (Igual)
    """
    genders = count_gender(data_list)
    answer = ""
    if genders[0] > genders[1]:
        answer = "Masculino"
    elif genders[0] < genders[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer

print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Masculino", "Feminino"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=False)

input("\n\nAperte ENTER para continuar...")

# TAREFA 7
# Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")
def count_user_type(users):
    """
       Função para calcular o total de cada tipo de usuário (Subscriber ou Customer)
       Argumentos:
          data_list: Lista de usuários
       Retorno:
          Retorna uma lista onde o primeiro indíce é quantidade de usuários tipo (Subscriber)
          e o segundo índice é a quantidade de usuários tipo (Customer)
          Exemplo: [subscriber, customer] (exemplo: [10, 15] significa 10 subscriber, 15 customer)
    """
    subscriber = users.count("Subscriber")
    customer = users.count("Customer")
    return [subscriber, customer]

users = column_to_list(data_list, -3)

print("\nImprimindo resultado de count_user_type:")
print(count_user_type(users))

types_users = ["Assinantes", "Clientes"]
quantity_users = count_user_type(users)
y_pos_users = list(range(len(types_users)))
plt.bar(y_pos_users, quantity_users)
plt.ylabel('Quantidade')
plt.xlabel('Tipo de usuário')
plt.xticks(y_pos_users, types_users)
plt.title('Quantidade por usuário')
plt.show(block=True)


input("\n\nAperte ENTER para continuar...")

# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "A afirmação é falsa pois existem registros da lista onde o gênero é nulo. Portanto o total de linhas não é igual a quantidade de gêneros cadastrados."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("\n\nAperte ENTER para continuar...")

# TAREFA 9
#Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = sorted(list(map(int, trip_duration_list)))

min_trip, max_trip, mean_trip, median_trip  = 0, 0, 0, 0

print("\nImprimindo uma amostra da lista de duração das viagens")
print(trip_duration_list[:10])

min_trip = trip_duration_list[0]
max_trip = trip_duration_list[len(trip_duration_list) - 1]

def calculate_mean_trip(list_duration):
    """
       Função para calcular o tempo médio das viagens
       Argumento:
          list_duration: Lista com os dados de trip_duration
       Retorno:
          mean_trip: Média de tempo das viagens
    """
    sum_duration = 0
    for duration in list_duration:
        sum_duration += duration
    mean_trip = round(sum_duration/len(list_duration))
    return mean_trip

def calculate_median_trip(list_duration):
    """
       Função para calcular o mediana de tempo das viagens
       Argumento:
          list_duration: Lista com os dados de trip_duration
       Retorno:
          median_trip: Mediana de tempo das viagens
    """
    size_list = len(list_duration) + 1
    index = round(size_list / 2)
    median_trip = list_duration[index]
    return median_trip

mean_trip = calculate_mean_trip(trip_duration_list)
median_trip = calculate_median_trip(trip_duration_list)

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("\n\nAperte ENTER para continuar...")

# TAREFA 10
# Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:

input("\n\nAperte ENTER para continuar...")

# TAREFA 12
# Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = input("Você vai encarar o desafio? (s / n) -> ")

def count_items(column_list):
    item_types = []
    count_items = []
    item_types = set(column_list)
    for item in item_types:
        occurrences = column_list.count(item)
        count_items.append(occurrences)
    return item_types, count_items

if answer == "s":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
