import requests
from PIL import Image
from io import BytesIO
import os
# import requests

def generate_summary(area_sq_m, location, api_key):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert in solar panel deployment in India."},
            {"role": "user", "content": f"""Given a rooftop area of {area_sq_m:.2f} square meters in {location}, estimate the solar panel capacity in kW, expected energy output, and ROI over 10 years under average Indian conditions."""}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]

def download_satellite_image(lat, lon, zoom=20, size="640x640", api_key="AIzaSyDCBkUcxib2ZhgShlrYAowboUCKyg-f2-A"):
    url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lon}&zoom={zoom}&size={size}&maptype=satellite&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        image = Image.open(BytesIO(response.content))
        os.makedirs("data", exist_ok=True)
        filename = f"data/satellite_{lat}_{lon}.png"
        image.save(filename)
        return filename
    else:
        raise Exception(f"Failed to fetch image: {response.status_code}")