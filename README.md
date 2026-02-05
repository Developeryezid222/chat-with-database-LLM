# 🤖 AI SQL Analyst - Consultas en Lenguaje Natural con Gemini 2.0

Este proyecto es un asistente inteligente capaz de interactuar con bases de datos SQL (MySQL) utilizando lenguaje natural. Construido con **LangChain** y **Google Gemini 2.0 Flash**, permite a usuarios no técnicos obtener insights, métricas y reportes complejos sin escribir una sola línea de SQL.

Lo bacano de hacer estos proyectos es la satisfación y aprendizaje de que nunca paramos de aprender.. 



## 🌟 Características Principales
- **Interfaz Intuitiva:** Chat interactivo desarrollado en Streamlit.
- **Razonamiento Complejo:** Capacidad para ejecutar subconsultas y CTEs mediante el agente de LangChain.
- **Multimodelo:** Integración optimizada para Gemini 2.0 Flash (con soporte previo para OpenAI).
- **Seguridad:** Manejo de variables de entorno para proteger credenciales y llaves de API.
- **Análisis de Nómina y Ventas:** Configurado para manejar datos sensibles y agregaciones financieras.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.x
- **LLM:** Google Gemini 2.0 Flash (via `langchain-google-genai`)
- **Orquestador:** LangChain (SQL Agent)
- **Base de Datos:** MySQL / SQLAlchemy
- **Frontend:** Streamlit

## 🚀 Instalación y Configuración

### 1. Clonar el repositorio
```bash
git clone [https://github.com/tu-usuario/Sql-analyst-IA.git](https://github.com/tu-usuario/Sql-analyst-IA.git)
cd Sql-analyst-IA