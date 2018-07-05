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
# Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
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
answer = "Escreva sua resposta aqui."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

#TODO Tarefa 9: Encontre o valor mínimo, máximo, média e mediana da duração de viagens

#TODO Tarefa 10: Mostre todas as estações da base de dados

#TODO Tarefa 11: Crie uma função que conte a ocorrência de qualquer coluna (opcional)
