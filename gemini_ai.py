# from gemini import GenerativeModel
import google.generativeai as genai
import os

genai.configure(api_key="AIzaSyAH7Mv_GEHx7nGj_-SmLGI6UaI_z3NlKEE")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("give me a story about laptop", stream=True)
for chunk in response:
    print(chunk.text)
    print("_" * 80)