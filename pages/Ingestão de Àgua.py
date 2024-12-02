import streamlit as st

aguaBebida = []

st.title("Ingestão de Àgua")


st.write('Informe seu peso para calcular quantos litros você deve beber diariamente.')

if 'aguaBebida' not in st.session_state:
    st.session_state.aguaBebida = []

with st.form("ingestao de agua"):
    peso = st.number_input("Digite seu peso (kg):", min_value=0.0, step=0.1)
            
    enviado = st.form_submit_button("Calcular")
    if enviado:
        if peso == 0:
            st.error("Por favor, insira um peso válido.")    
        else:
            agua = (peso*35)/1000
            st.write(f"Você precisa beber {agua:.1f} litros diariamente.")    

            

with st.form("registro_de_agua"):
    agua = (peso*35)/1000
    st.header(f"Sua Meta: {agua:.1f} Litros.")
    if agua > 0:
        qtdBebida = st.number_input("Quantos litros de água você já bebeu?", min_value=0.0, value=0.0, step=0.1)
        if qtdBebida > 0:
            st.session_state.aguaBebida.append(qtdBebida)
    bebeu = st.form_submit_button("Registrar")

    if bebeu:
        total_bebido = sum(st.session_state.aguaBebida)

        # Verifica o status da ingestão de água
        if total_bebido < agua:
            st.header(f"Ainda faltam {agua - total_bebido:.1f} litros para você alcançar sua meta.")
        elif total_bebido > agua:
            st.warning("Você excedeu sua meta de ingestão de água!")
        elif total_bebido > agua:
            st.warning("Você excedeu sua meta de ingestão de água!")
        elif total_bebido == agua:
            st.success("Parabéns! Você atingiu sua meta de ingestão de água!")    
                
            # Exibe o total de água ingerido
        st.write(f"Total de água ingerido até agora: {total_bebido:.1f} L.")
                                            




