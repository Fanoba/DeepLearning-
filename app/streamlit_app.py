import streamlit as st
from PIL import Image
from utils import predict_artist, get_artist_info_from_groq, format_biography  # 👈 Añadimos format_biography

# ====== Cargar estilos ======
with open("app/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# ====== Encabezado ======
st.markdown("<h1 class='title'>🎨 Conoce a tu Artista Interior</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Sube un dibujo o pintura y descubre a qué artista famoso se parece más tu estilo.</p>", unsafe_allow_html=True)

# ===============================================================
# 📤 UPLOAD
# ===============================================================
uploaded_file = st.file_uploader("📁 Sube tu imagen", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Mostrar imagen
    st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
    st.image(uploaded_file, caption="🖼️ Tu obra", use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Predicción del artista
    with st.spinner("🔍 Analizando estilo artístico con IA..."):
        image = Image.open(uploaded_file)
        artist_name, confidence = predict_artist(image)

    st.markdown(
        f"""
        <div class='glass-card result-card'>
            <h2>🧠 Artista más probable:</h2>
            <p class='artist-name'>{artist_name}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===============================================================
    # 📚 Información del artista desde Groq
    # ===============================================================
    with st.spinner("📚 Consultando biografía del artista..."):
        raw_info = get_artist_info_from_groq(artist_name)

    formatted_info = format_biography(raw_info)

    st.markdown(formatted_info, unsafe_allow_html=True)

# ===============================================================
# 🔄 Botón de reinicio
# ===============================================================
if st.button("🔄 Reiniciar"):
    st.experimental_rerun()
