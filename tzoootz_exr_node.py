import numpy as np
from PIL import Image
import torch

class TZOOTZ_EXRNode:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "scale_factor": ("FLOAT", {"default": 0.5, "min": 0.1, "max": 1.0, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "downscale_exr"
    CATEGORY = "image"
    
    def downscale_exr(self, image, scale_factor):
        # Convert the tensor to a PIL image
        image = Image.fromarray(np.clip(255.0 * image.cpu().numpy().squeeze(), 0, 255).astype(np.uint8))
        
        # Calculate new size
        width, height = image.size
        new_size = (int(width * scale_factor), int(height * scale_factor))
        
        # Resize the image using LANCZOS (formerly ANTIALIAS)
        downscaled_image = image.resize(new_size, Image.Resampling.LANCZOS)
        
        # Convert the downscaled image back to a tensor
        downscaled_image = torch.from_numpy(np.array(downscaled_image).astype(np.float32) / 255.0).unsqueeze(0)
        
        return (downscaled_image,)

# Register the node with ComfyUI
NODE_CLASS_MAPPINGS = {
    "TZOOTZ_EXR": TZOOTZ_EXRNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TZOOTZ_EXR": "TZOOTZ EXR Downscale | TZOOTZ RESEARCH",
}
