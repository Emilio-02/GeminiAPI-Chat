from dotenv import load_dotenv
import os
from google import genai

# 1. Carga las variables definidas en .env
load_dotenv()

# 2. Recupera la clave
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise RuntimeError("La variable GEMINI_API_KEY no está definida.")

# 3. Usa la clave al instanciar el cliente
client = genai.Client(api_key=api_key)

while True:
    print("Escribe 'salir' para cerrar el programa.")
    prompt = input("Preguntale a Gemini: ")
    print("Generando respuesta...")

    if prompt.lower() == "salir":
        print("saliendo...")
        break
    
    response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = prompt )
    print("Respuesta de Gemini: ", response.text)