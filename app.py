
import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms

st.title("Rock Formation Identifier")

uploaded_file = st.file_uploader("Upload an image of a rock formation", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("
Identifying rock type...")

    # Placeholder model and classes
    class_names = ["Igneous", "Sedimentary", "Metamorphic"]

    # Dummy prediction logic (replace with actual model)
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    image_tensor = transform(image).unsqueeze(0)

    # Simulate prediction
    prediction = torch.randint(0, len(class_names), (1,)).item()
    predicted_class = class_names[prediction]

    st.success(f"Predicted Rock Type: {predicted_class}")
