# ☀️ Solar AI Rooftop Assistant 

An AI-powered tool designed to analyze satellite imagery for rooftop solar potential, providing estimates on panel capacity, energy output, and return on investment (ROI) for locations in India.

---

## 📦 Project Setup Instructions

### Prerequisites

* Python 3.8 or higher
* pip (Python package installer)
* Virtual environment tool (optional but recommended)

### Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/Gyanvir/Solar-AI-Rooftop.git
   cd Solar-AI-Rooftop
   ```

2. **Set Up Virtual Environment (Optional)**

   ```bash
   python -m venv venv
   # Activate the virtual environment
   # On Windows:
   venv\Scripts\activate
   # On Unix or MacOS:
   source venv/bin/activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   streamlit run app.py
   ```

   Access the application at `http://localhost:8501` in your web browser.

---

## 🛠️ Implementation Documentation

### Project Structure

```
Solar-AI-Rooftop/
├── app.py                 # Streamlit application entry point
├── test_run.py            # Script for testing functionalities
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # MIT License
├── data/                  # Directory for input/output data
└── src/                   # Source code modules
    ├── api.py             # Handles API interactions
    ├── model.py           # Contains model-related functions
    └── utils.py           # Utility functions for calculations
```

### Core Components

* **Image Upload & Processing**: Users can upload satellite images or fetch them using latitude and longitude coordinates. The application processes these images to identify potential rooftop areas suitable for solar panel installation.

* **Rooftop Segmentation**: Utilizes brightness thresholding to simulate rooftop detection. This method estimates the usable rooftop area for solar panels.

* **Solar Metrics Calculation**:

  * **Capacity (kW)**: Calculated based on the estimated rooftop area and panel efficiency.
  * **Annual Output (kWh)**: Estimated using average solar insolation values.
  * **Installation Cost (USD)**: Computed using standard cost per kW metrics.
  * **Annual Savings (USD)**: Based on local electricity rates and estimated energy production.
  * **ROI over 10 Years (%)**: Evaluates the financial return over a decade.

* **AI-Generated Summary**: Optionally, the application can provide a textual summary of the analysis using GPT-based models via OpenRouter or OpenAI APIs.

---

## 📈 Example Use Cases

1. **Residential Solar Assessment**: Homeowners can evaluate the potential benefits of installing solar panels on their rooftops by analyzing satellite images of their property.

2. **Commercial Building Analysis**: Businesses can assess the feasibility and financial implications of adopting solar energy solutions for their facilities.

3. **Urban Planning**: City planners can identify areas with high solar potential to promote sustainable energy initiatives.

4. **Educational Tool**: Institutions can use the application as a teaching aid to demonstrate the integration of AI in renewable energy assessments.

---

## 🚀 Future Improvement Suggestions

1. **Enhanced Rooftop Detection**: Integrate advanced machine learning models, such as U-Net or Mask R-CNN, trained on labeled datasets for more accurate rooftop segmentation.

2. **Dynamic ROI Calculations**: Incorporate real-time data on electricity tariffs, government incentives, and maintenance costs to provide more precise ROI estimates.

3. **3D Modeling**: Develop 3D models of rooftops to account for shading, tilt, and orientation, improving the accuracy of solar potential assessments.

4. **User Account Management**: Implement user authentication to allow users to save and track their analyses over time.

5. **Mobile Compatibility**: Optimize the application for mobile devices to increase accessibility and usability.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## 📬 Contact

For questions or suggestions, please open an issue in the repository or contact the maintainer directly.

