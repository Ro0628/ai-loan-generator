from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os
import uuid
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from data.models.Borrower import Borrower
from data.models.Property import Property
from data.models.Loan import Loan
from data.models.LoanStatus import LoanStatus
from data.models.LoanType import LoanType

# Set OpenAI API Key
# Load OpenAI API Key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API Key is missing! Set OPENAI_API_KEY in the environment.")

app = FastAPI()

# Initialize OpenAI LLM with API Key
llm = ChatOpenAI(model="gpt-4", openai_api_key=OPENAI_API_KEY)

class LoanRequest(BaseModel):
    user_prompt: str

import json

def generate_test_loan(user_prompt):
    """Uses LLM to convert user text into structured loan data."""
    
    prompt_template = """
    You are an AI Loan Origination System that converts natural language loan requests into structured JSON data.
    Convert the following user request into structured loan details:

    "{user_prompt}"

    Provide the response in **valid JSON format**, with these fields:
    - loan_type (e.g., "VA", "FHA", "Conventional", "Jumbo", "USDA")
    - term_years (e.g., 15, 30)
    - loan_amount
    - property_location (City, State)
    - underwriting_status (e.g., "pending", "underwriting", "approved", "rejected")
    - borrower_name
    """

    structured_response = llm.predict(prompt_template.format(user_prompt=user_prompt))

    # Convert LLM's text response to JSON
    try:
        structured_loan = json.loads(structured_response)  # ✅ Convert string to dictionary
    except json.JSONDecodeError:
        raise ValueError("LLM response is not valid JSON. Check model output.")

    return structured_loan


@app.post("/generate-loan/")
async def generate_loan(request: LoanRequest):
    """Processes a natural language loan request and returns structured test loan data."""

    structured_loan = generate_test_loan(request.user_prompt)

    # Convert AI response to structured Loan object
    loan = Loan(
        loan_type=LoanType(structured_loan["loan_type"]),
        term_years=structured_loan["term_years"],
        loan_amount=structured_loan["loan_amount"],
        borrower=Borrower("John", "Doe", 35, 90000, 750),
        property=Property("123 Main St", "Houston", "TX", "77001", 400000),
        status=LoanStatus(structured_loan["underwriting_status"])
    )

    return {
        "loan_id": str(uuid.uuid4()),
        "loan_details": loan.__repr__()
    }
