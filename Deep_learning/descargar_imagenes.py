import os
import urllib.request
import numpy as np
from PIL import Image

# =======================
# 🐾 Lista completa de animales
# =======================
animals = [
    "antelope", "badger", "bat", "bear", "bee", "beetle", "bison", "boar",
    "butterfly", "cat", "caterpillar", "chimpanzee", "cockroach", "cow", "coyote",
    "crab", "crow", "deer", "dog", "dolphin", "donkey", "dragonfly", "duck",
    "eagle", "elephant", "flamingo", "fly", "fox", "goat", "goldfish", "goose",
    "gorilla", "grasshopper", "hamster", "hare", "hedgehog", "hippopotamus",
    "hornbill", "horse", "hummingbird", "hyena", "jellyfish", "kangaroo", "koala",
    "ladybugs", "leopard", "lion", "lizard", "lobster", "mosquito", "moth",
    "mouse", "octopus", "okapi", "orangutan", "otter", "owl", "ox", "oyster",
    "panda", "parrot", "pelecaniformes", "penguin", "pig", "pigeon", "porcupine",
    "possum", "raccoon", "rat", "reindeer", "rhinoceros", "sandpiper", "seahorse",
    "seal", "shark", "sheep", "snake", "sparrow", "squid", "squirrel", "starfish",
    "swan", "tiger", "turkey", "turtle", "whale", "wolf", "wombat", "woodpecker", "zebra"
]

# =======================
# 📁 Configuración de carpetas
# =======================
os.makedirs("data/animals_3", exist_ok=True)
save_root = "data/animals_3"

# =======================
# 🚀 Descarga y conversión
# =======================
for animal in animals:
    try:
        print(f"📥 Descargando {animal} ...")
        url = f"https://storage.googleapis.com/quickdraw_dataset/full/numpy_bitmap/{animal}.npy"
        path = f"data/{animal}.npy"

        # Descargar si no existe
        if not os.path.exists(path):
            urllib.request.urlretrieve(url, path)

        # Cargar y convertir a imágenes RGB
        data = np.load(path)
        save_dir = os.path.join(save_root, animal)
        os.makedirs(save_dir, exist_ok=True)

        for i, img_array in enumerate(data[:1000]):  # puedes cambiar 1000 → más si quieres
            img = Image.fromarray(img_array.reshape(28, 28))
            img = img.convert("RGB")  # pasa de escala de grises a RGB
            img.save(os.path.join(save_dir, f"{animal}_{i}.png"))

        print(f"✅ {animal}: {len(os.listdir(save_dir))} imágenes guardadas")

    except Exception as e:
        print(f"⚠️ No se pudo descargar {animal}: {e}")

print("🎉 Descarga y conversión completa.")
