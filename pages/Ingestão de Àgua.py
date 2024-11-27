import streamlit as st

st.title("Ingestão de Àgua")


if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "condições" in st.session_state:
    st.write('Informe seu peso para calcular quantos litros você deve beber diariamente.')
    with st.form("ingestao de agua"):
        peso = st.number_input("Digite seu peso (kg):", min_value=0.0, step=0.1)
        
        enviado = st.form_submit_button("Calcular")
    
    if enviado:
        if peso > 0:
            litros = (peso *35) / 1000
            st.header(f"Você precisa beber {litros:.3f} litros.")
        else:
            st.error("Por favor, insira um peso inválido.")    
    
        








else:
    st.warning("Realize o cadastro para acessar.")    