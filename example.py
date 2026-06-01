import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatGroq(
    groq_api_key=os.environ["GROQ_API_KEY"],
    model_name="llama-3.3-70b-versatile"
)

# Chain 1: Generate explanation
explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in detail for a software engineer."
)

explain_chain = explain_prompt | llm | StrOutputParser()

# Chain 2: Summarize explanation
summary_prompt = ChatPromptTemplate.from_template(
    "Summarize this in exactly 3 bullet points:\n\n{text}"
)

summary_chain = summary_prompt | llm | StrOutputParser()

topic = "LangChain"

detailed = explain_chain.invoke({"topic": topic})
summary = summary_chain.invoke({"text": detailed})

print("=== DETAILED ===")
print(detailed)

print("\n=== SUMMARY ===")
print(summary)