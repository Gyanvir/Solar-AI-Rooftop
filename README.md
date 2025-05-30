# Solar Rooftop AI Assistant

This tool helps identify usable rooftop space from satellite imagery and estimate the solar panel capacity, energy output, and ROI for Indian rooftops.

## Features
- Upload image or fetch via lat/lon (Google Maps API)
- Rooftop segmentation using simulated brightness threshold
- Energy & ROI estimation using realistic assumptions
- Optional GPT-based summary via OpenRouter or OpenAI

## Installation
```bash
git clone https://github.com/gyanvir/Solar-AI-Rooftop.git
cd solar-ai-intern
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt