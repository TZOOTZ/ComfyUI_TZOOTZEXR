# ComfyUI_TZOOTZEXR
ComfyUI EXR Node by TZOOTZ Research 2024®

## Overview
The **ComfyUI_TZOOTZEXR** node extends *ComfyUI* with HDR EXR file support, ideal for digital artists and experimental projects. This node enables loading EXR files and precision downscaling, preserving highlights and floating-point accuracy for visual fidelity.

## Features
- **EXR File Loading:** Import EXR files with full HDR data.
- **Floating-Point Precision:** Downscale images without losing high-brightness details.
- **Custom Scaling Factor:** Set your desired downscale level.
- **Seamless Integration:** Fits within ComfyUI node workflows.

## Requirements
Required libraries are listed in `requirements.txt`:

- OpenEXR
- Imath
- Pillow
- numpy

## Installation
1. **Clone the repository** to your ComfyUI custom nodes directory:
   ```bash
   git clone https://github.com/yourusername/ComfyUI_TZOOTZEXR.git
