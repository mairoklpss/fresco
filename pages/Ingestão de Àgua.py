import streamlit as st

def ingestao():
   if "usuario" in st.session_state:
    usuario = st.session_state["usuario"]

    if usuario["nome"] and usuario["data de nascimento"] and usuario["sexo"] and usuario["email"] and usuario["senha"] and usuario["telefone"]:
        st.write("td ok")
    else:
        st.write("nd ok")
        st.error("Realize o cadastro para acessar esta página")

ingestao() 



