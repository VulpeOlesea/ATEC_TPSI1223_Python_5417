# =====================================================================
# Tarefa: Lab #8
# UFCD: 5417 - Programação para a WEB - Servidor (server-side)
# Turma: TPSI PL 1223
# Formador: Nelson Santos
# Formanda: Olesea Vulpe
# =====================================================================*/
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
file_path = "vendas.csv"
data = pd.read_csv(file_path)

print("------------------------------------------")
# Desafio 1: Agrupamento e Soma
print("Desafio 1: Agrupamento e Soma\n")
agrupamento = data.groupby("Produto").sum()
print(agrupamento)


print("------------------------------------------")
# Desafio 2: Criação de Nova Coluna com Cálculos
print("Desafio 2: Criação de Nova Coluna 'Lucro'\n")
data["Lucro"] = data["Total_Venda"] * 0.2
print(data)


print("------------------------------------------")
# Desafio 3: Exportação para Excel
print(f"Desafio 3: Exportação para Excel\n")
export = "resultados_vendas.xlsx"
with pd.ExcelWriter(export, engine="openpyxl") as writer:
    agrupamento.to_excel(writer, sheet_name="Agrupamento_Soma", index=False)
    data.to_excel(writer, sheet_name="Lucros_Calculados", index=False)
print(f"Arquivo exportado com sucesso! Mostrar {export}")


print("------------------------------------------")
# Desafio 4: Visualização de Dados
print(f"Desafio 4: Visualização de Dados\n")
grafico = data.groupby("Produto")["Total_Venda"].sum()
grafico.plot(kind="bar", title="Total de Vendas por Produto", xlabel="Produto", ylabel="Total de Vendas", color="violet")
plt.tight_layout()
plt.show()
print(f"O gráfico foi criado com sucesso!")


print("------------------------------------------")
# Desafio 5: Ordenação de Dados
print(f"Desafio 5: Ordenação de Dados (por Total_Venda)\n")
data_sort = data.sort_values(by="Total_Venda", ascending=False)
print(data_sort)


print("------------------------------------------")
# Desafio 6: Remoção de Duplicados
print("Desafio 6: Remoção de Duplicados\n")
data_unique = data.drop_duplicates()
print(data_unique)


print("------------------------------------------")
# Desafio 7: Aplicação de Função Personalizada
print("Desafio 7: Aplicação de Função Personalizada")
def aplicar_desconto(total_venda):
    return total_venda * 0.9

data["Preco_Ajustado"] = data["Total_Venda"].apply(aplicar_desconto)
print("Nova Coluna com Preços Ajustados:\n")
print(data)


print("------------------------------------------")
# Desafio 8: Análise de Séries Temporais
print(f"Desafio 8: Análise de Séries Temporais")
serie_temporal = data.groupby("Data")["Total_Venda"].sum()
print("Total de Vendas por Data):\n", serie_temporal)

grafico = serie_temporal.plot(title="Tendência das Vendas ao Longo do Tempo", xlabel="Data", ylabel="Total de Vendas", marker="o", color="violet")
plt.tight_layout()
print(f"\nO gráfico foi criado com sucesso!")
plt.show()

# Perguntas
# Qual é a tendência geral das vendas ao longo do tempo?
'''
As vendas permanecem estáveis ao longo do tempo, sem um aumento ou queda consistente.
'''
# Existem padrões sazonais ou flutuações nos dados?
'''
Há flutuações frequentes, com picos e quedas abruptas, possivelmente influenciadas por fatores sazonais ou eventos específicos.
'''