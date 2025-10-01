# language_system.py - Multi-language support for LumaAir
import streamlit as st

# Language translations dictionary
TRANSLATIONS = {
    "English": {
        # Navigation and Headers
        "app_title": "🌟 LumaAir Intelligence Platform",
        "tagline": "Advanced Air Quality Forecasting & Health Solutions",
        "welcome_title": "Welcome to LumaAir Intelligence", 
        "welcome_subtitle": "Next-generation air quality forecasting platform",
        "forecast_config": "🎯 Forecast Configuration",
        "select_site": "🏢 Select Monitoring Site",
        "generate_forecast": "🚀 Generate Forecast",
        "forecast_params": "Forecast Parameters:",
        "duration": "Duration: Next 24 hours",
        "pollutants": "Pollutants: O₃, NO₂",
        "update_freq": "Update: Hourly",
        
        # Weather Page
        "weather_title": "☁️ Live Weather Conditions",
        "temperature": "🌡️ Temperature",
        "feels_like": "🌡️ Feels Like",
        "wind_speed": "💨 Wind Speed",
        "humidity": "💧 Humidity",
        "pressure": "📊 Pressure",
        "five_day": "5-Day Forecast",
        
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
        "app_preferences": "🎨 App Preferences",
        "theme": "🌙 Theme",
        "language": "🌐 Language", 
        "units": "📏 Units",
        "notifications": "🔔 Quick Actions",
        "refresh_data": "🔄 Refresh Data",
        "save_prefs": "💾 Save Prefs",
        "app_info": "📊 App Information",
        "version": "Version",
        "ai_model": "AI Model",
        "data_sites": "Data Sites",
        "active_theme": "Active Theme",
        
        # Footer
        "powered_by": "🚀 Powered by AI • 🌍 Real-time Delhi Monitoring • 🏥 Health-Focused Solutions",
        "copyright": "© 2025 LumaAir. Built for cleaner, healthier cities."
    },
    
    "Hindi": {
        # Navigation and Headers  
        "app_title": "🌟 लुमाएयर इंटेलिजेंस प्लेटफॉर्म",
        "tagline": "उन्नत वायु गुणवत्ता पूर्वानुमान और स्वास्थ्य समाधान",
        "welcome_title": "लुमाएयर इंटेलिजेंस में आपका स्वागत है",
        "welcome_subtitle": "नई पीढ़ी का वायु गुणवत्ता पूर्वानुमान प्लेटफॉर्म",
        "forecast_config": "🎯 पूर्वानुमान कॉन्फ़िगरेशन",
        "select_site": "🏢 निगरानी स्थल चुनें",
        "generate_forecast": "🚀 पूर्वानुमान जेनरेट करें",
        "forecast_params": "पूर्वानुमान मापदंड:",
        "duration": "अवधि: अगले 24 घंटे",
        "pollutants": "प्रदूषक: O₃, NO₂",
        "update_freq": "अपडेट: प्रति घंटा",
        
        # Weather Page
        "weather_title": "☁️ लाइव मौसम की स्थिति",
        "temperature": "🌡️ तापमान",
        "feels_like": "🌡️ महसूस होता है",
        "wind_speed": "💨 हवा की गति",
        "humidity": "💧 आर्द्रता",
        "pressure": "📊 दबाव",
        "five_day": "5-दिन का पूर्वानुमान",
        
        # Air Quality Tips
        "tips_title": "💡 वायु गुणवत्ता सुधार सुझाव",
        "indoor_tips": "🏠 घर के अंदर हवा की गुणवत्ता",
        "outdoor_tips": "🌳 बाहरी सुरक्षा",
        "health_tips": "🏥 स्वास्थ्य दिशानिर्देश",
        
        # Chatbot
        "chatbot_title": "🤖 लुमाएयर AI असिस्टेंट",
        "chatbot_subtitle": "वायु गुणवत्ता, प्रदूषण और पर्यावरणीय स्वास्थ्य के बारे में कुछ भी पूछें!",
        "chat_placeholder": "मुझसे वायु गुणवत्ता के बारे में पूछें...",
        "clear_chat": "🗑️ चैट इतिहास साफ़ करें",
        
        # Products
        "products_title": "🛒 वायु गुणवत्ता के लिए उपयोगी उत्पाद",
        "air_purifiers": "🌬️ एयर प्यूरिफायर",
        "masks_section": "😷 सुरक्षा मास्क",
        "plants_section": "🌱 हवा साफ करने वाले पौधे",
        "buy_amazon": "🛒 Amazon पर खरीदें",
        "buy_flipkart": "🛒 Flipkart पर खरीदें",
        
        # Settings
        "settings_title": "⚙️ ऐप सेटिंग्स और जानकारी",
        "app_preferences": "🎨 ऐप प्राथमिकताएं",
        "theme": "🌙 थीम",
        "language": "🌐 भाषा",
        "units": "📏 इकाइयां",
        "notifications": "🔔 त्वरित कार्य",
        "refresh_data": "🔄 डेटा रीफ्रेश करें",
        "save_prefs": "💾 प्राथमिकताएं सहेजें",
        "app_info": "📊 ऐप जानकारी",
        "version": "संस्करण",
        "ai_model": "AI मॉडल",
        "data_sites": "डेटा साइटें",
        "active_theme": "सक्रिय थीम",
        
        # Footer
        "powered_by": "🚀 AI द्वारा संचालित • 🌍 रियल-टाइम दिल्ली निगरानी • 🏥 स्वास्थ्य-केंद्रित समाधान",
        "copyright": "© 2025 लुमाएयर। स्वच्छ, स्वस्थ शहरों के लिए बनाया गया।"
    },
    
    "Spanish": {
        # Navigation and Headers
        "app_title": "🌟 Plataforma de Inteligencia LumaAir",
        "tagline": "Pronóstico Avanzado de Calidad del Aire y Soluciones de Salud",
        "welcome_title": "Bienvenido a LumaAir Intelligence",
        "welcome_subtitle": "Plataforma de pronóstico de calidad del aire de nueva generación",
        "forecast_config": "🎯 Configuración de Pronóstico",
        "select_site": "🏢 Seleccionar Sitio de Monitoreo",
        "generate_forecast": "🚀 Generar Pronóstico",
        "forecast_params": "Parámetros del Pronóstico:",
        "duration": "Duración: Próximas 24 horas",
        "pollutants": "Contaminantes: O₃, NO₂",
        "update_freq": "Actualización: Cada hora",
        
        # Weather Page
        "weather_title": "☁️ Condiciones Meteorológicas en Vivo",
        "temperature": "🌡️ Temperatura",
        "feels_like": "🌡️ Sensación Térmica",
        "wind_speed": "💨 Velocidad del Viento",
        "humidity": "💧 Humedad",
        "pressure": "📊 Presión",
        "five_day": "Pronóstico de 5 Días",
        
        # Air Quality Tips
        "tips_title": "💡 Consejos para Mejorar la Calidad del Aire",
        "indoor_tips": "🏠 Calidad del Aire Interior",
        "outdoor_tips": "🌳 Protección Exterior",
        "health_tips": "🏥 Pautas de Salud",
        
        # Chatbot
        "chatbot_title": "🤖 Asistente AI de LumaAir",
        "chatbot_subtitle": "¡Pregúntame sobre calidad del aire, contaminación y salud ambiental!",
        "chat_placeholder": "Pregúntame sobre calidad del aire...",
        "clear_chat": "🗑️ Limpiar Historial de Chat",
        
        # Products
        "products_title": "🛒 Productos Útiles para la Calidad del Aire",
        "air_purifiers": "🌬️ Purificadores de Aire",
        "masks_section": "😷 Mascarillas de Protección",
        "plants_section": "🌱 Plantas Purificadoras de Aire",
        "buy_amazon": "🛒 Comprar en Amazon",
        "buy_flipkart": "🛒 Comprar en Flipkart",
        
        # Settings
        "settings_title": "⚙️ Configuración e Información de la App",
        "app_preferences": "🎨 Preferencias de la App",
        "theme": "🌙 Tema",
        "language": "🌐 Idioma",
        "units": "📏 Unidades",
        "notifications": "🔔 Acciones Rápidas",
        "refresh_data": "🔄 Actualizar Datos",
        "save_prefs": "💾 Guardar Preferencias",
        "app_info": "📊 Información de la App",
        "version": "Versión",
        "ai_model": "Modelo AI",
        "data_sites": "Sitios de Datos",
        "active_theme": "Tema Activo",
        
        # Footer
        "powered_by": "🚀 Impulsado por AI • 🌍 Monitoreo en Tiempo Real de Delhi • 🏥 Soluciones Centradas en Salud",
        "copyright": "© 2025 LumaAir. Construido para ciudades más limpias y saludables."
    },
    
    "French": {
        # Navigation and Headers
        "app_title": "🌟 Plateforme d'Intelligence LumaAir",
        "tagline": "Prévision Avancée de la Qualité de l'Air et Solutions Santé",
        "welcome_title": "Bienvenue sur LumaAir Intelligence",
        "welcome_subtitle": "Plateforme de prévision de qualité de l'air nouvelle génération",
        "forecast_config": "🎯 Configuration des Prévisions",
        "select_site": "🏢 Sélectionner Site de Surveillance",
        "generate_forecast": "🚀 Générer Prévision",
        "forecast_params": "Paramètres de Prévision:",
        "duration": "Durée: Prochaines 24 heures",
        "pollutants": "Polluants: O₃, NO₂",
        "update_freq": "Mise à jour: Toutes les heures",
        
        # Weather Page
        "weather_title": "☁️ Conditions Météo en Direct",
        "temperature": "🌡️ Température",
        "feels_like": "🌡️ Ressenti",
        "wind_speed": "💨 Vitesse du Vent",
        "humidity": "💧 Humidité",
        "pressure": "📊 Pression",
        "five_day": "Prévisions 5 Jours",
        
        # Air Quality Tips
        "tips_title": "💡 Conseils d'Amélioration de la Qualité de l'Air",
        "indoor_tips": "🏠 Qualité de l'Air Intérieur",
        "outdoor_tips": "🌳 Protection Extérieure",
        "health_tips": "🏥 Directives Santé",
        
        # Chatbot
        "chatbot_title": "🤖 Assistant IA LumaAir",
        "chatbot_subtitle": "Demandez-moi tout sur la qualité de l'air, la pollution et la santé environnementale!",
        "chat_placeholder": "Demandez-moi sur la qualité de l'air...",
        "clear_chat": "🗑️ Effacer Historique Chat",
        
        # Products
        "products_title": "🛒 Produits Utiles pour la Qualité de l'Air",
        "air_purifiers": "🌬️ Purificateurs d'Air",
        "masks_section": "😷 Masques de Protection",
        "plants_section": "🌱 Plantes Purificatrices d'Air",
        "buy_amazon": "🛒 Acheter sur Amazon",
        "buy_flipkart": "🛒 Acheter sur Flipkart",
        
        # Settings
        "settings_title": "⚙️ Paramètres et Informations de l'App",
        "app_preferences": "🎨 Préférences de l'App",
        "theme": "🌙 Thème",
        "language": "🌐 Langue",
        "units": "📏 Unités",
        "notifications": "🔔 Actions Rapides",
        "refresh_data": "🔄 Actualiser Données",
        "save_prefs": "💾 Sauvegarder Préférences",
        "app_info": "📊 Infos de l'App",
        "version": "Version",
        "ai_model": "Modèle IA",
        "data_sites": "Sites de Données",
        "active_theme": "Thème Actif",
        
        # Footer
        "powered_by": "🚀 Alimenté par IA • 🌍 Surveillance Delhi en Temps Réel • 🏥 Solutions Axées Santé",
        "copyright": "© 2025 LumaAir. Construit pour des villes plus propres et saines."
    }
}

def get_text(key, language=None):
    """Get translated text for the current language"""
    if language is None:
        language = st.session_state.get("app_language", "English")
    
    return TRANSLATIONS.get(language, TRANSLATIONS["English"]).get(key, key)

def t(key):
    """Short function for getting translated text"""
    return get_text(key)