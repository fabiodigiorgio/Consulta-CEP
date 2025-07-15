
import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Consulta Área Atendimento", layout="centered")

# Dados embutidos do ccep.xlsx
dados_embutidos = [{'Cidade': 'São Paulo', 'CEP Inicial': '01000-000', 'CEP Final': '05999-999'}, {'Cidade': 'Guarulhos', 'CEP Inicial': '07000-000', 'CEP Final': '07399-999'}, {'Cidade': 'Barueri', 'CEP Inicial': '06400-000', 'CEP Final': '06499-999'}, {'Cidade': 'Jundiaí', 'CEP Inicial': '13200-000', 'CEP Final': '13299-999'}, {'Cidade': 'Santo André', 'CEP Inicial': '09000-000', 'CEP Final': '09299-999'}, {'Cidade': 'São Bernardo do Campo', 'CEP Inicial': '09600-000', 'CEP Final': '09899-999'}, {'Cidade': 'São Caetano do Sul', 'CEP Inicial': '09500-000', 'CEP Final': '09599-999'}, {'Cidade': 'Louveira', 'CEP Inicial': '13290-000', 'CEP Final': '13299-999'}, {'Cidade': 'Franco da Rocha', 'CEP Inicial': '07800-000', 'CEP Final': '07899-999'}, {'Cidade': 'Atibaia', 'CEP Inicial': '12940-000', 'CEP Final': '12949-999'}, {'Cidade': 'Alphaville', 'CEP Inicial': '06540-000', 'CEP Final': '06549-999'}]

df_ceps = pd.DataFrame(dados_embutidos)

# Logo centralizado
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    try:
        logo = Image.open("logo.png")
        st.image(logo, width=150)
    except:
        st.warning("⚠️ Logo não encontrado. Certifique-se de que 'logo.png' está na mesma pasta do script.")

# Título e instrução
st.title("🔍 Consulta Área Atendimento")
st.markdown("Digite um CEP válido para verificar se há atendimento disponível.")

# Campo de entrada de CEP
cep_input = st.text_input("CEP (Ex: 07010-000 ou 07010000)", max_chars=9)

# Função para verificar se o CEP está na faixa de atendimento
def verificar_cep_em_faixa(cep_digitado, df_ceps):
    try:
        cep_numerico = int(cep_digitado.replace("-", "").strip())
        for _, row in df_ceps.iterrows():
            cep_inicio = int(row["CEP Inicial"].replace("-", "").strip())
            cep_fim = int(row["CEP Final"].replace("-", "").strip())
            if cep_inicio <= cep_numerico <= cep_fim:
                return row["Cidade"]
        return None
    except:
        return "FORMATO DE CEP INVÁLIDO"

if cep_input:
    cidade = verificar_cep_em_faixa(cep_input, df_ceps)

    if cidade == "FORMATO DE CEP INVÁLIDO":
        st.error("❌ FORMATO DE CEP INVÁLIDO")
    elif cidade:
        st.success(f"✅ ATENDIMENTO DISPONÍVEL EM: {cidade}")
    else:
        st.warning("⚠️ INDISPONIBILIDADE DE ATENDIMENTO")

# Rodapé
st.markdown("---")
st.caption("Consulta baseada em faixas de CEP embutidas no código.")
