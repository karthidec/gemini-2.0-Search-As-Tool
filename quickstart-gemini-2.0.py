import os
from google import genai

#to load .env key
from dotenv import find_dotenv
from dotenv import load_dotenv
env_file = find_dotenv(".env")
load_dotenv(env_file)
API_KEY = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=API_KEY)

response = client.models.generate_content(model="gemini-2.0-flash-exp", contents="what is the today market rate of tesla share?")

print(response.text)
