# language_system.py - Multi-language support for LumaAir
import streamlit as st

# Complete translations dictionary
TRANSLATIONS = {
    "English": {
        # Navigation and Headers
        "app_title": "🌟 LumaAir Intelligence Platform",
        "welcome_title": "Welcome to Advanced Air Quality Intelligence",
        "welcome_subtitle": "Real-time predictions with machine learning",
        "monitoring_sites": "Monitoring Sites",
        "generate_forecast": "Generate Forecast",
        "theme": "Theme",
        "language": "Language",
        
        # Weather Page
        "weather_forecast": "Weather Forecast",
        "weather_title": "☁️ Live Weather Conditions",
        "select_location": "Select Location",
        "get_weather": "🌤️ Get Weather Data",
        "temperature": "🌡️ Temperature",
        "feels_like": "🌡️ Feels Like",
        "wind_speed": "💨 Wind Speed",
        "humidity": "💧 Humidity",
        "pressure": "📊 Pressure",
        "visibility": "👁️ Visibility",
        "five_day": "5-Day Forecast",
        "weather_error": "Error fetching weather data",
        "demo_data": "Showing demo data",
        
        # Air Quality Tips
        "tips_title": "💡 Air Quality Improvement Tips",
        "indoor_tips": "🏠 Indoor Air Quality",
        "outdoor_tips": "🌳 Outdoor Protection",
        "health_tips": "🏥 Health Guidelines",
        
        # Chatbot
        "chatbot_title": "🤖 LumaAir AI Assistant",
        "chatbot_subtitle": "Ask me anything about air quality, pollution, and environmental health!",
        "chat_placeholder": "Ask me about air quality...",
        "clear_chat": "🗑️ Clear Chat History",
        
        # Products
        "products_title": "🛒 Helpful Products for Air Quality",
        "air_purifiers": "🌬️ Air Purifiers",
        "masks_section": "😷 Protection Masks", 
        "plants_section": "🌱 Air Purifying Plants",
        "buy_amazon": "🛒 Buy on Amazon",
        "buy_flipkart": "🛒 Buy on Flipkart",
        
        # Settings
        "settings_title": "⚙️ App Settings & Information",
        "about_section": "ℹ️ About LumaAir",
        "preferences": "🎛️ Preferences",
        "units": "Units",
        "notifications": "🔔 Notifications"
    },
    
    "Hindi": {
        # Navigation and Headers
        "app_title": "🌟 लूमाएयर इंटेलिजेंस प्लेटफॉर्म",
        "welcome_title": "उन्नत वायु गुणवत्ता बुद्धि में आपका स्वागत है",
        "welcome_subtitle": "मशीन लर्निंग के साथ रीयल-टाइम भविष्यवाणी",
        "monitoring_sites": "निगरानी स्थल",
        "generate_forecast": "पूर्वानुमान उत्पन्न करें",
        "theme": "थीम",
        "language": "भाषा",
        
        # Weather Page
        "weather_forecast": "मौसम पूर्वानुमान",
        "weather_title": "☁️ लाइव मौसम की स्थिति",
        "select_location": "स्थान चुनें",
        "get_weather": "🌤️ मौसम डेटा प्राप्त करें",
        "temperature": "🌡️ तापमान",
        "feels_like": "🌡️ महसूस होता है",
        "wind_speed": "💨 हवा की गति",
        "humidity": "💧 नमी",
        "pressure": "📊 दबाव",
        "visibility": "👁️ दृश्यता",
        "five_day": "5 दिन का पूर्वानुमान",
        "weather_error": "मौसम डेटा प्राप्त करने में त्रुटि",
        "demo_data": "डेमो डेटा दिखा रहे हैं",
        
        # Air Quality Tips
        "tips_title": "💡 वायु गुणवत्ता सुधार युक्तियाँ",
        "indoor_tips": "🏠 इनडोर वायु गुणवत्ता",
        "outdoor_tips": "🌳 बाहरी सुरक्षा",
        "health_tips": "🏥 स्वास्थ्य दिशानिर्देश",
        
        # Chatbot
        "chatbot_title": "🤖 लूमाएयर AI असिस्टेंट",
        "chatbot_subtitle": "वायु गुणवत्ता, प्रदूषण और पर्यावरणीय स्वास्थ्य के बारे में कुछ भी पूछें!",
        "chat_placeholder": "मुझसे वायु गुणवत्ता के बारे में पूछें...",
        "clear_chat": "🗑️ चैट इतिहास साफ़ करें",
        
        # Products
        "products_title": "🛒 वायु गुणवत्ता के लिए उपयोगी उत्पाद",
        "air_purifiers": "🌬️ एयर प्यूरिफायर",
        "masks_section": "😷 सुरक्षा मास्क",
        "plants_section": "🌱 वायु शुद्ध करने वाले पौधे",
        "buy_amazon": "🛒 Amazon पर खरीदें",
        "buy_flipkart": "🛒 Flipkart पर खरीदें",
        
        # Settings
        "settings_title": "⚙️ ऐप सेटिंग्स और जानकारी",
        "about_section": "ℹ️ लूमाएयर के बारे में",
        "preferences": "🎛️ प्राथमिकताएं",
        "units": "इकाइयाँ",
        "notifications": "🔔 अधिसूचनाएं"
    },
    
    "Spanish": {
        # Navigation and Headers
        "app_title": "🌟 Plataforma de Inteligencia LumaAir",
        "welcome_title": "Bienvenido a la Inteligencia Avanzada de Calidad del Aire",
        "welcome_subtitle": "Predicciones en tiempo real con aprendizaje automático",
        "monitoring_sites": "Sitios de Monitoreo",
        "generate_forecast": "Generar Pronóstico",
        "theme": "Tema",
        "language": "Idioma",
        
        # Weather Page
        "weather_forecast": "Pronóstico del Tiempo",
        "weather_title": "☁️ Condiciones Meteorológicas en Vivo",
        "select_location": "Seleccionar Ubicación",
        "get_weather": "🌤️ Obtener Datos Meteorológicos",
        "temperature": "🌡️ Temperatura",
        "feels_like": "🌡️ Sensación Térmica",
        "wind_speed": "💨 Velocidad del Viento",
        "humidity": "💧 Humedad",
        "pressure": "📊 Presión",
        "visibility": "👁️ Visibilidad",
        "five_day": "Pronóstico de 5 Días",
        "weather_error": "Error al obtener datos meteorológicos",
        "demo_data": "Mostrando datos de demostración",
        
        # Air Quality Tips
        "tips_title": "💡 Consejos para Mejorar la Calidad del Aire",
        "indoor_tips": "🏠 Calidad del Aire Interior",
        "outdoor_tips": "🌳 Protección Exterior",
        "health_tips": "🏥 Pautas de Salud",
        
        # Chatbot
        "chatbot_title": "🤖 Asistente IA LumaAir",
        "chatbot_subtitle": "¡Pregúntame cualquier cosa sobre calidad del aire, contaminación y salud ambiental!",
        "chat_placeholder": "Pregúntame sobre calidad del aire...",
        "clear_chat": "🗑️ Limpiar Historial de Chat",
        
        # Products
        "products_title": "🛒 Productos Útiles para la Calidad del Aire",
        "air_purifiers": "🌬️ Purificadores de Aire",
        "masks_section": "😷 Máscaras de Protección",
        "plants_section": "🌱 Plantas Purificadoras de Aire",
        "buy_amazon": "🛒 Comprar en Amazon",
        "buy_flipkart": "🛒 Comprar en Flipkart",
        
        # Settings
        "settings_title": "⚙️ Configuraciones y Información de la App",
        "about_section": "ℹ️ Acerca de LumaAir",
        "preferences": "🎛️ Preferencias",
        "units": "Unidades",
        "notifications": "🔔 Notificaciones"
    },
    
    "French": {
        # Navigation and Headers
        "app_title": "🌟 Plateforme d'Intelligence LumaAir",
        "welcome_title": "Bienvenue dans l'Intelligence Avancée de la Qualité de l'Air",
        "welcome_subtitle": "Prédictions en temps réel avec apprentissage automatique",
        "monitoring_sites": "Sites de Surveillance",
        "generate_forecast": "Générer des Prévisions",
        "theme": "Thème",
        "language": "Langue",
        
        # Weather Page
        "weather_forecast": "Prévisions Météorologiques",
        "weather_title": "☁️ Conditions Météorologiques en Direct",
        "select_location": "Sélectionner l'Emplacement",
        "get_weather": "🌤️ Obtenir les Données Météo",
        "temperature": "🌡️ Température",
        "feels_like": "🌡️ Ressenti",
        "wind_speed": "💨 Vitesse du Vent",
        "humidity": "💧 Humidité",
        "pressure": "📊 Pression",
        "visibility": "👁️ Visibilité",
        "five_day": "Prévisions sur 5 Jours",
        "weather_error": "Erreur lors de la récupération des données météo",
        "demo_data": "Affichage des données de démonstration",
        
        # Air Quality Tips
        "tips_title": "💡 Conseils d'Amélioration de la Qualité de l'Air",
        "indoor_tips": "🏠 Qualité de l'Air Intérieur",
        "outdoor_tips": "🌳 Protection Extérieure",
        "health_tips": "🏥 Directives de Santé",
        
        # Chatbot
        "chatbot_title": "🤖 Assistant IA LumaAir",
        "chatbot_subtitle": "Demandez-moi tout sur la qualité de l'air, la pollution et la santé environnementale !",
        "chat_placeholder": "Demandez-moi à propos de la qualité de l'air...",
        "clear_chat": "🗑️ Effacer l'Historique du Chat",
        
        # Products
        "products_title": "🛒 Produits Utiles pour la Qualité de l'Air",
        "air_purifiers": "🌬️ Purificateurs d'Air",
        "masks_section": "😷 Masques de Protection",
        "plants_section": "🌱 Plantes Purificatrices d'Air",
        "buy_amazon": "🛒 Acheter sur Amazon",
        "buy_flipkart": "🛒 Acheter sur Flipkart",
        
        # Settings
        "settings_title": "⚙️ Paramètres et Informations de l'App",
        "about_section": "ℹ️ À Propos de LumaAir",
        "preferences": "🎛️ Préférences",
        "units": "Unités",
        "notifications": "🔔 Notifications"
    }
}

def get_text(key):
    """Get translated text based on current language setting"""
    if 'app_language' not in st.session_state:
        st.session_state.app_language = "English"
    
    current_language = st.session_state.app_language
    
    # Return translated text or key if not found
    return TRANSLATIONS.get(current_language, {}).get(key, key)

# Helper function for easier access
def t(key):
    """Short alias for get_text"""
    return get_text(key)