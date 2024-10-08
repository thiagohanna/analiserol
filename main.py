import streamlit as st
import pandas as pd
import numpy as np

# Inicializar o histórico de números
if 'number_history' not in st.session_state:
    st.session_state.number_history = []

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
                    percentages.append((y, percentage))
                else:
                    percentages.append((y, 0))  # Células vazias para percentuais iguais a zero
            else:
                percentages.append((y, 0))  # Células vazias se não houver cálculos ativos

        # Ordenar as células de cada linha pela maior para menor porcentagem
        percentages.sort(key=lambda item: item[1], reverse=True)
        df_analysis.loc[x] = [f"<span style='font-size:14px; white-space: nowrap;'>{cell[0]}</span> <span style='font-size:14px; white-space: nowrap;'>( {cell[1]}% )</span>" if cell[1] > 0 else "" for cell in percentages]

    return df_analysis

# Configuração da página do Streamlit
st.set_page_config(layout="wide")  # Define o layout para tela larga
st.title("Análise de Números")
st.write("Insira um número para adicionar à sequência e analisar a frequência de números à esquerda.")

# Campo de entrada para adicionar um novo número
new_number = st.text_input("Digite um número:", "")

# Processar o novo número inserido
if new_number.isdigit() and 0 <= int(new_number) <= 36:
    st.session_state.number_history.append(int(new_number))
    st.success(f"Número {new_number} adicionado com sucesso!")
else:
    if new_number:  # Se houver entrada, mas não for válida
        st.error("Por favor, insira um número inteiro entre 0 e 36.")

# Analisar a lista completa de números inseridos
if st.session_state.number_history:
    df_analysis = analyze_numbers(st.session_state.number_history)
    
    # Exibir a tabela de análise resultante sem cabeçalhos de coluna e células sem valores de zero
    st.write("Tabela de Análise de Números")
    st.markdown(
        df_analysis.style.hide(axis='columns').to_html(), 
        unsafe_allow_html=True
    )

    # Mostrar o histórico de números já inseridos
    st.write("Histórico de Números Digitados:")
    st.write(st.session_state.number_history)
