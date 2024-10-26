# TZOOTZ RESEARCH - Custom ComfyUI Node for EXR Downscaling
from .tzoootz_exr_node import TZOOTZ_EXRNode  # Import your custom node

# Register the TZOOTZ_EXR node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "TZOOTZ_EXR": TZOOTZ_EXRNode,  # Registering the TZOOTZ_EXR node
}

# Branding mappings for display names
NODE_DISPLAY_NAME_MAPPINGS = {
    "TZOOTZ_EXR": "TZOOTZ EXR Downscale | TZOOTZ RESEARCH",  # Branding the display name for your node
}
