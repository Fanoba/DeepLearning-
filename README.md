# DeepLearning-
Poryecto de Deep learning usando un modelo CNN y una pagina web 
# 🎨 Clasificador de Pintores con Deep Learning (MobileNetV2)

Este proyecto implementa un modelo de Deep Learning capaz de clasificar obras de arte según su autor utilizando únicamente características visuales. El modelo utiliza **MobileNetV2 con Transfer Learning** entrenado sobre un subconjunto de pintores seleccionados del dataset *WikiArt*, procesado y filtrado para mejorar la precisión y evitar problemas de sobreajuste.

---

## 📌 Descripción General

El objetivo del proyecto es entrenar un clasificador multiclase que, dada una imagen de una pintura, determine a cuál artista pertenece.  
Dado que el dataset original cuenta con 129 artistas y alrededor de 91,000 imágenes, se decidió reducir el problema para mejorar la calidad del aprendizaje:

- Se seleccionaron los **10 pintores con mayor número de imágenes**.
- Se aplicó **data augmentation** para compensar la reducción de datos.
- Se empleó **transfer learning** para entrenar de manera eficiente sin requerir grandes recursos computacionales.

El modelo final fue entrenado en entorno local utilizando TensorFlow 2.16.1.

---

## 🗂️ Estructura del Dataset

El dataset original incluye cuatro columnas:

- **Artista** (129 clases)
- **Imagen** (≈91,000 obras)
- **Género pictórico**
- **Estilo pictórico**

Durante la exploración se detectaron:

- Imágenes corruptas → eliminadas completamente  
- Carpetas residuales como `.ipynb_checkpoints` → removidas  
- Formatos no válidos → descartados  

Luego, para el entrenamiento final:

- Se seleccionaron **10 artistas** más representados.

Referencias 
•	HugGAN Community. (2025, June 6). wikiart. Huggingface.co. https://huggingface.co/datasets/huggan/wikiart?
