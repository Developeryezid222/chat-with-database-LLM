# 🤖 AI SQL Analyst - Consultas en Lenguaje Natural con Gemini 2.0

La implementación de este agente de IA no es solo un ejercicio técnico, sino una solución de negocio que resuelve los siguientes puntos de dolor:

Democratización de los Datos: Permite que personal no técnico (Ventas, RRHH, Gerencia) obtenga insights de la base de datos sin depender de un analista o desarrollador para escribir queries SQL.

Reducción de Latencia en Reportes: Consultas que antes tomaban minutos en ser redactadas y ejecutadas se resuelven en segundos, acelerando la toma de decisiones basada en datos.

Eficiencia Operativa: Libera al equipo de ingeniería de tareas repetitivas de extracción de datos, permitiéndoles enfocarse en el desarrollo de funcionalidades core.

Escalabilidad con Gemini 2.0 Flash: El uso de este modelo específico garantiza una respuesta casi instantánea y un costo operativo significativamente bajo (token-efficient) en comparación con modelos más grandes, sin sacrificar precisión.

Prevención de Errores Humanos: Al automatizar la generación de joins y filtros complejos, se reduce el riesgo de errores en la sintaxis SQL que podrían entregar datos incorrectos. 

💡 Casos de Uso Reales
- Soporte Tecnico: "¿Cuáles son los 5 productos con más reportes de falla este mes?"
- Recursos Humanos: "¿Generame una tabla de los desarrolladores que ingresaron en el mes de Enero a marzo?".



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
python -m venv venv
# En Windows:
.\venv\Scripts\activate

Autor: Yezid Perez - Est Ingenieria de Sistemas.

