import streamlit as st

# Inicializa o estado se não existir
if 'aguaBebida' not in st.session_state:
    st.session_state.aguaBebida = []

st.title("Ingestão de Água")

st.subheader('Registre a quantidade de água que você irá beber durante o dia.')

# Verifica se as informações do usuário estão no session_state
if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "peso" in st.session_state:
    st.write("Coletamos suas informações de saúde e calculamos a quantidade ideal de água que você deve ingerir todos os dias.")
    
    with st.form("ingestao de agua"):
        peso = st.session_state['peso']
        agua = (peso * 35) / 1000
        st.write(f"De acordo com o seu peso, você precisa beber {agua:.1f} litros diariamente.")
        st.header(f"Sua meta de hoje: {agua:.1f} Litros.")
        
        if agua > 0:
            # Exibe o quanto o usuário já bebeu, e armazena isso no session_state
            qtdBebida = st.number_input("Quantos litros de água você já bebeu?", min_value=0.0, value=0.0, step=0.1)
            if qtdBebida > 0:
                st.session_state.aguaBebida.append(qtdBebida)
        
        bebeu = st.form_submit_button("Registrar")
        
    if bebeu:
        total_bebido = sum(st.session_state.aguaBebida)
        

                # Verifica o status da ingestão de água
    if bebeu:
        if total_bebido < agua:
            st.subheader(f"Ainda faltam {agua - total_bebido:.1f} litros para você alcançar sua meta.")
            st.header(f"Total de água ingerido até agora: {total_bebido:.1f} L.") 
        elif total_bebido >= agua:
            st.subheader(f"Total de água ingerido até agora: {total_bebido:.1f} L.") 
            st.session_state['agua'] = True  # Marca que a meta foi atingida

    if "agua" in st.session_state and st.session_state["agua"]:
        st.success("Parabéns! Você atingiu sua meta!")

    navegar = st.button("Ir para Registro de Atividades")
    if navegar:
        st.switch_page("pages\Registro de Atividades.py")    


        
        

else:
    st.warning("Realize o Cadastro para acessar.")
