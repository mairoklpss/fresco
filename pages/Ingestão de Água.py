import streamlit as st

aguaBebida = []

st.title("Ingestão de Água")


st.write('Registre a quantidade de água que você irá beber durante o dia.')
if 'aguaBebida' not in st.session_state:
    st.session_state.aguaBebida = []

if "nome" in st.session_state and "email" in st.session_state and "senha" in st.session_state and "condições" in st.session_state and "peso" in st.session_state:
    if "agua" in st.session_state and st.session_state["agua"]:
        st.success("Parabéns! Você atingiu sua meta de ingestão de água!")  


    with st.form("ingestao de agua"):
        peso = st.session_state['peso']
        st.write(f"Seu peso é de {peso}Kg.")        
        agua = (peso*35)/1000
        st.write(f"Você precisa beber {agua:.1f} litros diariamente.")    
        st.header(f"Sua Meta: {agua:.1f} Litros.")
        if agua > 0:
            qtdBebida = st.number_input("Quantos litros de água você já bebeu?", min_value=0.0, value=0.0, step=0.1)
            if qtdBebida > 0:
                st.session_state.aguaBebida.append(qtdBebida)
        bebeu = st.form_submit_button("Registrar")

        if bebeu:
            total_bebido = sum(st.session_state.aguaBebida)

            # Verifica o status da ingestão de água
            if total_bebido > agua:
                st.warning("Você excedeu sua meta de ingestão de água!")
                st.header(f"Total de água ingerido até agora: {total_bebido:.1f} L.")  
            elif total_bebido < agua:
                st.header(f"Ainda faltam {agua - total_bebido:.1f} litros para você alcançar sua meta.")
                st.header(f"Total de água ingerido até agora: {total_bebido:.1f} L.")  
            elif total_bebido > agua:
                st.warning("Você excedeu sua meta de ingestão de água!")
                st.header(f"Total de água ingerido até agora: {total_bebido:.1f} L.")  
            elif total_bebido == agua:  
                st.header(f"Total de água ingerido até agora: {total_bebido:.1f} L.")  
                st.session_state['agua'] = True
           
                                                


else:
    st.warning("Realize o Cadastro para acessar.")    


