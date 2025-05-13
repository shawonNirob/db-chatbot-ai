from langchain.prompts import PromptTemplate
from app.chains.memory_chain import memory

error_prompt = PromptTemplate( input_variable=["chat_history", "error"], template="""
    Conversation so far:
    "{chat_history}"

    Database error:
    "{error}"

    Respond ONLY in this JSON format:

    - Summarize or response to the user like this:
    {{
        "action": "response",
        "content": "<a clear response to the user>"
    }}

    """
)