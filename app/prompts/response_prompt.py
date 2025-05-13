from langchain.prompts import PromptTemplate
from app.chains.memory_chain import memory

resp_prompt = PromptTemplate( input_variable=["dtabase_returned", "chat_history"], template="""
    Conversation so far:
    "{chat_history}"

    Database returned:
    "{dtabase_returned}"

    Respond ONLY in this JSON format:

    - Summarize or response to the user like this:
    {{
        "action": "response",
        "content": "<a clear response to the user>"
    }}

    """
)