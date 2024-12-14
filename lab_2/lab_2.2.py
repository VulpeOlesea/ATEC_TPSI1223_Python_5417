# =====================================================================
# Tarefa: Lab #2
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
'''
Criação e Modificação de Listas

Construir e manipular as seguintes listas:
1. Lista de números: Uma lista com 10 números inteiros
2. Lista de nomes: Uma lista com 5 nomes de pessoas
3. Lista de tarefas: Uma lista de 5 tarefas diárias que precisas de realizar

Tarefas
• Aceder e imprimir o primeiro e o último elemento de cada lista
• Adicionar um novo elemento ao final de cada lista
• Remover o segundo elemento de cada lista
• Ordenar a lista de números em ordem crescente
• Iterar sobre a lista de nomes e imprime uma mensagem de saudação para cada nome
'''

numeros = [1, 32, 3, 24, 5, 61, 7, 88, 9, 10]
nomes = ["Maria", "Ana", "Paulo", "Mario", "Luisa"]
tarefas = ["Descansar", "Cozinhar", "Estudar", "Treinar", "Ler"]

# Aceder e imprimir o primeiro e o último elemento de cada lista
print(numeros[0],",", numeros[-1])
print(nomes[0],",", nomes[-1])
print(tarefas[0],",", tarefas[-1])

print("\n---------------------------------------------------")
# Adicionar um novo elemento ao final de cada lista
numeros.append(14)
nomes.append("Lora")
tarefas.append("Trabalhar")

print(numeros)
print(nomes)
print(tarefas)

print("\n---------------------------------------------------")
# Remover o segundo elemento de cada lista
numeros.pop(1)
nomes.pop(1)
tarefas.pop(1)

print(numeros)
print(nomes)
print(tarefas)

print("\n---------------------------------------------------")
# Ordenar a lista de números em ordem crescente
numeros.sort()

print(numeros)

print("\n---------------------------------------------------\n")
# Iterar sobre a lista de nomes e imprime uma mensagem de saudação para cada nome
for nome in nomes:
    print(f"Olá, {nome}!")
