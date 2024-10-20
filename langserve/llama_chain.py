#from langchain_community.llms import Ollama

from langchain.prompts.prompt import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import ChatOllama

from langserve.pydantic_v1 import BaseModel

llm = ChatOllama(
    model="llama3.1",
    temperature=0,
    # other params...
)


# Templates
_TEMPLATE = """Dado el siguiente documento, genera un resumen detallado y extenso del mismo, en su idioma original.
{document}

Instrucciones para el resumen:
- Destaca los puntos clave del documento.
- Proporciona detalles relevantes que ayuden a entender mejor el contenido.
- Enfócate en la esencia del contenido para una comprensión rápida y efectiva.
- Mantén la objetividad y precisión en la información presentada, evitando sesgos o interpretaciones subjetivas.
- Estructura el resumen en párrafos separados por temas o secciones importantes.
- Incluye ejemplos específicos y citas textuales cuando sea relevante.
- Si hay varias secciones o capítulos, proporciona un resumen detallado de cada uno.

Resumen:"""


# Prompts
SUMMARY_PROMPT = PromptTemplate.from_template(_TEMPLATE)




def get_summary_chain():

    # User input
    class interactive_data(BaseModel):
        """Summary of a note."""

        document: str



    summary_chain = (
        SUMMARY_PROMPT | llm | StrOutputParser()
    )

    chain = summary_chain.with_types(input_type=interactive_data)


    return chain


