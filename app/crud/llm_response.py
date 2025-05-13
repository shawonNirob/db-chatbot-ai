from fastapi import HTTPException
from app.llm.get_llm import get_llm_response
from loguru import logger
from app.schemas.process_schema import LLMAction
from app.crud.db_crud import crud_operation

def sql_processor(data: LLMAction) -> dict:
    try:
        action = data.action
        content = data.content

        if action == "singleSQL":
            result = crud_operation(content)
            return result

        elif action == "multipleSQL":
            if isinstance(content, list):
                results = []
                for sql in content:
                    result = crud_operation(sql)
                    results.append(result)
                return results

            elif isinstance(content, str):
                result = crud_operation(content)
                return result

        elif action == "question":
            return {"action": "question", "content": content}

        elif action == "logic":
            return {"action": "logic", "content": content}

        else:
            return {"error": "Unknown action in LLM response"}

    except Exception as e:
        logger.error(f"LLM processing failed: {str(e)}")
        raise HTTPException(status_code=500, detail=f"LLM Response Processing failed: {str(e)}")


# if operation == "select":
#     data = run_sql(sql)
#     return response_chain.run(question=user_query, data=data)

# elif operation in ["insert", "update", "delete"]:
#     run_sql(sql)
#     return f"{operation.upper()} operation completed successfully."

# elif operation == "create":
#     run_sql(sql)
#     return "Table or object created successfully."

# else:
#     return "Unsupported SQL operation or invalid syntax."