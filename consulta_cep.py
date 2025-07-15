import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Consulta Área Atendimento", layout="centered")

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

# Carregar o arquivo de CEPs
try:
    df_ceps = pd.read_excel("ccep.xlsx")
except:
    st.error("❌ Arquivo ccep.xlsx não encontrado. Certifique-se de que está na mesma pasta do script.")
    st.stop()

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
st.caption("Consulta baseada em faixas de CEP definidas no arquivo ccep.xlsx.")