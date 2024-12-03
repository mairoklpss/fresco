import streamlit as st

st.title("Monitorização de Atividade")
st.subheader("Registre e acompanhe suas atividades físicas diárias.")

if "atvd" not in st.session_state:
    st.session_state.atvd = []

 

st.subheader("Registrar Atividades Físicas Realizadas")   
with st.form("registro"):
    data = st.date_input("Data:")
    atividade = st.text_input("Digite a atividade física realizada:", placeholder= "Ex: Corrida, Academia...")
    duracao = st.text_input("Duração (em minutos):")
    registro = st.form_submit_button("Registrar")

    if registro:
        if data == "" or atividade == "" or duracao == "":
            st.error("Verifique se todos os campos estão preenchidos corretamente.")
        else:
            st.session_state.atvd.append({"data": data, "atvd": atividade, "duração": duracao})
            st.success(f"{atividade} realizada em {data} registrada com sucesso!")


st.subheader("Atividades Registradas")
for i, atvd in enumerate(atividade):
    col1 = st.columns([0.8])
    with col1:
        st.write(f"📈 {atvd["atividade"]} - Duração: {atvd["duração"]}, realizada em {atvd["data"]}")

         
