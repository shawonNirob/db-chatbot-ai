from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from app.prompts.db_prompt import sql_prompt
from app.prompts.response_prompt import resp_prompt
from app.prompts.dberror_prompt import error_prompt
from app.config import settings
import os

os.environ["API_KEY"] = settings.API_KEY

llm = ChatOpenAI(temperature=0.7, model=settings.MODEL_ID)

#return_messages=True: Instead of returning the chat history as a plain string, 
#it returns a list of HumanMessage and AIMessage objects
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

sql_chain = LLMChain(llm=llm, prompt=sql_prompt, memory=memory)
response_chain = LLMChain(llm=llm, prompt=resp_prompt, memory=memory)
dberror_chain = LLMChain(llm=llm, prompt=error_prompt, memory=memory)