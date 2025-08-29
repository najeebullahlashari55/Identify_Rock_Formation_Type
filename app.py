import streamlit as st
import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision import models, transforms
from PIL import Image
import matplotlib.pyplot as plt

# ✅ Define your rock formation class labels
CLASS_LABELS = [
    "Sandstone",
    "Limestone",
    "Shale",
    "Dolomite",
    "Conglomerate"
]

# ✅ Load model with automatic pretrained weights
@st.cache_resource
def load_model():
    model = models.mobilenet_v3_large(pretrained=True)
    
    # Replace final classifier for your specific number of classes
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features, len(CLASS_LABELS))
    
    model.eval()
    return model

# Preprocessing for uploaded image
def preprocess_image(image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406], 
            std=[0.229, 0.224, 0.225]
        )
    ])
    return transform(image).unsqueeze(0)

# --- Streamlit UI ---
st.title("🪨 Rock Formation Type Identifier")
st.write("This is a demo app using a pretrained MobileNetV3 model. For production use, you would need to train the model on your specific rock dataset.")

uploaded_file = st.file_uploader("Upload a rock image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        model = load_model()
        input_tensor = preprocess_image(image)

        with torch.no_grad():
            outputs = model(input_tensor)
            probabilities = F.softmax(outputs, dim=1)[0]
            conf, predicted = torch.max(probabilities, 0)

        predicted_class = CLASS_LABELS[predicted.item()]
        confidence = conf.item() * 100

        st.write(f"### ✅ Predicted Class: {predicted_class} ({confidence:.2f}% confidence)")

        # Show all class probabilities
        st.subheader("Class Probabilities")
        for i, prob in enumerate(probabilities):
            st.write(f"- {CLASS_LABELS[i]}: {prob.item()*100:.2f}%")

        # Bar chart
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.bar(CLASS_LABELS, [p.item()*100 for p in probabilities])
        ax.set_ylabel("Confidence (%)")
        ax.set_title("Prediction Probabilities")
        plt.xticks(rotation=30)
        st.pyplot(fig)
        
    except Exception as e:
        st.error(f"Error processing image: {str(e)}")
else:
    st.info("Please upload an image to get a prediction.")