# 🤖 LumaAir ML Models Directory

This folder contains all the machine learning models and related files for the LumaAir platform.

## 📁 **Folder Structure:**

```
models/
├── site_models/          # 🎯 Trained ML Models
│   ├── site_1_model_o3.pkl    # O₃ prediction model for Site 1
│   ├── site_1_model_no2.pkl   # NO₂ prediction model for Site 1
│   ├── site_2_model_o3.pkl    # O₃ prediction model for Site 2
│   ├── site_2_model_no2.pkl   # NO₂ prediction model for Site 2
│   ├── ...                    # Models for sites 3-7
│   └── site_7_model_no2.pkl   # NO₂ prediction model for Site 7
│
├── features/             # 📊 Feature Definitions
│   ├── site_1_features.pkl    # Feature list for Site 1 (37 features)
│   ├── site_2_features.pkl    # Feature list for Site 2
│   ├── ...                    # Feature definitions for sites 3-7
│   └── site_7_features.pkl    # Feature list for Site 7
│
└── metrics/              # 📈 Model Performance
    ├── site_1_metrics.pkl     # Performance metrics for Site 1
    ├── site_2_metrics.pkl     # Performance metrics for Site 2
    ├── ...                    # Metrics for sites 3-7
    └── site_7_metrics.pkl     # Performance metrics for Site 7
```

## 🎯 **Model Details:**

### **Sites Covered:**
1. **Site 1** - Punjabi Bagh, West Delhi (28.69536, 77.18168)
2. **Site 2** - IGI Airport T3 (28.5718, 77.07125)  
3. **Site 3** - Lodhi Colony Metro (28.58278, 77.23441)
4. **Site 4** - Haryana Border (28.82286, 77.10197)
5. **Site 5** - Okhla Industrial (28.53077, 77.27123)
6. **Site 6** - Rohini Metro (28.72954, 77.09601)
7. **Site 7** - Burari Crossing (28.71052, 77.24951)

### **Pollutants Predicted:**
- 🌫️ **O₃** (Ozone) - Ground-level ozone concentrations
- 🏭 **NO₂** (Nitrogen Dioxide) - Traffic and industrial emissions

### **Model Type:**
- **Algorithm:** LightGBM (Light Gradient Boosting Machine)
- **Features:** 37 input features per site including weather, time, and location data
- **Training Period:** 2019-2024 historical data
- **Prediction Range:** Daily predictions with hourly, weekly, and 24-hour modes

## 🔧 **Usage:**

These models are automatically loaded by `pretrained_prediction_engine.py` and used in the **📊 Pretrained Data** page of the LumaAir application.

## 📝 **File Formats:**

All files are stored in Python pickle format (`.pkl`) and contain:
- **Models:** Trained LightGBM classifier objects
- **Features:** List of 37 feature names used for predictions  
- **Metrics:** Model accuracy, precision, recall, and F1-scores

---
*Last Updated: October 2025*
*LumaAir Intelligence Platform v2.5.0*