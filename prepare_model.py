import torch
import torch.nn as nn
from torchvision import models

def prepare_model(num_classes=5):
    """
    Prepares MobileNetV3 Large with pretrained weights and
    saves it as rock_model_state.pt (state_dict only).
    """

    print("🔄 Loading pretrained MobileNetV3...")
    model = models.mobilenet_v3_large()

    # Load pretrained weights from the file you uploaded
    state_dict = torch.load("mobilenet_v3_large.pth", map_location="cpu")
    model.load_state_dict(state_dict)

    # Replace the final classification layer with custom classes
    in_features = model.classifier[3].in_features
    model.classifier[3] = nn.Linear(in_features, num_classes)

    # Save only the state_dict (safe to load later)
    torch.save(model.state_dict(), "rock_model_state.pt")
    print("✅ Saved rock_model_state.pt successfully!")

if __name__ == "__main__":
    # Change this number to match your dataset’s rock formation classes
    prepare_model(num_classes=5)
