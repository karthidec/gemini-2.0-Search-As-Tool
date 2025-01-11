import os
from google import genai

#to load .env key
from dotenv import find_dotenv
from dotenv import load_dotenv
env_file = find_dotenv(".env")
load_dotenv(env_file)
API_KEY = os.getenv("GOOGLE_API_KEY")

from google import genai
from google.genai.types import Tool, GenerateContentConfig, GoogleSearch

client = genai.Client()
model_id = "gemini-2.0-flash-exp"

google_search_tool = Tool(
    google_search = GoogleSearch()
)

response = client.models.generate_content(
    model=model_id,
    contents="what is the today market rate of tesla share?",
    config=GenerateContentConfig(
        tools=[google_search_tool],
        response_modalities=["TEXT"],
    )
)

for each in response.candidates[0].content.parts:
    print(each.text)
