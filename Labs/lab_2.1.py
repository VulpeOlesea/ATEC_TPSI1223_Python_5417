# =====================================================================
# Tarefa: Lab #2
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
'''
Criação e Modificação de Dicionários

Construa dicionários para representar os seguintes objetos:
1. Data: Um dicionário que representa uma data, por exemplo, 23 de Outubro de 1971, com as chaves
dia, mês, e ano
2. Evento no Calendário: Um dicionário que guarda informações sobre um evento, com as seguintes
chaves: título, data, hora e descrição
3. Pessoa: Um dicionário que contém informações sobre uma pessoa, como nome, idade e cidade
4. Produto numa Loja Online: Um dicionário que representa um produto com as chaves nome do
produto, preço, quantidade disponível, e categoria

Tarefas
• Aceder e imprime valores individuais dos dicionários
• Modificar um dos valores dentro de cada dicionário
• Adicionar uma nova chave-valor ao dicionário
• Remover uma chave de um dos dicionários
'''

data = {"dia": 23, "mês": "Outubro", "ano": 1971}
evento = {"título": "Aniversário", "data": "23/10/1971", "hora": "22:00", "descrição": "Festa de aniversário"}
pessoa = {"nome": "Ana Maria", "idade": 25, "cidade": "Porto"}
produto = {"nome do produto": "Buquê de rosas", "preço": 45.00, "quantidade disponível": 10, "categoria": "Flores"}

# Aceder e imprime valores individuais dos dicionários
print(data["mês"])
print(evento["título"])
print(pessoa["cidade"])
print(produto["nome do produto"])

print("\n---------------------------------------------------")
# Modificar um dos valores dentro de cada dicionário
data["ano"] = 1990
evento["hora"] = "20:00"
pessoa["idade"] = 26
produto["quantidade disponível"] = 20

print(data)
print(evento)
print(pessoa)
print(produto)

print("\n---------------------------------------------------")
# Adicionar uma nova chave-valor ao dicionário
data["hora"] = "08:08"
evento["localização"] = "All In Porto"
pessoa["altura"] = 165
produto["loja"] = "Florista Tina"

print(data)
print(evento)
print(pessoa)
print(produto)

print("\n---------------------------------------------------\n")
# Remover uma chave de um dos dicionários
pessoa.pop("altura")
print(pessoa)
