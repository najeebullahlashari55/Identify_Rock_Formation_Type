import torch
import torch.nn as nn
from torchvision import models

@st.cache_resource
def load_model():
    num_classes = 5  # <-- change this
    model = models.mobilenet_v3_large()
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features, num_classes)

    state_dict = torch.load("rock_model_state.pt", map_location="cpu")
    model.load_state_dict(state_dict)
    model.eval()
    return model
