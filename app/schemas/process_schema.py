from pydantic import BaseModel

class LLMAction(BaseModel):
    action: str
    content: str | list[str] | dict


