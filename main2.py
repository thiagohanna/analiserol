import pandas as pd
import streamlit as st

# Configura a largura da página
st.set_page_config(layout="wide")

# Base de dados atualizada
data = {
    'Número': list(range(37)),
    'Terminal': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6'],
    'Dúzia': ['ZERO', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D1', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D2', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3', 'D3'],
    'Coluna': ['ZERO', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3', 'C1', 'C2', 'C3'],
    'Par/Ímpar': ['ZERO', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par', 'Ímpar', 'Par'],
    'Tipo': ['ZERO', 'Separado', 'Separado', 'Separado', 'Separado', 'Separado', 'Separado', 'Separado', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Separado', 'Separado', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Separado', 'Separado', 'Separado', 'Separado', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Junto', 'Separado', 'Separado', 'Separado', 'Separado', 'Separado'],
    'Seção': ['ZERO', 'Orphelins', 'Voisin', 'Voisin', 'Voisin', 'Tier', 'Orphelins', 'Voisin', 'Tier', 'Orphelins', 'Tier', 'Tier', 'Voisin', 'Tier', 'Orphelins', 'Voisin', 'Tier', 'Orphelins', 'Voisin', 'Voisin', 'Orphelins', 'Voisin', 'Voisin', 'Tier', 'Tier', 'Voisin', 'Tier', 'Voisin', 'Voisin', 'Tier', 'Orphelins', 'Tier', 'Voisin', 'Orphelins', 'Tier', 'Voisin', 'Tier'],
    'Cor': ['Zero', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Preto', 'Vermelho', 'Preto', 'Vermelho', 'Preto', 'Vermelho']
}

df = pd.DataFrame(data)

# Definindo os links de imagem associados a cada número
image_links = {
    0: 'https://iili.io/dQoa96v.png',
    1: 'https://iili.io/dQoYyMJ.png',
    2: 'https://iili.io/dQoYpna.png',
    3: 'https://iili.io/dQoYbZg.png',
    4: 'https://iili.io/dQoYDwF.png',
    5: 'https://iili.io/dQoYtu1.png',
    6: 'https://iili.io/dQoYQyP.png',
    7: 'https://iili.io/dQoYL8B.png',
    8: 'https://iili.io/dQoYsaV.png',
    9: 'https://iili.io/dQoYi3Q.png',
    10: 'https://iili.io/dQoY66x.png',
    11: 'https://iili.io/dQoY4Gj.png',
    12: 'https://iili.io/dQoYrCb.png',
    13: 'https://iili.io/dQoYUZu.png',
    14: 'https://iili.io/dQoYSje.png',
    15: 'https://iili.io/dQoY8u9.png',
    16: 'https://iili.io/dQoYky7.png',
    17: 'https://iili.io/dQoYevS.png',
    18: 'https://iili.io/dQoYOa2.png',
    19: 'https://iili.io/dQoYN3l.png',
    20: 'https://iili.io/dQoYj44.png',
    21: 'https://iili.io/dQoYhGf.png',
    22: 'https://iili.io/dQoYXCG.png',
    23: 'https://iili.io/dQoYVQs.png',
    24: 'https://iili.io/dQoYMjn.png',
    25: 'https://iili.io/dQoYGTX.png',  
    26: 'https://iili.io/dQoY1pt.png',
    27: 'https://iili.io/dQoY0vI.png',
    28: 'https://iili.io/dQoYlYN.png',
    29: 'https://iili.io/dQoYY4R.png',
    30: 'https://iili.io/dQoY7Ev.png',
    31: 'https://iili.io/dQoY5CJ.png',
    32: 'https://iili.io/dQoYAQa.png',
    33: 'https://iili.io/dQoYzp1.png',
    34: 'https://iili.io/dQoYxkP.png',
    35: 'https://iili.io/dQoYTTF.png',
    36: 'https://iili.io/dQoYuhg.png'
}

# Dicionário de cores e fontes para cada atributo
cores = {
    'Par/Ímpar': {
        'Zero': ('#6fa752', 'white'),
        'Par': ('#96cf55', 'black'),
        'Ímpar': ('#e49b9a', 'black')
    },
    'Dúzia': {
        'Zero': ('#6fa752', 'white'),
        'D1': ('#a265d0', 'white'),
        'D2': ('#4099f8', 'white'),
        'D3': ('#fada6c', 'white')
    },
    'Coluna': {
        'Zero': ('#6fa752', 'white'),
        'C1': ('#a265d0', 'black'),
        'C2': ('#4099f8', 'black'),
        'C3': ('#fada6c', 'black')
    },
    'Seção': {
        'Zero': ('#6fa752', 'white'),
        'Voisin': ('#3e7521', 'white'),
        'Orphelins': ('#74410d', 'white'),
        'Tier': ('#245292', 'white')
    },
    'Tipo': {
        'Zero': ('#6fa752', 'white'),
        'Separado': ('#d2d124', 'black'),
        'Junto': ('#5bbbc5', 'black')
    },
    'Terminal': {
        '0': ('#6fa752', 'black'),
        '1': ('#ff8c00', 'white'),
        '2': ('#4099f8', 'white'),
        '3': ('#fada6c', 'black'),
        '4': ('#abb7b8', 'black'),
        '5': ('#000000', 'white'),
        '6': ('#4b0081', 'white'),
        '7': ('#daa1dc', 'white'),
        '8': ('#86471a', 'white'),
        '9': ('#e14c3c', 'white')
    },
    'Cor': {
        'Zero': ('#6fa752', 'white'),
        'Vermelho': ('#ff0000', 'white'),
        'Preto': ('#000000', 'white')
    }
}

# Função para tratar a lista master e validar números
def tratar_lista_master(texto):
    texto = texto.replace('\n', ' ').replace('\r', ' ')  # Remove quebras de linha
    lista = texto.replace(',', ' ').split()  # Aceita vírgulas e espaços como separadores
    lista = [int(n) for n in lista if n.isdigit() and 0 <= int(n) <= 36]  # Filtra apenas números válidos (0-36)
    return lista  # Mantém os números duplicados

# Função para formatar a lista master
def formatar_lista_master(lista_master, circulados={}):
    formatted_numbers = []
    for numero in lista_master:
        row = df[df['Número'] == numero].iloc[0]
        bg_color, text_color = cores['Par/Ímpar']['Zero'] if numero == 0 else cores['Cor'][row['Cor']]
        
        if numero in circulados:
            for attr, color in circulados[numero].items():
                bg_color, text_color = color
        
        formatted_numbers.append(f"<td style='color:{text_color}; background-color:{bg_color}; text-align:center; padding:5px;'>{numero}</td>")

    linhas = ['<tr>' + ''.join(formatted_numbers[i:i+10]) + '</tr>' for i in range(0, len(formatted_numbers), 10)]
    return '<table style="width:100%; table-layout:fixed;">' + ''.join(linhas) + '</table>'

# Função para análise de números
def analisar_roleta(lista_master):
    df_filtrado = df[df['Número'].isin(lista_master)]
    resultado = {}

    # Totais por cada atributo
    total_cor = len(lista_master)
    total_paridade = len(lista_master)
    total_duzia = len(lista_master)
    total_coluna = len(lista_master)
    total_secao = len(lista_master)
    total_tipo = len(lista_master)
    total_terminal = len(lista_master)

    # Cor
    resultado['Cor Vermelho'] = sum([1 for n in lista_master if df[df['Número'] == n]['Cor'].values[0] == 'Vermelho'])
    resultado['Cor Preto'] = sum([1 for n in lista_master if df[df['Número'] == n]['Cor'].values[0] == 'Preto'])

    # Par/Ímpar
    resultado['Par'] = sum([1 for n in lista_master if df[df['Número'] == n]['Par/Ímpar'].values[0] == 'Par'])
    resultado['Ímpar'] = sum([1 for n in lista_master if df[df['Número'] == n]['Par/Ímpar'].values[0] == 'Ímpar'])

    # Dúzias
    resultado['D1'] = sum([1 for n in lista_master if df[df['Número'] == n]['Dúzia'].values[0] == 'D1'])
    resultado['D2'] = sum([1 for n in lista_master if df[df['Número'] == n]['Dúzia'].values[0] == 'D2'])
    resultado['D3'] = sum([1 for n in lista_master if df[df['Número'] == n]['Dúzia'].values[0] == 'D3'])
    resultado['Zero'] = sum([1 for n in lista_master if df[df['Número'] == n]['Dúzia'].values[0] == 'ZERO'])

    # Colunas
    resultado['C1'] = sum([1 for n in lista_master if df[df['Número'] == n]['Coluna'].values[0] == 'C1'])
    resultado['C2'] = sum([1 for n in lista_master if df[df['Número'] == n]['Coluna'].values[0] == 'C2'])
    resultado['C3'] = sum([1 for n in lista_master if df[df['Número'] == n]['Coluna'].values[0] == 'C3'])
    resultado['Coluna Zero'] = sum([1 for n in lista_master if df[df['Número'] == n]['Coluna'].values[0] == 'ZERO'])

    # Seção
    resultado['Seção Zero'] = sum([1 for n in lista_master if df[df['Número'] == n]['Seção'].values[0] == 'ZERO'])
    resultado['Seção Voisin'] = sum([1 for n in lista_master if df[df['Número'] == n]['Seção'].values[0] == 'Voisin'])
    resultado['Seção Orphelins'] = sum([1 for n in lista_master if df[df['Número'] == n]['Seção'].values[0] == 'Orphelins'])
    resultado['Seção Tier'] = sum([1 for n in lista_master if df[df['Número'] == n]['Seção'].values[0] == 'Tier'])

    # Tipo
    resultado['Tipo Zero'] = sum([1 for n in lista_master if df[df['Número'] == n]['Tipo'].values[0] == 'ZERO'])
    resultado['Separado'] = sum([1 for n in lista_master if df[df['Número'] == n]['Tipo'].values[0] == 'Separado'])
    resultado['Junto'] = sum([1 for n in lista_master if df[df['Número'] == n]['Tipo'].values[0] == 'Junto'])

    # Terminais
    for i in range(10):
        resultado[f'Term {i}'] = sum([1 for n in lista_master if df[df['Número'] == n]['Terminal'].values[0] == str(i)])

    # Totais separados por categoria
    totais = {
        'Dúzia': total_duzia,
        'Coluna': total_coluna,
        'Paridade': total_paridade,
        'Seção': total_secao,
        'Tipo': total_tipo,
        'Terminal': total_terminal
    }

    return resultado, totais

# Função para exibir imagens
def exibir_imagens(lista_master):
    cols = st.columns(min(10, len(lista_master)))
    for i in range(min(10, len(lista_master))):
        num = lista_master[i]
        # Verifica se o número tem uma imagem associada
        if num in image_links:
            cols[i].image(image_links[num], width=150)
        else:
            cols[i].write(f"Imagem não disponível para {num}")

# Função para circular números por atributo
def circular_atributo(coluna, grupo, cores):
    st.session_state['circulados'] = {}
    df_atributo = df[df[coluna].isin(grupo)]
    for _, row in df_atributo.iterrows():
        if row['Número'] not in st.session_state['circulados']:
            st.session_state['circulados'][row['Número']] = {}
        st.session_state['circulados'][row['Número']][coluna] = cores[row[coluna]]

# Função para aplicar filtro do botão de terminal
def aplicar_terminal(escuros, claros):
    st.session_state['circulados'] = {}
    for numero in escuros:
        st.session_state['circulados'][numero] = {'Terminal': ('#00008B', 'white')}  # Azul escuro e letra branca
    for numero in claros:
        st.session_state['circulados'][numero] = {'Terminal': ('#ADD8E6', 'black')}  # Azul claro e letra preta
    for numero in range(37):
        if numero not in escuros and numero not in claros:
            st.session_state['circulados'][numero] = {'Outros': ('#ffffff', 'black')}  # Fundo branco e letra preta

# Função para aplicar filtro do botão "Espelho +1v"
def aplicar_espelho():
    st.session_state['circulados'] = {}
    numeros_verde_escuro = [12, 21, 32, 23, 13, 31]
    numeros_verde_claro = [0, 2, 4, 8, 9, 10, 14, 15, 26, 28, 35, 36]
    for numero in numeros_verde_escuro:
        st.session_state['circulados'][numero] = {'Espelho +1v': ('#006400', 'white')}  # Verde escuro e letra branca
    for numero in numeros_verde_claro:
        st.session_state['circulados'][numero] = {'Espelho +1v': ('#90EE90', 'black')}  # Verde claro e letra preta
    for numero in range(37):
        if numero not in numeros_verde_escuro and numero not in numeros_verde_claro:
            st.session_state['circulados'][numero] = {'Outros': ('#ffffff', 'black')}  # Fundo branco e letra preta

# Função para aplicar filtro do botão "11-22-33 +1v"
def aplicar_112233():
    st.session_state['circulados'] = {}
    numeros_verde_escuro = [11, 22, 33, 0]
    numeros_verde_claro = [26, 32, 36, 30, 9, 18, 1, 16]
    for numero in numeros_verde_escuro:
        st.session_state['circulados'][numero] = {'11-22-33 +1v': ('#006400', 'white')}  # Verde escuro e letra branca
    for numero in numeros_verde_claro:
        st.session_state['circulados'][numero] = {'11-22-33 +1v': ('#90EE90', 'black')}  # Verde claro e letra preta
    for numero in range(37):
        if numero not in numeros_verde_escuro and numero not in numeros_verde_claro:
            st.session_state['circulados'][numero] = {'Outros': ('#ffffff', 'black')}  # Fundo branco e letra preta

# Função para aplicar filtro Term Alto e Term Baixo
def aplicar_filtro_term(alto=True):
    st.session_state['circulados'] = {}
    if alto:
        numeros_escuros = [6,16,26,36,7,17,27,8,18,28,9,19,29]
        st.session_state['legenda'] = "Numeros: 6,16,26,36,7,17,27,8,18,28,9,19,29"
    else:
        numeros_escuros = [0,10,20,30,1,11,21,31,2,12,22,32,3,13,23,33,4,14,24,34,5,25,35]
        st.session_state['legenda'] = "Numeros: 0,10,20,30,1,11,21,31,2,12,22,32,3,13,23,33,4,14,24,34,5,25,35"
    for numero in numeros_escuros:
        st.session_state['circulados'][numero] = {'Terminal': ('#00008B', 'white')}  # Azul escuro e letra branca
    for numero in range(37):
        if numero not in numeros_escuros:
            st.session_state['circulados'][numero] = {'Outros': ('#ffffff', 'black')}  # Fundo branco e letra preta

# Inicializa variáveis no session_state
if 'lista_master' not in st.session_state:
    st.session_state['lista_master'] = []

if 'circulados' not in st.session_state:
    st.session_state['circulados'] = {}

# Adiciona persistência para os resultados da análise
if 'resultado' not in st.session_state:
    st.session_state['resultado'] = None
    st.session_state['totais'] = None

# Função para adicionar números ao pressionar "Enter"
def adicionar_numeros(novo_numero_input):
    try:
        novos_numeros = tratar_lista_master(novo_numero_input)
        lista_master = st.session_state['lista_master']
        lista_master = novos_numeros + lista_master  # Adiciona os novos números no início da lista master
        st.session_state['lista_master'] = lista_master  # Atualiza a lista master
        st.session_state['novo_numero'] = ""  # Limpa o campo de entrada
        # Chama a função para analisar automaticamente após a adição
        st.session_state['resultado'], st.session_state['totais'] = analisar_roleta(lista_master)
    except ValueError:
        st.error("Por favor, insira números válidos.")

# Campo para adicionar novos números (ao pressionar Enter)
novo_numero_input = st.text_input(
    "Adicionar novos números à lista (cole múltiplos números separados por vírgula ou espaço)",
    value=st.session_state['novo_numero'] if 'novo_numero' in st.session_state else "",
    key="novo_numero",
    on_change=lambda: adicionar_numeros(st.session_state['novo_numero'])
)

# Exibe imagens após adicionar números
if st.session_state['lista_master']:
    lista_master = st.session_state['lista_master']
    exibir_imagens(lista_master)

# Variável para armazenar legenda atual
if 'legenda' not in st.session_state:
    st.session_state['legenda'] = ""

# Exibe a legenda se houver
if st.session_state['legenda']:
    st.markdown(f"<p style='font-size:14px'>{st.session_state['legenda']}</p>", unsafe_allow_html=True)

# Linha de botões dividida em três linhas
st.markdown("<h3>Painel de Resultados</h3>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
col8, col9, col10, col11, col12, col13, col14 = st.columns(7)
col15, col16, col17, col18, col19, col20, col21 = st.columns(7)

with col1:
    if st.button("Cor"):
        circular_atributo('Cor', ['Vermelho', 'Preto'], {'Vermelho': cores['Cor']['Vermelho'], 'Preto': cores['Cor']['Preto']})
        st.session_state['legenda'] = ""

with col2:
    if st.button("Par/Ímpar"):
        circular_atributo('Par/Ímpar', ['Par', 'Ímpar'], {'Par': cores['Par/Ímpar']['Par'], 'Ímpar': cores['Par/Ímpar']['Ímpar']})
        st.session_state['legenda'] = ""

with col3:
    if st.button("Dúzia"):
        circular_atributo('Dúzia', ['D1', 'D2', 'D3'], {'D1': cores['Dúzia']['D1'], 'D2': cores['Dúzia']['D2'], 'D3': cores['Dúzia']['D3']})
        st.session_state['legenda'] = ""

with col4:
    if st.button("Coluna"):
        circular_atributo('Coluna', ['C1', 'C2', 'C3'], {'C1': cores['Coluna']['C1'], 'C2': cores['Coluna']['C2'], 'C3': cores['Coluna']['C3']})
        st.session_state['legenda'] = ""

with col5:
    if st.button("Seção"):
        circular_atributo('Seção', ['Zero', 'Voisin', 'Orphelins', 'Tier'], {'Zero': cores['Seção']['Zero'], 'Voisin': cores['Seção']['Voisin'], 'Orphelins': cores['Seção']['Orphelins'], 'Tier': cores['Seção']['Tier']})
        st.session_state['legenda'] = ""

with col6:
    if st.button("Tipo"):
        circular_atributo('Tipo', ['Separado', 'Junto'], {'Separado': cores['Tipo']['Separado'], 'Junto': cores['Tipo']['Junto']})
        st.session_state['legenda'] = ""

with col7:
    if st.button("Terminal"):
        circular_atributo('Terminal', [str(i) for i in range(10)], cores['Terminal'])
        st.session_state['legenda'] = ""

# Segunda linha de botões
with col8:
    if st.button("Espelho +1v"):
        aplicar_espelho()
        st.session_state['legenda'] = "Numeros: 12,21,32,23,13,31 (+1v)"

with col9:
    if st.button("11-22-33 +1v"):
        aplicar_112233()
        st.session_state['legenda'] = "Numeros: 11,22,33,0 (+1v)"

with col10:
    if st.button("Term Alto"):
        aplicar_filtro_term(alto=True)

with col11:
    if st.button("Term Baixo"):
        aplicar_filtro_term(alto=False)

with col12:
    if st.button("Term 1-9"):
        aplicar_terminal([1,2,3,4,5,6,7,8,9], [])
        st.session_state['legenda'] = "Numeros: 1,2,3,4,5,6,7,8,9"

with col13:
    if st.button("Term 10-19"):
        aplicar_terminal([10,11,12,13,14,15,16,17,18,19], [])
        st.session_state['legenda'] = "Numeros: 10,11,12,13,14,15,16,17,18,19"

with col14:
    if st.button("Term 20-29"):
        aplicar_terminal([20,21,22,23,24,25,26,27,28,29], [])
        st.session_state['legenda'] = "Numeros: 20,21,22,23,24,25,26,27,28,29"

# Terceira linha de botões
with col15:
    if st.button("Term 0"):
        aplicar_terminal([0,10,20,30], [])
        st.session_state['legenda'] = "Numeros: 0,10,20,30 (+2v)"

with col16:
    if st.button("Term 1"):
        aplicar_terminal([1,11,21,31], [])
        st.session_state['legenda'] = "Numeros: 1,11,21,31 (+2v)"

with col17:
    if st.button("Term 2"):
        aplicar_terminal([2,12,22,32], [])
        st.session_state['legenda'] = "Numeros: 2,12,22,32 (+2v)"

with col18:
    if st.button("Term 3"):
        aplicar_terminal([3,13,23,33], [])
        st.session_state['legenda'] = "Numeros: 3,13,23,33 (+2v)"

with col19:
    if st.button("Term 4"):
        aplicar_terminal([4,14,24,34], [])
        st.session_state['legenda'] = "Numeros: 4,14,24,34 (+2v)"

with col20:
    if st.button("Term 5"):
        aplicar_terminal([5,15,25,35], [])
        st.session_state['legenda'] = "Numeros: 5,15,25,35 (+2v)"

with col21:
    if st.button("Term 6"):
        aplicar_terminal([6,16,26,36], [])
        st.session_state['legenda'] = "Numeros: 6,16,26,36 (+2v)"

with col1:
    if st.button("Term 7"):
        aplicar_terminal([7,17,27], [])
        st.session_state['legenda'] = "Numeros: 7,17,27 (+2v)"

with col2:
    if st.button("Term 8"):
        aplicar_terminal([8,19,28], [])
        st.session_state['legenda'] = "Numeros: 8,19,28 (+2v)"

with col3:
    if st.button("Term 9"):
        aplicar_terminal([9,19,9], [])
        st.session_state['legenda'] = "Numeros: 9,19,9 (+2v)"

# Exibe o Painel de Resultados
if st.session_state['lista_master']:
    lista_master = st.session_state['lista_master']
    st.markdown(formatar_lista_master(lista_master, st.session_state['circulados']), unsafe_allow_html=True)
