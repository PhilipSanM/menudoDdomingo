#from langchain_community.llms import Ollama

from langchain.prompts.prompt import PromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_ollama import ChatOllama

from pydantic.v1 import BaseModel, Field

llm = ChatOllama(
    model="llama2",
    temperature=0.3,
    base_url="https://e8hupnv84c4a4c-11434.proxy.runpod.net//api/generate"
    # other params...
)


# Templates
_TEMPLATE = """Dime que funcionas"""


# Prompts
SUMMARY_PROMPT = PromptTemplate.from_template(_TEMPLATE)




def get_chain():

    # User input
    class interactive_data(BaseModel):
        """Summary of a note."""

        document: str



    summary_chain = (
        SUMMARY_PROMPT | llm | StrOutputParser()
    )

    chain = summary_chain.with_types(input_type=interactive_data)


    return chain


