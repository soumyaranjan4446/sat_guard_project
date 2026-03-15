import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import os

# --- Page Configuration ---
st.set_page_config(page_title="SAT-GUARD | DefenseVision", layout="wide")

# --- Load Model ---
@st.cache_resource
def load_model():
    # Point this to your trained model path
    model_path = 'models/best.pt'
    
    # Fallback to pre-trained if custom model isn't trained yet
    if not os.path.exists(model_path):
        st.warning(f"Custom model not found at {model_path}. Loading base model for demonstration.")
        return YOLO('yolov8n-obb.pt')
    
    return YOLO(model_path)

model = load_model()

# --- Dashboard UI ---
st.title("🛰️ SAT-GUARD: AI-Based Satellite Surveillance")
st.markdown("### Military Asset Detection System using Rotated Bounding Boxes")

# Sidebar
st.sidebar.header("System Controls")
confidence_threshold = st.sidebar.slider("Confidence Threshold", 0.0, 1.0, 0.25, 0.05)

# Main layout
col1, col2 = st.columns(2)

uploaded_file = st.sidebar.file_uploader("Upload Satellite Imagery (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the uploaded image
    image = Image.open(uploaded_file)
    
    with col1:
        st.subheader("Original Satellite Feed")
        st.image(image, use_container_width=True)
    
    # Inference button
    if st.sidebar.button("Run Threat Detection", type="primary"):
        with st.spinner("Analyzing satellite feed..."):
            # Run YOLOv8 OBB inference
            results = model.predict(source=image, conf=confidence_threshold)
            
            # Plot results on image
            res_image = results[0].plot()
            
            with col2:
                st.subheader("Detected Assets")
                st.image(res_image, use_container_width=True)
                
            # --- Extract and display intelligence data ---
            st.divider()
            st.subheader("Intelligence Report")
            
            detections = results[0].obb # Rotated boxes
            
            if detections is not None and len(detections) > 0:
                st.success(f"{len(detections)} potential targets detected.")
                
                # Extract classes and confidences
                classes = detections.cls.cpu().numpy()
                confs = detections.conf.cpu().numpy()
                names = model.names
                
                # Display metrics in a clean format
                for i in range(len(classes)):
                    class_name = names[int(classes[i])]
                    confidence = confs[i] * 100
                    st.markdown(f"**Target {i+1}:** `{class_name.upper()}` | **Confidence:** `{confidence:.2f}%`")
            else:
                st.info("No military assets detected in this sector.")
else:
    st.info("Please upload a satellite image from the sidebar to begin surveillance.")