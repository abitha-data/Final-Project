import streamlit as st
from utils import load_model, load_image, detect_and_draw

# Page config
st.set_page_config(
    page_title="Road Damage Detection",
    page_icon="🚧",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    h1 {
        text-align: center;
        color: #00FFAA;
    }
    .stButton>button {
        background-color: #00FFAA;
        color: black;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>🚧 Road Damage Detection System</h1>", unsafe_allow_html=True)
st.write("### YOLOv8 + MobileNet Deep Learning Model")

# Load model
model = load_model()

# Upload
uploaded_file = st.file_uploader("📤 Upload Road Image", type=["jpg","png","jpeg"])

if uploaded_file:

    image = load_image(uploaded_file)
    output_image, detections = detect_and_draw(model, image)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📷 Original Image")
        st.image(image, channels="BGR", use_container_width=True)

    with col2:
        st.markdown("### 🔍 Detection Result")
        st.image(output_image, channels="BGR", use_container_width=True)

    st.markdown("---")

    st.markdown("## 📊 Detection Summary")

    if len(detections) == 0:
        st.warning("⚠ No damage detected")
    else:
        for i, (label, conf) in enumerate(detections):
            st.success(f"✔ Damage {i+1}: {label} ({conf:.2f})")