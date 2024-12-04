import streamlit as st

st.title("Monitorização de Atividade")
st.subheader("Registre e acompanhe suas atividades físicas diárias.")

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "condições" in st.session_state:
  
    # Inicializa o estado se não existir
    if "atvd" not in st.session_state:
        st.session_state.atvd = []

    st.subheader("Registrar Atividades Físicas Realizadas")
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
                    "duração": duracao,
                })
                st.success(f"{atividade} realizada em {data} registrada com sucesso!")

    # Ordena atividades por data
    atividades_ordenadas = sorted(st.session_state.atvd, key=lambda x: x["data"])

    st.subheader("Atividades Registradas")
    if atividades_ordenadas:
        for i, atvd in enumerate(atividades_ordenadas):
            col1, col2 = st.columns([0.8, 0.2])
            with col1:
                st.write(f"📈 {atvd['atvd']} - Duração: {atvd['duração']} minutos, realizada em {atvd['data']}")
            with col2:
                if st.button("❌ Remover", key=f"remove_{i}"):
                    del st.session_state.atvd[i]  # Remove a atividade 
    else:
        st.info("Nenhuma atividade registrada.")

   

else:
    st.warning("Realize o cadastro para acessar.")   