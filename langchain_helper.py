from secret_key import openapi_key
from operator import itemgetter
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda
from langchain_openai import ChatOpenAI
import os

# Load environment variables from .env
os.environ["OPENAI_API_KEY"] = openapi_key

# Define prompt templates
prompt1 = ChatPromptTemplate.from_template("What is a good name for a restaurant that sells {cuisine} food? Please return just one name please")
prompt2 = ChatPromptTemplate.from_template("What would be a good menu for a restaurant called {restaurant_name}?")

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4")


# Create chains
chain1 = prompt1 | model | StrOutputParser()

chain2 = (
    {"restaurant_name": chain1}
    | prompt2
    | model
    | StrOutputParser()
)

# Function to invoke the chain
def chain_function(cuisine):
    if not isinstance(cuisine, str):
        raise TypeError("Expected cuisine to be a string.")
    
    # Get restaurant name separately to handle the input for menu generation
    restaurant_name_response = chain1.invoke({"cuisine": cuisine})
    restaurant_name = restaurant_name_response.strip()

    # Generate menu based on restaurant name
    menu_response = chain2.invoke({"cuisine": cuisine, "restaurant_name": restaurant_name})
    menu = menu_response.strip()

    return {"restaurant_name": restaurant_name, "menu": menu}

# Example usage
if __name__ == "__main__":
    cuisine_input = "Spanish"  # Ensure the input is a string
    response = chain_function(cuisine_input)
    print("Restaurant Name:", response['restaurant_name'])
    print("Menu:", response['menu'])
