from src.api import download_satellite_image, generate_summary
from src.utils import preprocess_image
from src.model import predict_rooftop_area, calculate_confidence
from src.utils import estimate_solar_metrics

# Step 1: Download image
image_path = download_satellite_image(28.6139, 77.2090, api_key="AIzaSyDCBkUcxib2ZhgShlrYAowboUCKyg-f2-A")

# Step 2: Preprocess image
img_array = preprocess_image(image_path)

# Step 3: Predict rooftop area
mask = predict_rooftop_area(img_array)

# Step 4: Calculate area (assume each pixel = 0.25 sqm for example)
area_estimate = mask.sum() * 0.25
confidence = calculate_confidence(mask)

# Step 5: Generate insight
summary = generate_summary(area_estimate, "New Delhi", api_key="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")

print(f"Estimated Area: {area_estimate:.2f} m^2")
print(f"Confidence: {confidence}")
print("\nRecommendation:\n", summary)

metrics = estimate_solar_metrics(area_estimate)
print("\n[Calculated Metrics]")
for k, v in metrics.items():
    print(f"{k.replace('_', ' ').capitalize()}: {v}")