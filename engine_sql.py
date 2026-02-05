import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent

load_dotenv()

def get_sql_agent():
    # 1. Conexión a la DB
    db = SQLDatabase.from_uri(os.getenv("DATABASE_URL"))
    
    # 2. Configuración de Gpt (Gratis)
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash", 
        temperature=0,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    instrucciones = """
    Eres un experto en SQL Analytics. 
    Cuando se te pida comparar datos o buscar valores atípicos, DEBES usar subconsultas o CTEs (Common Table Expressions).
    
    Ejemplos de lógica que debes aplicar:
    - Si piden "productos por encima del promedio", primero calcula el promedio en una subconsulta.
    - Si piden "la ciudad que más aporta al total", usa agregaciones complejas.
    - Siempre calcula el total como (cantidad * precio_unitario).
    """
    # 3. Creación del Agente
    # Este agente tiene permiso para ver el esquema y ejecutar queries
    return create_sql_agent(
    llm=llm,
    db=db,
    agent_type="tool-calling",
    verbose=True,
    prefix=instrucciones,
    handle_parsing_errors=True
)