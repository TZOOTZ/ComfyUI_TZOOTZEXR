ComfyUI_TZOOTZEXR
ComfyUI EXR Node by TZOOTZ Research 2024®

Overview
The ComfyUI_TZOOTZEXR node extends ComfyUI with HDR EXR file support, ideal for digital artists and experimental projects. This node enables loading EXR files and precision downscaling, preserving highlights and floating-point accuracy for visual fidelity.

Features
EXR File Loading: Import EXR files with full HDR data.
Floating-Point Precision: Downscale images without losing high-brightness details.
Custom Scaling Factor: Set your desired downscale level.
Seamless Integration: Fits within ComfyUI node workflows.
Requirements
Required libraries are listed in requirements.txt:

OpenEXR
Imath
Pillow
numpy
Installation
Clone the repository to your ComfyUI custom nodes directory: git clone https://github.com/yourusername/ComfyUI_TZOOTZEXR.git

Navigate to the ComfyUI directory: cd C:\Users\Filthy\Desktop\IA LAB\ComfyUI_windows_portable

Install dependencies: pip install -r custom_nodes/ComfyUI_TZOOTZEXR/requirements.txt

Usage
In ComfyUI, select TZOOTZ_EXRNode to load and downscale EXR files. Set the scaling factor to achieve your desired resolution while preserving HDR details.

About TZOOTZ Research 2024®
TZOOTZ Research creates tools for digital art and experimental visuals. This EXR node aligns with our mission to provide artists with precision-focused tools for creative expression.

License
This project is licensed under the MIT License. See the LICENSE file for more information.
