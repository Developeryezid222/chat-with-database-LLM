import streamlit as st
from engine_sql import get_sql_agent


st.set_page_config(page_title="DataInsight AI", layout="wide", page_icon="📊")


with st.sidebar:
    st.title("⚙️ Configuración")
    st.info("Conectado a: MySQL (Producción)")
    if st.button("Limpiar Historial"):
        st.session_state["messages"] = [{"role": "system", "content": "Eres un asistente útil para análisis de datos SQL."}]
        st.rerun()

st.title("📊 DataInsight: Analista SQL Inteligente")

if "agent_executor" not in st.session_state:
    with st.spinner("Inicializando agente SQL..."):
        st.session_state.agent_executor = get_sql_agent()


# Inicializar historial de chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes anteriores (Estilo ChatGPT)
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input de Chat
if prompt := st.chat_input("¿Qué tablas tienes disponibles?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Analizando datos..."):
            try:
                # Ejecutar el agente
                full_response = st.session_state.agent_executor.invoke({"input": prompt})
                
                # 1. Extraer el contenido del 'output'
                raw_output = full_response.get("output", "")

                # 2. Si el output es una lista (como te está pasando), unir los textos
                if isinstance(raw_output, list):
                    clean_answer = ""
                    for item in raw_output:
                        if isinstance(item, dict) and "text" in item:
                            clean_answer += item["text"]
                        elif isinstance(item, str):
                            clean_answer += item
                    answer = clean_answer
                else:
                    answer = str(raw_output)

                # 3. Mostrar solo el texto limpio
                st.markdown(answer)
                
                # Guardar en el historial
                st.session_state.messages.append({"role": "assistant", "content": answer})

            except Exception as e:
                st.error(f"Hubo un problema: {e}")