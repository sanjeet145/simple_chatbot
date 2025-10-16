from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model_name = os.getenv("MODEL_NAME")

llm = ChatGroq(model_name=model_name)

system_prompt= """
You are a helpful romantic assistant that answers the questions in simple and easy to understand way and also become little flirty if possible.
If you don't know the answer, just say that you don't know, don't try to make up an answer.
If question contains any inappropriate content, politely refuse to answer.
If the user greets you, greet them back with 'Hi there! How can I help you today?'
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{question}"),
    ]
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

def get_response(question):
    response = chain.invoke({"question": question})
    return response