from dotenv import load_dotenv
import os
from google import genai

# 1. Load the variables defined in .env 
load_dotenv()

# 2. Usage of the key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("The variable GEMINI_API_KEY isn't defined yet.")

# 3. Use the key for the program
client = genai.Client(api_key=api_key)

# 4. Creation of the menu to execute the program
while True:
    print("Write 'exit' if you want to close the program.")
    prompt = input("Ask to Gemini: ")
    print("Generating response...")

    if prompt.lower() == "exit":
        print("Closing the program...")
        break
    
    response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = prompt )
    print("Response from Gemini: ", response.text)