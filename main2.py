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
    25: 'https://iili.io/dQoYGTX.png',  # Corrigido o hiperlink da imagem do número 25
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

# Inicializa variáveis no session_state
if 'lista_master' not in st.session_state:
    st.session_state['lista_master'] = []

if 'circulados' not in st.session_state:
    st.session_state['circulados'] = {}

# Adiciona persistência para as legendas
if 'legenda' not in st.session_state:
    st.session_state['legenda'] = None

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

# Função para aplicar legendas
def aplicar_legenda(legenda_texto):
    st.session_state['legenda'] = legenda_texto

# Função para aplicar filtro do botão de terminal
def aplicar_terminal(escuros, claros, legenda_texto):
    st.session_state['circulados'] = {}
    aplicar_legenda(legenda_texto)
    for numero in escuros:
        st.session_state['circulados'][numero] = {'Terminal': ('#00008B', 'white')}  # Azul escuro e letra branca
    for numero in claros:
        st.session_state['circulados'][numero] = {'Terminal': ('#ADD8E6', 'black')}  # Azul claro e letra preta

# Função para aplicar filtro do botão "Espelho +1v"
def aplicar_espelho():
    st.session_state['circulados'] = {}
    aplicar_legenda("Numeros: 12,21,32,23,13,31 (+1v)")
    numeros_verde_escuro = [12, 21, 32, 23, 13, 31]
    numeros_verde_claro = [0, 2, 4, 8, 9, 10, 14, 15, 26, 28, 35, 36]
    for numero in numeros_verde_escuro:
        st.session_state['circulados'][numero] = {'Espelho +1v': ('#006400', 'white')}  # Verde escuro e letra branca
    for numero in numeros_verde_claro:
        st.session_state['circulados'][numero] = {'Espelho +1v': ('#90EE90', 'black')}  # Verde claro e letra preta

# Função para aplicar filtro do botão "11-22-33 +1v"
def aplicar_112233():
    st.session_state['circulados'] = {}
    aplicar_legenda("Numeros: 11,22,33,0 (+1v)")
    numeros_verde_escuro = [11, 22, 33, 0]
    numeros_verde_claro = [26, 32, 36, 30, 9, 18, 1, 16]
    for numero in numeros_verde_escuro:
        st.session_state['circulados'][numero] = {'11-22-33 +1v': ('#006400', 'white')}  # Verde escuro e letra branca
    for numero in numeros_verde_claro:
        st.session_state['circulados'][numero] = {'11-22-33 +1v': ('#90EE90', 'black')}  # Verde claro e letra preta

# Função para aplicar filtro do botão "Terminal Alto"
def aplicar_terminal_alto():
    st.session_state['circulados'] = {}
    aplicar_legenda("Numeros: 6,16,26,36,7,17,27,8,18,28,9,19,29")
    numeros_terminal_alto = [6, 16, 26, 36, 7, 17, 27, 8, 18, 28, 9, 19, 29]
    for numero in numeros_terminal_alto:
        st.session_state['circulados'][numero] = {'Terminal Alto': ('#00008B', 'white')}  # Azul escuro e letra branca

# Função para aplicar filtro do botão "Terminal Baixo"
def aplicar_terminal_baixo():
    st.session_state['circulados'] = {}
    aplicar_legenda("Numeros: 0,10,20,30,1,11,21,31,2,12,22,32,3,13,23,33,4,14,24,34,5,25,35")
    numeros_terminal_baixo = [0, 10, 20, 30, 1, 11, 21, 31, 2, 12, 22, 32, 3, 13, 23, 33, 4, 14, 24, 34, 5, 25, 35]
    for numero in numeros_terminal_baixo:
        st.session_state['circulados'][numero] = {'Terminal Baixo': ('#00008B', 'white')}  # Azul escuro e letra branca

# Função para adicionar números ao pressionar "Enter"
def adicionar_numeros(novo_numero_input):
    try:
        novos_numeros = tratar_lista_master(novo_numero_input)
        lista_master = st.session_state['lista_master']
        lista_master = novos_numeros + lista_master  # Adiciona os novos números no início da lista master
        st.session_state['lista_master'] = lista_master  # Atualiza a lista master
        st.session_state['novo_numero'] = ""  # Limpa o campo de entrada
    except ValueError:
        st.error("Por favor, insira números válidos.")

# Campo para adicionar novos números (ao pressionar Enter)
novo_numero_input = st.text_input(
    "Adicionar novos números à lista (cole múltiplos números separados por vírgula ou espaço)",
    value=st.session_state['novo_numero'] if 'novo_numero' in st.session_state else "",
    key="novo_numero",
    on_change=lambda: adicionar_numeros(st.session_state['novo_numero'])
)

# Linha abaixo das imagens dividida em duas colunas (esquerda e direita)
col_esquerda, col_direita = st.columns([0.6, 0.4])

# Coluna da direita - Apresentar a "Painel de resultados" e os botões
with col_direita:
    # Botões de atributos
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)

    with col1:
        if st.button("Cor"):
            circular_atributo('Cor', ['Vermelho', 'Preto'], {'Vermelho': cores['Cor']['Vermelho'], 'Preto': cores['Cor']['Preto']})

    with col2:
        if st.button("Par/Ímpar"):
            circular_atributo('Par/Ímpar', ['Par', 'Ímpar'], {'Par': cores['Par/Ímpar']['Par'], 'Ímpar': cores['Par/Ímpar']['Ímpar']})

    with col3:
        if st.button("Dúzia"):
            circular_atributo('Dúzia', ['D1', 'D2', 'D3'], {'D1': cores['Dúzia']['D1'], 'D2': cores['Dúzia']['D2'], 'D3': cores['Dúzia']['D3']})

    with col4:
        if st.button("Coluna"):
            circular_atributo('Coluna', ['C1', 'C2', 'C3'], {'C1': cores['Coluna']['C1'], 'C2': cores['Coluna']['C2'], 'C3': cores['Coluna']['C3']})

    with col5:
        if st.button("Seção"):
            circular_atributo('Seção', ['Zero', 'Voisin', 'Orphelins', 'Tier'], {'Zero': cores['Seção']['Zero'], 'Voisin': cores['Seção']['Voisin'], 'Orphelins': cores['Seção']['Orphelins'], 'Tier': cores['Seção']['Tier']})

    with col6:
        if st.button("Tipo"):
            circular_atributo('Tipo', ['Separado', 'Junto'], {'Separado': cores['Tipo']['Separado'], 'Junto': cores['Tipo']['Junto']})

    with col7:
        if st.button("Terminal"):
            circular_atributo('Terminal', [str(i) for i in range(10)], cores['Terminal'])

    # Botões novos para aplicar os filtros "Espelho +1v" e "11-22-33 +1v"
    espelho_btn, analise_btn, alto_btn, baixo_btn = st.columns([1, 1, 1, 1])
    with espelho_btn:
        if st.button("Espelho +1v"):
            aplicar_espelho()

    with analise_btn:
        if st.button("11-22-33 +1v"):
            aplicar_112233()

    with alto_btn:
        if st.button("Terminal Alto"):
            aplicar_terminal_alto()

    with baixo_btn:
        if st.button("Terminal Baixo"):
            aplicar_terminal_baixo()

    # Botões para aplicar filtros de terminais
    cols_term = st.columns(10)
    for i, (label, escuros, claros, legenda) in enumerate([
        ("Term 0", [0, 10, 20, 30], [3, 26, 32, 15, 24, 5, 23, 8, 33, 1, 14, 31, 11, 36], "Numeros: 0,10,20,30 (+2v)"),
        ("Term 1", [1, 11, 21, 31], [16, 33, 20, 14, 8, 30, 36, 13, 25, 2, 4, 19, 9, 22], "Numeros: 1,11,21,31 (+2v)"),
        ("Term 2", [2, 12, 22, 32], [17, 25, 21, 4, 7, 28, 35, 3, 31, 9, 18, 29, 26, 0, 19, 15], "Numeros: 2,12,22,32 (+2v)"),
        ("Term 3", [3, 13, 23, 33], [12, 35, 26, 0, 11, 36, 27, 6, 5, 10, 8, 30, 24, 16, 1, 20], "Numeros: 3,13,23,33 (+2v)"),
        ("Term 4", [4, 14, 24, 34], [2, 21, 19, 15, 1, 20, 31, 9, 10, 5, 16, 33, 27, 6, 17, 25], "Numeros: 4,14,24,34 (+2v)"),
        ("Term 5", [5, 15, 25, 35], [23, 10, 24, 16, 4, 19, 32, 0, 34, 17, 2, 21, 28, 12, 3, 26], "Numeros: 5,15,25,35 (+2v)"),
        ("Term 6", [6, 16, 26, 36], [13, 27, 34, 17, 5, 24, 33, 1, 35, 3, 0, 32, 30, 11], "Numeros: 6,16,26,36 (+2v)"),
        ("Term 7", [7, 17, 27], [18, 29, 28, 12, 6, 34, 25, 2, 36, 13], "Numeros: 7,17,27 (+2v)"),
        ("Term 8", [8, 19, 28], [10, 23, 30, 11, 9, 22, 29, 7, 12, 35], "Numeros: 8,19,28 (+2v)"),
        ("Term 9", [9, 19, 9], [14, 31, 22, 18, 21, 4, 15, 32, 7, 28], "Numeros: 9,19,9 (+2v)"),
    ]):
        with cols_term[i]:
            if st.button(label):
                aplicar_terminal(escuros, claros, legenda)

# Coluna da esquerda - Painel de Resultados
with col_esquerda:
    st.markdown("<h3>Painel de Resultados</h3>", unsafe_allow_html=True)
    if st.session_state['legenda']:
        st.markdown(f"<p style='color: grey;'>Legenda: {st.session_state['legenda']}</p>", unsafe_allow_html=True)

    if st.session_state['lista_master']:
        lista_master = st.session_state['lista_master']
        st.markdown(formatar_lista_master(lista_master, st.session_state['circulados']), unsafe_allow_html=True)
