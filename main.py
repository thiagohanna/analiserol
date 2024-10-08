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

    # Mantém todos os números na lista, incluindo repetições consecutivas
    for i in range(1, len(number_list)):
        y = number_list[i - 1]
        x = number_list[i]
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
st.write("Insira números separados por vírgula ou um número individual para adicionar à sequência.")

# Campo de entrada para adicionar números separados por vírgula ou individualmente
number_input = st.text_input("Digite números separados por vírgula ou um número individual:", "")

# Processar a entrada de números
if number_input:
    try:
        # Processar múltiplos números separados por vírgula
        new_numbers = [int(num.strip()) for num in number_input.split(",") if num.strip().isdigit()]
        if new_numbers:
            st.session_state.number_history = new_numbers + st.session_state.number_history
        else:
            st.error("Por favor, insira apenas números inteiros entre 0 e 36 separados por vírgula.")

        # Limpar o campo de entrada após adicionar os números
        st.experimental_rerun()
    except ValueError:
        st.error("Ocorreu um erro ao processar os números. Certifique-se de que estão no formato correto.")

# Analisar a lista completa de números inseridos
if st.session_state.number_history:
    df_analysis = analyze_numbers(st.session_state.number_history)
    
    # Exibir a tabela de análise resultante sem cabeçalhos de coluna e células sem valores de zero
    st.write("Tabela de Análise de Números")
    st.markdown(
        df_analysis.style.hide(axis='columns').to_html(), 
        unsafe_allow_html=True
    )

    # Mostrar o histórico de números já inseridos, com os últimos números à esquerda
    st.write("Histórico de Números Digitados (últimos à esquerda):")
    st.write(", ".join(map(str, st.session_state.number_history)))
