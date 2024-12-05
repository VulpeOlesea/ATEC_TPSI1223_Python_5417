# =====================================================================
# Tarefa: Lab #2
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
'''
Integração de Listas e Dicionários

Realize as seguintes operações:
1. Dicionário com listas: Construa um dicionário que contenha informações sobre um aluno, onde as
chaves sejam nome, idade, e notas, sendo notas uma lista com3 valores numéricos que representem
as suas notas
2. Lista de dicionários: Cria uma lista que contenha 3 dicionários, cada um representando um produto
numa loja online, com as seguintes chaves: nome, preço, e quantidade

Tarefas
• Aceder e imprimir a lista de notas do aluno
• Adicionar uma nova nota à lista de notas do aluno
• Aceder e imprimir o nome e o preço de cada produto da lista de dicionários
• Atualizar o preço do segundo produto na lista
• Remover o último produto da lista
'''

aluno = {"nome": "Maria", "idade": 18, "notas": [18, 19, 20]}

produtos = [
    {"nome": "Buquê de rosas", "preço": 45.00, "quantidade": 10},
    {"nome": "Buquê de tulipas", "preço": 20.00, "quantidade": 15},
    {"nome": "Buquê de peônias", "preço": 53.00, "quantidade": 8}
]

# Aceder e imprimir a lista de notas do aluno
print(aluno["notas"])

print("\n---------------------------------------------------")
# Adicionar uma nova nota à lista de notas do aluno
aluno["notas"].append(20)
print(aluno["notas"])

print("\n---------------------------------------------------")
# Aceder e imprimir o nome e o preço de cada produto da lista de dicionários
for produto in produtos:
    print(f"Nome: {produto["nome"]}, Preço: {produto["preço"]}")

print("\n---------------------------------------------------")
# Atualizar o preço do segundo produto na lista
produtos[1]["preço"] = 25.00
print(produtos[1])

print("\n---------------------------------------------------\n")

# Remover o último produto da lista
produtos.pop()

print(produtos)
