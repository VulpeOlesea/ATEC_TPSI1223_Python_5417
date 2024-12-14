# =====================================================================
# Tarefa: Lab #6
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
'''
Exercício 1: Verificação de Número de Cartão de Crédito
'''
def verificar_cartao(numero_cartao):

    if not numero_cartao.isdigit():
        return False

    digitos = list(map(int, numero_cartao))

    if all(d == 0 for d in digitos):
        return False

    digitos = digitos[::-1]

    # O algoritmo de Luhn
    soma = 0
    for i, digito in enumerate(digitos):
        if i % 2 == 1:
            digito *= 2
            if digito > 9:
                digito -= 9
        soma += digito
    return soma % 10 == 0

# Exemplos de Input e Output
print(verificar_cartao("4532015112830366"))
print(verificar_cartao("1234567812345678"))
print(verificar_cartao("4111111111111111"))
print(verificar_cartao("0000000000000000"))
print("---------------------------------------------------------")

'''
-------------------------------------------------------
Exercício 2: Conversão de Temperaturas
-------------------------------------------------------
'''
def converter_temperatura(valor, unidade):

    try:
        temperatura = float(valor)
    except ValueError:
        return "Erro (input inválido). Insira um número."

    # Celsius para Fahrenheit
    if unidade.lower() == "c":
        converter = (temperatura * 9/5) + 32
        return f"{temperatura}°C = {converter:.2f}°F"
    # Fahrenheit para Celsius
    elif unidade.lower() == "f":
        converter = (temperatura - 32) * 5/9
        return f"{temperatura}°F = {converter:.2f}°C"
    else:
        return "Erro (unidade inválida). Use 'C' para Celsius ou 'F' para Fahrenheit."

# Exemplos de Input e Output
print(converter_temperatura(0, "C"))
print(converter_temperatura(100, "C"))
print(converter_temperatura(32, "F"))
print(converter_temperatura(-40, "C"))
print(converter_temperatura("cinquenta", "C"))
print("---------------------------------------------------------")

'''
---------------------------------------------------------------------
Exercício 3: Verificação do Dígito de Controlo de um Código de Barras
---------------------------------------------------------------------
'''
def verificar_cod_barras(codigo):

    if not codigo.isdigit():
        return "Erro (Código inválido). Deve conter apenas números."

    if len(codigo) < 2:
        return "Erro (Código inválido). Deve ter pelo menos dois dígitos."

    digitos = list(map(int, codigo))
    digito_real = digitos.pop()

    soma = 0
    for i, digito in enumerate(reversed(digitos)):
        soma += digito * (3 if i % 2 == 0 else 1)

    digito_calculado = (10 - (soma % 10)) % 10

    return digito_real == digito_calculado

# Exemplos de Input e Output
print(verificar_cod_barras("12345670"))
print(verificar_cod_barras("12345678"))
print(verificar_cod_barras("00000000"))
print("---------------------------------------------------------")

'''
---------------------------------------------------------------------
Exercício 4: Cálculo do IMC (Índice de Massa Corporal)
---------------------------------------------------------------------
'''
def calcular_imc(peso, altura):

    if peso <= 0:
        return "Erro (Peso inválido). Deve ser maior que zero."
    if altura <= 0:
        return "Erro (Altura inválida). Deve ser maior que zero."

    imc = peso / (altura ** 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif 18.5 <= imc <= 24.9:
        classificacao = "Peso normal"
    elif 25 <= imc <= 29.9:
        classificacao = "Excesso de peso"
    elif 30 <= imc <= 34.9:
        classificacao = "Obesidade grau 1"
    elif 35 <= imc <= 39.9:
        classificacao = "Obesidade grau 2"
    else:
        classificacao = "Obesidade grau 3"

    return f"IMC = {imc:.2f}, Classificação: {classificacao}"

# Exemplos de Input e Output
print(calcular_imc(70, 1.75))
print(calcular_imc(50, 1.60))
print(calcular_imc(90, 1.60))
print(calcular_imc(-70, 1.75))
print(calcular_imc(70, 0))
print("---------------------------------------------------------")

'''
---------------------------------------------------------------------
Exercício 5: Conversor de Unidades de Medida
---------------------------------------------------------------------
'''
def converter_distancia(valor, unidade):
    try:
        distancia = float(valor)
    except ValueError:
        return "Erro (Input inválido). Insira um número."

    if distancia < 0:
        return "Erro: Distância não pode ser negativa."

    # Km para milhas
    if unidade.lower() == "km":
        convertido = distancia * 0.621371
        return f"{distancia} km = {convertido:.2f} milhas."
    # Milhas para km
    elif unidade.lower() == "milhas":
        convertido = distancia / 0.621371
        return f"{distancia} milhas = {convertido:.2f} km."
    else:
        return "Erro: Unidade inválida. Use 'km' ou 'milhas'."

# Exemplos de Input e Output
print(converter_distancia(10, "km"))
print(converter_distancia(5, "milhas"))
print(converter_distancia(-10, "km"))
print(converter_distancia("dez", "km"))
print("---------------------------------------------------------")
