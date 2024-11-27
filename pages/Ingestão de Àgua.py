import streamlit as st

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state:
    st.success("td ok")
else:
    st.warning("nd ok")    