
from fastapi import FastAPI
from langserve import add_routes
from llama_chain import get_chain





app = FastAPI(
    title="LangChain Server",
    version="1.0.0",
    description="Langserve usado para el chatbot acerca de DOFs de la materia de Ingeniería de Software",
)
# Adds routes to the app for using the chain under:
# /invoke
# /batch
# /stream


add_routes(app,
            get_chain(), 
            path= "/generate_info",
            )



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)