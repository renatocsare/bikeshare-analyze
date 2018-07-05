# coding: utf-8

import csv
import matplotlib.pyplot as plt

print("""
------__o
-----_\ <,_
----(_)/ (_)

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
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    male = data_list.count('Male')
    female = data_list.count('Female')
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------


#TODO Tarefa 6: Mostre o gênero mais popular

#TODO Tarefa 7: Mostre um gráfico usando os dados anteriores

#TODO Tarefa 8: Responda o motivo do número de homens e mulheres não bater com a quantidade de amostras

#TODO Tarefa 9: Encontre o valor mínimo, máximo, média e mediana da duração de viagens

#TODO Tarefa 10: Mostre todas as estações da base de dados

#TODO Tarefa 11: Crie uma função que conte a ocorrência de qualquer coluna (opcional)
