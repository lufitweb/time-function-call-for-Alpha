from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from datetime import datetime
import os
import pytz

groq = ChatGroq(api_key=os.environ.get("GROQ_API_KEY"))

@tool
def get_current_time(location="UTC"):
    """Get the current time for a specific location."""
    try:
        tz = pytz.timezone(location)
        current_time = datetime.now(tz)
        return current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Unknown time zone: {location}. Please provide a valid time zone or country name."

prompt = ChatPromptTemplate.from_messages([
    
])

output_parser = StrOutputParser()

chain = prompt | groq | output_parser

def get_time_response(user_input):
    location = "UTC" 
    if "in" in user_input.lower():
        location = user_input.lower().split("in")[-1].strip()
    
    time_result = get_current_time.invoke(location)
    
    response = chain.invoke({
        "input": user_input,
        "time_result": time_result
    })
    return response

if __name__ == "__main__":
    user_query = "What time is it in Tokyo?"
    result = get_time_response(user_query)
    print(result)