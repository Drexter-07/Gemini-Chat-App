from dotenv import load_dotenv
load_dotenv()
from google import genai
from google.genai import types
import os

api_keyy = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_keyy)

# response = client.models.generate_content(
#     model="gemini-2.0-flash", contents="Explain how AI works in a few words"
# )
# print(response.text)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents='what is 2+2'
)
print(response.text)