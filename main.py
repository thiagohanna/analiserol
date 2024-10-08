import streamlit as st
import pandas as pd
import numpy as np

# Função para analisar a lista e preencher a tabela com percentuais
def analyze_numbers(number_list):
    counts = {i: {j: 0 for j in range(37)} for i in range(37)}
    total_counts = {i: 0 for i in range(37)}
    
    # Percorrer a lista para contar as ocorrências de pares (y, x)
    for i in range(1, len(number_list)):
        y = number_list[i - 1]
        x = number_list[i]
        if 0 <= y <= 36 and 0 <= x <= 36:  # Verifica se os números estão no intervalo desejado
            counts[x][y] += 1
            total_counts[x] += 1
    
    # Criar uma tabela de análise com os percentuais calculados
    df_analysis = pd.DataFrame(np.zeros((37, 37)), columns=range(37), index=range(37))
    for x in range(37):
        for y in range(37):
            if total_counts[x] > 0:
                df_analysis.at[x, y] = (counts[x][y] / total_counts[x]) * 100
            else:
                df_analysis.at[x, y] = 0
    return df_analysis

# Configuração da página do Streamlit
st.title("Análise de Números da Roleta")
st.write("Insira uma lista de números separados por vírgula para analisar a frequência de números à esquerda.")

# Campo de entrada para o usuário fornecer a lista de números
number_input = st.text_input("Digite os números separados por vírgula:", "32, 13, 26, 20, 18, 10")

# Converter a entrada do usuário para uma lista de inteiros
try:
    number_list = [int(num.strip()) for num in number_input.split(",")]
    df_analysis = analyze_numbers(number_list)
    
    # Exibir a tabela de análise resultante
    st.write("Tabela de Análise de Números da Roleta")
    st.dataframe(df_analysis)
except ValueError:
    st.error("Por favor, insira apenas números inteiros separados por vírgula.")
