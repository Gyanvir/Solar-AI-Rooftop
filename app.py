
import streamlit as st
from PIL import Image
import numpy as np
import cv2

from src.api import download_satellite_image, generate_summary
from src.utils import preprocess_image, estimate_solar_metrics
from src.model import predict_rooftop_area, calculate_confidence

st.set_page_config(page_title="Solar Rooftop AI", layout="centered")

st.title("☀️ Solar Rooftop Analyzer")
st.write("Upload a satellite image or enter location coordinates to estimate solar potential and ROI.")

# Image Upload or Coordinates
option = st.radio("Choose Input Method", ["Upload Image", "Use Coordinates"])

if option == "Upload Image":
    uploaded_file = st.file_uploader("Upload satellite image (.png or .jpg)", type=["png", "jpg", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file).convert("RGB")
        image = image.resize((256, 256))
        st.image(image, caption="Uploaded Image", use_column_width=True)
        image_path = "data/uploaded.png"
        image.save(image_path)
elif option == "Use Coordinates":
    lat = st.number_input("Latitude", value=28.6139)
    lon = st.number_input("Longitude", value=77.2090)
    api_key = st.text_input("Google Maps API Key", type="password")
    if st.button("Download Satellite Image"):
        if api_key:
            image_path = download_satellite_image(lat, lon, api_key=api_key)
            image = Image.open(image_path).convert("RGB")
            st.image(image, caption="Satellite Image", use_column_width=True)
        else:
            st.warning("Please enter your API key.")

if "image_path" in locals():
    
    # image_array = preprocess_image(image_path)
    # mask = predict_rooftop_area(image_array)
    # area_estimate = round(mask.sum() * 0.35, 2)
    # confidence = calculate_confidence(mask)
    # image_np = np.array(image.resize((256, 256))).astype(np.uint8)
    # red_overlay = np.zeros_like(image_np)
    # red_overlay[mask] = [255, 0, 0]  # red where mask is True
    # blended = cv2.addWeighted(image_np, 0.7, red_overlay, 0.3, 0)
    # st.image(blended, caption="Rooftop Mask Overlay", use_container_width=True)
    
    # Convert mask to uint8 format
    mask_uint8 = (mask * 255).astype(np.uint8)
    # Find contours
    contours, _ = cv2.findContours(mask_uint8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw contours on the original image
    image_np = np.array(image.resize((256, 256))).copy()
    cv2.drawContours(image_np, contours, -1, (255, 0, 0), 2)  # Blue lines    
    # Display updated image with contours
    st.image(image_np, caption="Detected Rooftop Boundaries", use_container_width=True)

    # Calculations
    st.subheader("📊 Estimated Solar Metrics")
    st.write(f"**Estimated Rooftop Area:** {area_estimate} m²")
    st.write(f"**Detection Confidence:** {confidence}")
    metrics = estimate_solar_metrics(area_estimate)
    print("🚀 Debug metrics from code:")
    for k, v in metrics.items():
        print(f"{k}: {v}")
   
    for key, value in metrics.items():
        display_key = key.replace('_', ' ').capitalize()
        st.write(f"**{display_key}:** `{value}`")
    

    # Optional LLM output
    use_llm = st.checkbox("Get AI-generated recommendation")
    if use_llm:
        llm_api_key = st.text_input("OpenRouter API Key", type="password")
        if llm_api_key:
            with st.spinner("Generating..."):
                summary = generate_summary(area_estimate, "New Delhi", api_key=llm_api_key)
                st.subheader("💡 AI Recommendation")
                st.markdown(summary)
