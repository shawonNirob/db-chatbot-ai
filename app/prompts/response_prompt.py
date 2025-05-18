from langchain.prompts import PromptTemplate

resp_prompt = PromptTemplate( input_variable=["question", "database_returned"], template="""
    User Query:
    "{question}"

    Database returned:
    "{database_returned}"

    Respond ONLY in this JSON format:

    - response to the user like this:
    {{
        "action": "response",
        "content": "<a clear natural language response to the user>"
    }}

    """
)