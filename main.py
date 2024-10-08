import streamlit as st
import pandas as pd
import numpy as np

# Função para analisar a lista e preencher a tabela com percentuais
def analyze_numbers(number_list):
    counts = {i: {j: 0 for j in range(37)} for i in range(37)}
    total_counts = {i: 0 for i in range(37)}
    
    # Remover números consecutivos repetidos para considerar apenas uma ocorrência
    filtered_list = [number_list[i] for i in range(len(number_list)) if i == 0 or number_list[i] != number_list[i - 1]]
    
    # Percorrer a lista filtrada para contar as ocorrências de pares (y, x)
    for i in range(1, len(filtered_list)):
        y = filtered_list[i - 1]
        x = filtered_list[i]
        if 0 <= y <= 36 and 0 <= x <= 36:  # Verifica se os números estão no intervalo desejado
            counts[x][y] += 1
            total_counts[x] += 1
    
    # Criar uma tabela de análise com os percentuais calculados
    column_names = [f"{i+1}º" for i in range(37)]
    df_analysis = pd.DataFrame(index=range(37), columns=column_names)
    for x in range(37):
        percentages = []
        for y in range(37):
            if total_counts[x] > 0:
                percentage = int((counts[x][y] / total_counts[x]) * 100)  # Remove casas decimais
                if percentage > 0:  # Apenas mostrar células com valores diferentes de zero
                    percentages.append((y, f"<span style='font-size:14px;'>{y}</span> <span style='font-size:14px;'>( {percentage}% )</span>"))
                else:
                    percentages.append((y, ""))  # Células vazias para percentuais iguais a zero
            else:
                percentages.append((y, ""))  # Células vazias se não houver cálculos ativos
        # Ordenar as células de cada linha pela maior para menor porcentagem
        percentages.sort(key=lambda item: int(item[1].split('(')[-1][:-2]) if item[1] else 0, reverse=True)
        df_analysis.loc[x] = [cell[1] for cell in percentages]
    
    return df_analysis

# Configuração da página do Streamlit
st.set_page_config(layout="wide")  # Define o layout para tela larga
st.title("Análise de Números")
st.write("Insira uma lista de números separados por vírgula para analisar a frequência de números à esquerda.")

# Campo de entrada para o usuário fornecer a lista de números
number_input = st.text_input("Digite os números separados por vírgula:", "32, 13, 26, 20, 18, 10")

# Limpar e converter a entrada do usuário para uma lista de inteiros
try:
    # Remover espaços em excesso e converter para inteiros
    number_list = [int(num.strip()) for num in number_input.split(",") if num.strip().isdigit()]
    if not number_list:
        st.error("Por favor, insira apenas números inteiros separados por vírgula.")
    else:
        df_analysis = analyze_numbers(number_list)
        # Exibir a tabela de análise resultante sem cabeçalhos de coluna e células sem valores de zero
        st.write("Tabela de Análise de Números")
        st.markdown(
            df_analysis.style.hide(axis='columns').to_html(), 
            unsafe_allow_html=True
        )
except ValueError:
    st.error("Por favor, insira apenas números inteiros separados por vírgula.")
