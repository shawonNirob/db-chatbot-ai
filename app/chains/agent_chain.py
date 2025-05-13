import json
import requests
from fastapi import HTTPException
from app.config import settings
from loguru import logger
from app.chains.llm_chain import sql_chain
from app.crud.llm_response import sql_processor
from app.rag import search_embeddings

async def vector_search(query: str) -> dict:
    #Find the database embeddings
    schemas = await search_vector(query)

    #get the LLM response
    sql_result = sql_chain.run(schemas=schemas, question=query)

    #return sql_processor(sql_result)
    return sql_result


