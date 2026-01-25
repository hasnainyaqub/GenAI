from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.tools import tool
import requests
from dotenv import load_dotenv
load_dotenv()

@tool 
def get_coversion_factor(base_currency: str, target_currency: str) -> float:
    """This function fetches the currency factor between a given  currency and target currency"""
    url = f'https://v6.exchangerate-api.com/v6/18c8f9820ba7d32edff8e295/pair/{base_currency}/{target_currency}'

    response = requests.get(url)
    return response.json()

@tool
def convert(base_currency_value: int, conversion_rate: float) -> float:
    """This function converts the base currency to target currency"""
    return base_currency_value * conversion_rate

result = convert.invoke({'base_currency_value': 10, 'conversion_rate': 85})
print(result)