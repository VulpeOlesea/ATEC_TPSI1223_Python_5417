# =====================================================================
# Tarefa: Lab #5
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
'''
Exercício 1: Adivinha o Número (Guess the Number)
'''

import random

random_num = random.randint(1, 100)
tentativas = 0

print("Tente adivinhar o número entre 1 e 100.")

while True:

    user_input = input("Digite o número: ")

    if not user_input.isdigit():
        print("Por favor, insira um número válido")
        continue

    tentativa = int(user_input)
    tentativas += 1

    if tentativa < random_num:
        print("Muito baixo!")
    elif tentativa > random_num:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou o número {random_num} em {tentativas} tentativas.")
        break


# Perguntas
# • De que forma a função random.randint() gera números aleatórios?
'''
A função random.randint(a, b) gera um número pseudoaleatório entre os valores a e b, inclusive.
Pseudoaleatório significa que os números gerados parecem ser aleatórios, mas na realidade são calculados por um algoritmo determinístico.
'''
# • O que aconteceria se o utilizador introduzisse um valor inválido (não numérico)? Como poderia tratar essa situação?
'''
Se o utilizador introduzir um valor inválido, como uma string ("abc") ou outro tipo de dado que não pode ser convertido para inteiro, 
haverá um erro "Por favor, insira um número válido", para realizar isso usei o método .isdigit(). 
Ele retorna True se todos os caracteres da string forem dígitos e a string não estiver vazia. Caso contrário, retorna False.
'''

'''
-------------------------------------------------------
Exercício 2: Calculadora de juros (Interest Calculator)
-------------------------------------------------------
'''
def juros_simples(capital, taxa, anos):
    return capital * (1 + taxa * anos)

def juros_compostos(capital, taxa, anos):
    return capital * (1 + taxa) ** anos

capital = float(input("Digite o montante inicial (capital): "))
taxa = float(input("Digite a taxa de juro anual (em %): ")) / 100
anos = int(input("Digite o número de anos: "))

valor_juros_simples = juros_simples(capital, taxa, anos)
valor_juros_compostos = juros_compostos(capital, taxa, anos)

print("\n-----------------------------------------")
print(f"Valor final com juros simples: {valor_juros_simples:.2f}")
print(f"Valor final com juros compostos: {valor_juros_compostos:.2f}")

# Perguntas
# • Qual é a fórmula para o cálculo de juros simples? E para juros compostos?
'''
Fórmula para o cálculo de juros simples:
capital * (1 + taxa * anos) 

Fórmula para o cálculo de juros compostos:
capital * (1 + taxa) ** anos

(e depois dividir taxa por 100 para saber em %)
'''
# • Qual seria a melhor opção de investimento dependendo da taxa de juro e do número de anos?
'''
Para um prazo longo e taxas de juro altas, juros compostos serão significativamente mais vantajosos.
'''

'''
-------------------------------------------------------
Exercício 3: Leis por idade (Laws by Age)
-------------------------------------------------------
'''

idade = int(input("Insira a sua idade: "))

if idade >= 16 and idade < 18:
    print("Você pode votar, mas não pode conduzir nem beber álcool.")
elif idade >= 18:
    print("Você pode conduzir, votar e beber álcool")
else:
    print("Você ainda é muito jovem para conduzir, votar ou beber álcool.")

# Perguntas
# • Que estrutura condicional seria mais eficiente para implementar este exercício: múltiplos if-else ou outra abordagem?
'''
Estrutura condicional: if-elif-else
'''
# • Que regras podem variar de país para país? Como poderia adaptar o programa para suportar diferentes legislações?
'''
Para adaptar o programa a diferentes países, pode adicionar mais algumas condições elif
'''

'''
-------------------------------------------------------
Exercício 4: Treinador de matemática (Math Trainer)
-------------------------------------------------------
'''
import random

print("\nResolva as operações geradas. Digite 'sair' para encerrar.\n")
respostas = 0
respostas_total = 0

while True:
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operacao = random.choice(['+', '-', '*', '/'])

    if operacao == '/' and num1 % num2 != 0:
        continue

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        resultado = num1 // num2

    resposta = input(f"Qual é o resultado de: {num1} {operacao} {num2} = ")

    # Se o utilizador quer sair
    if resposta.lower() == 'sair':
        break

    if resposta.isdigit() or (resposta.startswith('-')):
        if int(resposta) == resultado:
            print("Correto!")
            respostas += 1
        else:
            print(f"Incorreto. A resposta certa é {resultado}.")
        respostas_total += 1
    else:
        print("Insira um número válido ou palavra 'sair'.\n")

# Se o utilizador decidir sair do jogo
print("\nResultado: ")
print(f"Você respondeu corretamente a {respostas} de {respostas_total} operações.")

# Perguntas
# • Como pode garantir que as operações geradas são equilibradas, ou seja, que não são demasiado fáceis ou difíceis?
'''
Para evitar operações muito fáceis ou muito difíceis usei os números entre 1 e 10.
'''

# • Como pode o programa fornecer feedback ao utilizador sobre o seu progresso ou desempenho?
'''
Depois cada resposta, o programa diz se a resposta está correta ou não.
E ao final mostra número total de respostas corretas.
'''

'''
-------------------------------------------------------
Exercício 5: Sistema de Login (Login System)
-------------------------------------------------------
'''

login = {
    "anna": "123",
    "maria": "456",
    "mario": "789"
}

utilizador = input("Digite seu nome de utilizador: ")
senha = input("Digite sua palavra-passe: ")

if utilizador in login and login[utilizador] == senha:
    print(f"Bem-vindo, {utilizador}!")
else:
    print("Erro: Nome de utilizador ou palavra-passe incorretos.")

# Perguntas
# • Como poderia melhorar este sistema de login para suportar funcionalidades como a recuperação de senha ou múltiplas tentativas?
'''
Pode ser implementado através de perguntas de segurança ou envio de código por email.
'''

'''
-------------------------------------------------------
Exercício 6: Verificador de Ano Bissexto (Leap Year)
-------------------------------------------------------
'''
ano = int(input("Digite um ano: "))

if not (ano % 4 and ano % 100) or not ano % 400:
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")

# Perguntas
# • Porque é que existem anos bissextos? Qual a importância dessa correção no calendário?
'''
O ano bissexto existe para ajustar o calendário ao ciclo solar
'''