import json
import requests
from fastapi import HTTPException
from app.config import settings
from loguru import logger
from app.chains.llm_chain import sql_chain
from app.crud.llm_response import sql_processor
from app.rag import search_vector
import logging
from typing import Dict, Any
from langchain_core.messages import AIMessage
from app.utils.response_perser import parse_ai_message
from app.crud.llm_response import sql_processor
from app.schemas.process_schema import LLMAction
from app.chains.llm_chain import response_chain
from sqlalchemy.orm import Session

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def vector_search(db: Session, query: str) -> Dict[str, Any]:
    try:
        logger.info(f"Processing vector search for query: {query}")
        # Get the search results
        schema = search_vector(query)
        logger.info(f"Found {len(schema)} schema")

        #return sql_chain.run(schemas=schema, question=query)
        #return {"schema": schema}

        logger.info("Sending schema to the llm as a sql_prompt")


        #return sql_processor()

        response = sql_chain.invoke({
            "schemas": schema,
            "question": query
        }) #, config={"configurable": {"session_id": "some-user-session-id"}})

        logger.info(f"LLM response: {response}")


        parsed_response = parse_ai_message(response)
        logger.info(f"parsed_response: {parsed_response}")


        llm_action = LLMAction(**parsed_response)


        data = sql_processor(db, llm_action)
        logger.info(f"Data from database: {data}")

        second_response = response_chain.invoke({
            "question": query,
            "database_returned": data
        })

        final_response = parse_ai_message(second_response)
        logger.info(f"Final response: {final_response}")

        return final_response

    except Exception as e:
        logger.error(f"Error in vector_search: {e}")
        return {"error": str(e)}


