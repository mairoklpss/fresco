import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

st.title("Registro de Atividades Físicas")
st.subheader("Registre as atividades físicas realizadas durante o seu dia.")
# Inicializa o estado se não existir
if "atvd" not in st.session_state:
    st.session_state.atvd = []

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "peso" in st.session_state:

   
    with st.form("registro"):
        data = st.date_input("Data:")
        atividade = st.text_input("Digite a atividade física realizada:", placeholder="Ex: Corrida, Academia...")
        duracao = st.text_input("Duração (em minutos):")
        registro = st.form_submit_button("Registrar")

        if registro:
            if not atividade or not duracao:  # Verifica campos vazios
                st.error("Verifique se todos os campos estão preenchidos corretamente.")
            elif not duracao.isdigit() or int(duracao) <= 0:  # Valida duração como número positivo
                st.error("Por favor, insira um valor válido para a duração (número positivo).")
            else:
                st.session_state.atvd.append({
                    "data": data,
                    "atvd": atividade,
                    "duração": int(duracao),  # Converte duração para inteiro
                })
                st.success(f"{atividade} registrada com sucesso!")
                st.session_state["atividade"] = atividade
                st.session_state["duraçao"] = duracao

    st.subheader("Atividades Registradas")
    if st.session_state.atvd:
        for i, atvd in enumerate(st.session_state.atvd):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"📈 {atvd['atvd']} - Duração: {atvd['duração']} minutos, realizada em {atvd['data']}")
            with col2:
                if st.button("❌ Remover", key=f"remove_{i}"):
                    del st.session_state.atvd[i]  # Remove a atividade

        # Criar o DataFrame para visualização
        df = pd.DataFrame(st.session_state.atvd)

        # Gráfico com Matplotlib
        if not df.empty:
            # Criando uma nova coluna para um identificador único da atividade
            df["atividade_id"] = [f"{atvd}_{i}" for i, atvd in enumerate(df["atvd"])]

            fig, ax = plt.subplots(figsize=(10, 5))
            ax.bar(df["atividade_id"], df["duração"], color='skyblue')
            ax.set_title("Duração das Atividades Registradas")
            ax.set_xlabel("Atividade")
            ax.set_ylabel("Duração (minutos)")

            # Ajusta os rótulos corretamente com atividades únicas
            ax.set_xticks(range(len(df)))  # Ajusta os ticks para o número de atividades
            ax.set_xticklabels(df["atividade_id"], rotation=45, ha="right")
            
            st.pyplot(fig)
    else:
        st.info("Nenhuma atividade registrada.")

    navegar = st.button("Ir para Ingestão de Água")
    if navegar:
        st.switch_page("pages\Ingestão de Água.py")      

 
else:
    st.warning("Realize o Cadastro para acessar.")       
