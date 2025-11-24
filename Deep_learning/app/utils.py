
from dotenv import load_dotenv
from groq import Groq
import tensorflow as tf
import numpy as np
from PIL import Image
import os
import requests
import json

# ====== Cargar .env ======
env_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".env"))
load_dotenv(env_path)

load_dotenv()
GROQ_API_KEY = os.getenv("API_KEY")

client = Groq(api_key=GROQ_API_KEY)
if GROQ_API_KEY is None:
    raise ValueError("❌ ERROR: NO se encontró OPENAI_API_KEY en el archivo .env")


# ====== Cargar modelo ======
MODEL_PATH = "models/wikiart_mobilenet.h5"
model = tf.keras.models.load_model(MODEL_PATH)
IMG_SIZE = 224
# ====== Cargar clases ======
# Debes generar un archivo artists.txt con 1 artista por línea

with open("models/class_names.json", "r") as f:
    CLASS_NAMES = json.load(f)

len(CLASS_NAMES) == model.output_shape[1]

def predict_artist(image: Image.Image):
    image = image.convert("RGB")
    image = image.resize((IMG_SIZE, IMG_SIZE))

    img_array = np.array(image, dtype=np.float32) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)

    idx = np.argmax(preds)
    confidence = float(preds[0][idx])

    # DEVOLVER SOLO 2 VALORES
    return CLASS_NAMES[idx], confidence



def get_artist_info_from_groq(artist_name):
    """
    Consulta la API de Groq usando openai-compatible endpoint.
    """
    if not GROQ_API_KEY:
        return "⚠️ Error: GROQ_API_KEY no está configurada."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {GROQ_API_KEY}"
    }

    data = {
        "model": "openai/gpt-oss-20b",
        "messages": [
            {
                "role": "user",
                "content": f"Dame una biografía breve y clara del artista {artist_name}. Incluye: estilo, época e importancia."
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "choices" in result:
            return result["choices"][0]["message"]["content"]

        return f"⚠️ Error en respuesta de Groq: {result}"

    except Exception as e:
        return f"⚠️ Error al consultar Groq: {e}"

def format_biography(text: str) -> str:
    return f"""
<div class="card">
  <h3>📚 Biografía del artista</h3>
  <p style="line-height: 1.6; font-size: 1.1rem;">
    {text.replace("\n", "<br>")}
  </p>
</div>
"""
