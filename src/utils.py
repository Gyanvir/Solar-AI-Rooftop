from PIL import Image
import numpy as np

def preprocess_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = image.resize((256, 256))
    image_array = np.array(image) / 255.0
    return image_array

def estimate_solar_metrics(area_sq_m):
    # Constants (can be adjusted)
    panel_efficiency = 0.18  # 18%
    solar_irradiation = 5    # kWh/m²/day
    days_per_year = 365
    electricity_price = 0.1  # USD/kWh
    installation_cost_per_kw = 1250
    #  Debug prints
    print("⚙️ DEBUG VALUES:")
    print(f"Area: {area_sq_m}")
    print(f"Panel efficiency: {panel_efficiency}")
    print(f"Irradiation: {solar_irradiation}")
    # 1. Capacity in kW
    capacity_kw = area_sq_m * panel_efficiency * solar_irradiation
    print(f"Capacity (kW): {capacity_kw}")

    # 2. Annual energy output in kWh
    annual_output_kwh = capacity_kw * days_per_year

    # 3. Installation cost
    installation_cost = capacity_kw * installation_cost_per_kw

    # 4. Annual savings
    annual_savings = annual_output_kwh * electricity_price

    # 5. 10-year ROI
    total_savings = annual_savings * 10
    roi_percent = ((total_savings - installation_cost) / installation_cost) * 100

    return {
        "capacity_kw": round(capacity_kw, 2),
        "annual_output_kwh": round(annual_output_kwh, 2),
        "installation_cost_usd": round(installation_cost, 2),
        "annual_savings_usd": round(annual_savings, 2),
        "roi_10yr_percent": round(roi_percent, 2)
    }