# 🌟 LumaAir Intelligence Platform

> **Advanced Air Quality Forecasting & Health Solutions**

[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![AI](https://img.shields.io/badge/Google-Gemini_AI-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/)

## 🎯 **Overview**

LumaAir is a next-generation air quality forecasting platform that combines machine learning, real-time weather data, and health-focused solutions to help people make informed decisions about air quality in Delhi, India.

### ✨ **Key Features**

- 🧠 **AI-Powered Predictions** - 24-hour forecasts for O₃ and NO₂ concentrations
- 🌍 **Multi-Language Support** - English, Hindi, Spanish, French
- 🎨 **Dynamic Themes** - Light and Dark modes with glassmorphism design
- 🌡️ **Weather Integration** - Real-time weather data with unit conversion
- 🤖 **AI Chatbot** - Powered by Google Gemini 2.5 for air quality guidance
- 🛒 **Smart Shopping** - Curated air purifiers, masks, and plants
- 📊 **7 Monitoring Sites** - Real Delhi locations with coordinates
- 📱 **Responsive Design** - Modern dashboard with interactive animations

## 🏗️ **Architecture**

### **Core Components:**
- **Home Dashboard** - ML forecasting with interactive charts
- **Weather Module** - RapidAPI integration with temperature conversion
- **AI Assistant** - Google Gemini chatbot for health guidance
- **Product Recommendations** - Amazon/Flipkart integration
- **Multi-Language System** - Complete i18n support
- **Theme Engine** - Dynamic styling with CSS-in-JS

### **Tech Stack:**
- **Frontend:** Streamlit with custom CSS/HTML
- **AI/ML:** Google Gemini 2.5 Flash API
- **Weather API:** RapidAPI Weather Service
- **Data Processing:** Pandas, NumPy
- **Visualization:** Plotly Interactive Charts
- **Styling:** Custom CSS with glassmorphism effects

## 🚀 **Quick Start**

### **Prerequisites**
```bash
Python 3.8+
pip (Python package manager)
```

### **Installation**

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/LumaAir-Intelligence-Platform.git
cd LumaAir-Intelligence-Platform
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Set up API keys:**
   - Get Google AI API key from [Google AI Studio](https://aistudio.google.com/)
   - Get RapidAPI key from [RapidAPI Weather](https://rapidapi.com/weatherapi/api/weatherapi-com/)

4. **Run the application:**
```bash
streamlit run Home.py
```

5. **Open your browser:** `http://localhost:8501`

## 🌍 **Multi-Language Support**

LumaAir supports 4 languages with complete interface translation:

- 🇺🇸 **English** - Default interface
- 🇮🇳 **Hindi** - हिंदी अनुवाद 
- 🇪🇸 **Spanish** - Interfaz en Español
- 🇫🇷 **French** - Interface en Français

**How to switch:** Go to footer settings → Language selector → Choose your language

## 📊 **Delhi Monitoring Sites**

| Site ID | Location | Coordinates | Area Coverage |
|---------|----------|-------------|---------------|
| Site 1 | Punjabi Bagh | 28.69536, 77.18168 | West Delhi |
| Site 2 | IGI Airport | 28.5718, 77.07125 | Southwest Delhi |
| Site 3 | Lodhi Colony | 28.58278, 77.23441 | South Delhi |
| Site 4 | Haryana Border | 28.82286, 77.10197 | North Delhi |
| Site 5 | Okhla | 28.53077, 77.27123 | Southeast Delhi |
| Site 6 | Rohini | 28.72954, 77.09601 | Northwest Delhi |
| Site 7 | Burari | 28.71052, 77.24951 | North Delhi |

## 🎨 **Features Showcase**

### **Dashboard Intelligence**
- Real-time air quality predictions
- Interactive Plotly charts
- Health advisory system
- Color-coded pollution levels

### **AI Chatbot Assistant**
- Natural language processing
- Air quality expertise
- Health recommendations
- Multi-language responses

### **Smart Product Recommendations**
- Air purifiers with specifications
- N95/N99 masks for protection  
- Air-purifying plants
- Direct shopping links

## 🛠️ **Development**

### **Project Structure**
```
LumaAir/
├── Home.py                          # Main dashboard
├── theme_loader.py                  # Theme management
├── language_system.py               # Multi-language support
├── style.css                        # Custom styling
├── pages/
│   ├── 1_☁️_Weather_Forecast.py    # Weather module
│   ├── 2_💡_Air_Quality_Tips.py    # Health tips
│   ├── 3_🤖_AI_Chatbot.py          # AI assistant
│   └── 4_🛒_Helpful_Products.py    # Shopping module
└── requirements.txt                 # Dependencies
```

### **API Configuration**
The app uses two main APIs:
- **Google Gemini AI:** For intelligent chatbot responses
- **RapidAPI Weather:** For real-time weather data

## 📈 **Usage Statistics**

- **Pollutant Predictions:** O₃, NO₂ concentrations
- **Forecast Range:** 24-hour predictions
- **Update Frequency:** Hourly refresh
- **Accuracy:** ML-based forecasting algorithms
- **Coverage:** Delhi NCR region

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create feature branch:** `git checkout -b feature/AmazingFeature`
3. **Commit changes:** `git commit -m 'Add AmazingFeature'`
4. **Push to branch:** `git push origin feature/AmazingFeature`
5. **Open Pull Request**

### **Areas for Contribution:**
- 🌍 Additional language translations
- 📊 More visualization charts
- 🤖 Enhanced AI responses
- 🏥 Health recommendation algorithms
- 📱 Mobile responsiveness improvements

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 **Acknowledgments**

- **Google Gemini AI** for intelligent chatbot capabilities
- **RapidAPI Weather** for reliable weather data
- **Streamlit** for the amazing web app framework
- **Delhi Pollution Control Committee** for monitoring site data
- **Open source community** for inspiration and tools

## 📞 **Contact & Support**

- **Issues:** [GitHub Issues](https://github.com/yourusername/LumaAir-Intelligence-Platform/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/LumaAir-Intelligence-Platform/discussions)
- **Email:** your-email@example.com

---

<div align="center">

**🌟 Built with ❤️ for cleaner, healthier cities 🌟**

[![Made with Streamlit](https://img.shields.io/badge/Made%20with-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Powered by AI](https://img.shields.io/badge/Powered%20by-Google%20AI-4285F4.svg)](https://ai.google.dev/)

**[⭐ Star this repo](https://github.com/yourusername/LumaAir-Intelligence-Platform) | [🍴 Fork it](https://github.com/yourusername/LumaAir-Intelligence-Platform/fork) | [📖 Documentation](https://github.com/yourusername/LumaAir-Intelligence-Platform/wiki)**

</div>