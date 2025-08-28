
import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms

# Load the pretrained model (assumes model is saved locally as 'rock_model.pt')
@st.cache_resource
def load_model():
    model = torch.load("rock_model.pt", map_location=torch.device('cpu'))
    model.eval()
    return model

model = load_model()

# Define class names (example from GitHub repo)
class_names = ["Aphanitic Basalt", "Volcanic Tuff", "Andesite", "Volcanic Scoria", "Vesicular Basalt", "Granodiorite", "Gabbro", "Limestone", "Sandstone", "Shale", "Slate", "Marble", "Quartzite", "Schist", "Phyllite", "Conglomerate", "Breccia", "Dolomite", "Rhyolite"]

# Define image preprocessing
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

# Streamlit UI
st.title("Rock Formation Identifier")

uploaded_file = st.file_uploader("Upload an image of a rock formation", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Identifying rock type...")

    image_tensor = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(image_tensor)
        _, predicted = torch.max(outputs, 1)
        predicted_class = class_names[predicted.item()]

    st.success(f"Predicted Rock Type: {predicted_class}")
