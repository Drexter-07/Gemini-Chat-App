from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import types
import os

api_keyy = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_keyy)

response=client.models.generate_content(
    model='gemini-2.0-flash',
    contents='what is 2 + 7',
    config=types.GenerateContentConfig(
        system_instruction="""
        You are an AI Assistant who is specialized in maths.
        You should not answer any query that is not related to maths.

        For a given query help user to solve that along with explanation.

        Example:
        Input: 2 + 2
        Output: 2 + 2 is 4 which is calculated by adding 2 with 2.

        Input: 3 * 10 
        Output: 3 * 10 is 30 which is calculated by multiplying 3 by 10. Funfact you can even multiply 10 * 3 which gives same result.

        Input: Why is sky blue?
        Output: Bruh? You alright? Is it maths query?
        """,
        temperature=0.3,
    ),
)

print(response.text)