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
        "get_weather_forecast": "🌤️ Get Weather Forecast",
        "city_selection": "🏙️ City Selection",
        "choose_city": "Choose a City",
        "fetching_weather": "📡 Fetching weather data for",
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
        "shopping_title": "Helpful Products for Air Quality",
        "shopping_subtitle": "Discover products to improve your air quality and health",
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
        "notifications": "🔔 Notifications",
        
        # Pretrained Data Page
        "pretrained_title": "📊 Pretrained Data Predictions",
        "pretrained_subtitle": "Historical predictions using trained ML models (2019-2024)",
        "select_site": "Select Monitoring Site",
        "select_pollutant": "Select Pollutant",
        "select_time_period": "Select Time Period",
        "select_date_range": "Select Date Range",
        "start_date": "Start Date",
        "end_date": "End Date", 
        "generate_prediction": "🔮 Generate Predictions",
        "prediction_results": "📈 Prediction Results",
        "model_info": "🤖 Model Information",
        "summary_stats": "📊 Summary Statistics",
        "mean_value": "Mean Value",
        "std_deviation": "Standard Deviation", 
        "min_value": "Minimum",
        "max_value": "Maximum",
        "median_value": "Median",
        "data_points": "Data Points",
        "threshold_exceedances": "Threshold Exceedances",
        "no_predictions": "No predictions available. Please check your selections.",
        "loading_models": "Loading pretrained models...",
        "prediction_chart": "📈 Prediction Timeline",
        "model_type": "Model Type",
        "features_count": "Number of Features",
        "model_fitted": "Model Status",
        "best_iteration": "Best Iteration",
        "estimators_count": "Estimators"
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
        "get_weather_forecast": "🌤️ मौसम पूर्वानुमान प्राप्त करें",
        "city_selection": "🏙️ शहर चयन",
        "choose_city": "एक शहर चुनें",
        "fetching_weather": "📡 मौसम डेटा प्राप्त कर रहा है",
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
        "shopping_title": "वायु गुणवत्ता के लिए उपयोगी उत्पाद",
        "shopping_subtitle": "अपनी वायु गुणवत्ता और स्वास्थ्य में सुधार के लिए उत्पाद खोजें",
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
        "notifications": "🔔 अधिसूचनाएं",
        
        # Pretrained Data Page
        "pretrained_title": "📊 पूर्व-प्रशिक्षित डेटा भविष्यवाणी",
        "pretrained_subtitle": "प्रशिक्षित ML मॉडल का उपयोग करते हुए ऐतिहासिक भविष्यवाणी (2019-2024)",
        "select_site": "निगरानी स्थल चुनें",
        "select_pollutant": "प्रदूषक चुनें",
        "select_time_period": "समय अवधि चुनें",
        "select_date_range": "दिनांक सीमा चुनें",
        "start_date": "प्रारंभ दिनांक",
        "end_date": "समाप्ति दिनांक",
        "generate_prediction": "🔮 भविष्यवाणी उत्पन्न करें",
        "prediction_results": "📈 भविष्यवाणी परिणाम",
        "model_info": "🤖 मॉडल जानकारी",
        "summary_stats": "📊 सारांश सांख्यिकी",
        "mean_value": "औसत मान",
        "std_deviation": "मानक विचलन",
        "min_value": "न्यूनतम",
        "max_value": "अधिकतम", 
        "median_value": "मध्यक",
        "data_points": "डेटा बिंदु",
        "threshold_exceedances": "थ्रेशोल्ड उल्लंघन",
        "no_predictions": "कोई भविष्यवाणी उपलब्ध नहीं। कृपया अपने चयन की जाँच करें।",
        "loading_models": "पूर्व-प्रशिक्षित मॉडल लोड हो रहे हैं...",
        "prediction_chart": "📈 भविष्यवाणी समयरेखा",
        "model_type": "मॉडल प्रकार",
        "features_count": "फीचर्स की संख्या",
        "model_fitted": "मॉडल स्थिति",
        "best_iteration": "सर्वोत्तम पुनरावृत्ति",
        "estimators_count": "एस्टिमेटर्स"
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
        "get_weather_forecast": "🌤️ Obtener Pronóstico del Tiempo",
        "city_selection": "🏙️ Selección de Ciudad",
        "choose_city": "Elige una Ciudad",
        "fetching_weather": "📡 Obteniendo datos meteorológicos para",
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
        "shopping_title": "Productos Útiles para la Calidad del Aire",
        "shopping_subtitle": "Descubre productos para mejorar tu calidad del aire y salud",
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
        "notifications": "🔔 Notificaciones",
        
        # Pretrained Data Page
        "pretrained_title": "📊 Predicciones de Datos Preentrenados",
        "pretrained_subtitle": "Predicciones históricas usando modelos ML entrenados (2019-2024)",
        "select_site": "Seleccionar Sitio de Monitoreo",
        "select_pollutant": "Seleccionar Contaminante",
        "select_time_period": "Seleccionar Período de Tiempo",
        "select_date_range": "Seleccionar Rango de Fechas",
        "start_date": "Fecha de Inicio",
        "end_date": "Fecha de Fin",
        "generate_prediction": "🔮 Generar Predicciones",
        "prediction_results": "📈 Resultados de Predicción",
        "model_info": "🤖 Información del Modelo",
        "summary_stats": "📊 Estadísticas Resumidas",
        "mean_value": "Valor Promedio",
        "std_deviation": "Desviación Estándar",
        "min_value": "Mínimo",
        "max_value": "Máximo",
        "median_value": "Mediana",
        "data_points": "Puntos de Datos",
        "threshold_exceedances": "Excesos de Umbral",
        "no_predictions": "No hay predicciones disponibles. Verifique sus selecciones.",
        "loading_models": "Cargando modelos preentrenados...",
        "prediction_chart": "📈 Cronología de Predicción",
        "model_type": "Tipo de Modelo",
        "features_count": "Número de Características",
        "model_fitted": "Estado del Modelo",
        "best_iteration": "Mejor Iteración",
        "estimators_count": "Estimadores"
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
        "get_weather_forecast": "🌤️ Obtenir les Prévisions Météo",
        "city_selection": "🏙️ Sélection de Ville",
        "choose_city": "Choisissez une Ville",
        "fetching_weather": "📡 Récupération des données météo pour",
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
        "shopping_title": "Produits Utiles pour la Qualité de l'Air",
        "shopping_subtitle": "Découvrez des produits pour améliorer votre qualité de l'air et votre santé",
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
        "notifications": "🔔 Notifications",
        
        # Pretrained Data Page
        "pretrained_title": "📊 Prédictions de Données Préentraînées",
        "pretrained_subtitle": "Prédictions historiques utilisant des modèles ML entraînés (2019-2024)",
        "select_site": "Sélectionner Site de Surveillance",
        "select_pollutant": "Sélectionner Polluant",
        "select_time_period": "Sélectionner Période de Temps",
        "select_date_range": "Sélectionner Plage de Dates",
        "start_date": "Date de Début",
        "end_date": "Date de Fin",
        "generate_prediction": "🔮 Générer Prédictions",
        "prediction_results": "📈 Résultats de Prédiction",
        "model_info": "🤖 Informations du Modèle",
        "summary_stats": "📊 Statistiques Résumées",
        "mean_value": "Valeur Moyenne",
        "std_deviation": "Écart Type",
        "min_value": "Minimum",
        "max_value": "Maximum",
        "median_value": "Médiane",
        "data_points": "Points de Données",
        "threshold_exceedances": "Dépassements de Seuil",
        "no_predictions": "Aucune prédiction disponible. Veuillez vérifier vos sélections.",
        "loading_models": "Chargement des modèles préentraînés...",
        "prediction_chart": "📈 Chronologie de Prédiction",
        "model_type": "Type de Modèle",
        "features_count": "Nombre de Caractéristiques",
        "model_fitted": "Statut du Modèle",
        "best_iteration": "Meilleure Itération",
        "estimators_count": "Estimateurs"
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