import openai
#from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
openai.api_key = os.getenv("API_KEY")

prompt1 = "develop and deploy a web app"

def ask_openai(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo", 
            messages=[
                {"role": "system", "content": "You are an expert coder and web developer."}, 
                {"role": "user", "content": prompt}  
            ],
            temperature=0.7  
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

response = ask_openai(prompt1)
print(response)