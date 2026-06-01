import os
from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict

from langgraph.graph import StateGraph, END
from langchain_groq import ChatGroq


# ----------------------
# State Definition
# ----------------------

class BMIState(TypedDict):
    height_cm: float
    weight_kg: float
    bmi: float
    category: str
    advice: str


# ----------------------
# LLM
# ----------------------

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY not found. Set environment variable or create a .env file."
    )

llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile",
    temperature=0,
)


# ----------------------
# Node 1: Calculate BMI
# ----------------------

def calculate_bmi(state: BMIState):

    height_m = state["height_cm"] / 100

    bmi = state["weight_kg"] / (height_m ** 2)

    state["bmi"] = round(bmi, 1)

    return state


# ----------------------
# Node 2: Classify BMI
# ----------------------

def classify_bmi(state: BMIState):

    bmi = state["bmi"]

    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal Weight"
    elif bmi < 30:
        category = "Overweight"
    elif bmi < 35:
        category = "Obesity Class I"
    elif bmi < 40:
        category = "Obesity Class II"
    else:
        category = "Obesity Class III"

    state["category"] = category

    return state


# ----------------------
# Node 3: Generate Advice
# ----------------------

def generate_advice(state: BMIState):

    prompt = f"""
    A person has:

    BMI: {state['bmi']}
    Category: {state['category']}

    Give 3 concise health recommendations.
    """

    response = llm.invoke(prompt)

    state["advice"] = response.content

    return state


# ----------------------
# Build Graph
# ----------------------

graph = StateGraph(BMIState)

graph.add_node("calculate_bmi", calculate_bmi)
graph.add_node("classify_bmi", classify_bmi)
graph.add_node("generate_advice", generate_advice)

graph.set_entry_point("calculate_bmi")

graph.add_edge("calculate_bmi", "classify_bmi")
graph.add_edge("classify_bmi", "generate_advice")
graph.add_edge("generate_advice", END)

app = graph.compile()


# ----------------------
# Run
# ----------------------

result = app.invoke(
    {
        "height_cm": 170,
        "weight_kg": 95
    }
)

print("\n=== BMI REPORT ===")
print(f"BMI       : {result['bmi']}")
print(f"Category  : {result['category']}")
print("\nAdvice:")
print(result["advice"])