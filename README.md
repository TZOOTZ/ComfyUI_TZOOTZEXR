ComfyUI_TZOOTZEXR
ComfyUI EXR Node by TZOOTZ Research 2024®

Overview
The ComfyUI_TZOOTZEXR node empowers ComfyUI with high-dynamic range (HDR) EXR file support, designed for digital artists and experimental projects. By enabling EXR file loading and precise downscaling, the node preserves highlights and floating-point accuracy in images, perfect for workflows where visual fidelity is essential.

Features
EXR File Loading: Import EXR files directly into ComfyUI, retaining full HDR data.
Floating-Point Precision: Downscale images without losing high-brightness details.
Custom Scaling Factor: Set your desired downscale level for flexible resolution management.
Seamless Integration: Operates within the ComfyUI node structure for easy workflow inclusion.
Requirements
This node requires a few essential libraries to handle EXR and image processing tasks. Install them from requirements.txt:

plaintext
Copy code
OpenEXR
Imath
Pillow
numpy
These libraries ensure that the EXR handling and downscaling processes are fully functional.

Installation
Clone the repository to your ComfyUI custom nodes directory:

bash
Copy code
git clone https://github.com/yourusername/ComfyUI_TZOOTZEXR.git
Navigate to the ComfyUI directory:

bash
Copy code
cd C:\Users\Filthy\Desktop\IA LAB\ComfyUI_windows_portable
Install dependencies:

bash
Copy code
pip install -r custom_nodes/ComfyUI_TZOOTZEXR/requirements.txt
Usage
In ComfyUI, select the TZOOTZ_EXRNode to load and downscale EXR files.
Set the scaling factor to achieve the desired resolution while maintaining HDR integrity.
Review your EXR images in ComfyUI, applying additional processing as needed.
About TZOOTZ Research 2024®
TZOOTZ Research is committed to pushing the boundaries of digital and experimental art through innovative tools and visual research. This EXR node aligns with our mission to provide artists with precision-focused tools to express and realize creative ideas.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
