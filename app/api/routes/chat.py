from fastapi import APIRouter, HTTPException
from app.schemas.chat_schema import AskRequest

router = APIRouter()

QUERY_CHAR_LIMIT = 250

@router.post("/ask", response_model=dict, status_code=200)
def ask(request: AskRequest):
    if len(request.query) > QUERY_CHAR_LIMIT:
        return {"error": "Query size exceeded", "allowed_limit": QUERY_CHAR_LIMIT}

    try:
        return vector_search(request.query)
    except Exception as e:
        raise HTTPException(status_code=500, details=str(e))

@router.post("/reset")
def reset_memory():
    memory.clear()
