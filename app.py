import streamlit as st
from PIL import Image
import time
import random

st.title("🪨 Mineral Identifier Test")
st.write("Testing mode - will show different random results")

# Sample minerals for testing
minerals = ["Quartz", "Feldspar", "Calcite", "Mica", "Hematite", "Pyrite", "Gypsum"]

uploaded_file = st.file_uploader("Upload photo", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, width=300)
    
    if st.button("Test Analysis"):
        with st.spinner("Analyzing..."):
            # Simulate AI thinking
            time.sleep(2)
            
            # Generate different random results each time
            random.shuffle(minerals)
            
            st.success("✅ Analysis Complete!")
            st.subheader("Test Results:")
            
            for i in range(3):
                confidence = random.randint(60, 95)
                st.write(f"**{i+1}. {minerals[i]}** - {confidence}% confidence")
        
        st.info("This is a test mode. Enable real AI with API key for actual analysis.")