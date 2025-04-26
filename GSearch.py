from dotenv import load_dotenv
load_dotenv()
from google import genai
import os
api_keyy = os.getenv("GEMINI_API_KEY")


client = genai.Client(api_key=api_keyy)

MODEL = 'gemini-2.0-flash'
search_tool = {'google_search': {}}

chat = client.chats.create(model=MODEL, config={'tools': [search_tool]})
r = chat.send_message('Today gold price in India and what is todays date?')
response = r.candidates[0].content.parts[0].text
print(response)