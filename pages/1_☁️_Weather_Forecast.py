# pages/1_☁️_Weather_Forecast.py

import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Weather Forecast", page_icon="☁️", layout="wide")

# --- Load Theme and Language ---
from theme_loader import apply_global_theme
from language_system import get_text

apply_global_theme()
t = get_text

# Real API Key for weather data
API_KEY = os.getenv("RAPIDAPI_KEY", "797baaae03msh3e64748769dd1a6p154df7jsn05cea50abd53")

# --- API Call Function ---
def get_5_day_forecast(latitude, longitude):
    url = "https://open-weather13.p.rapidapi.com/fivedaysforcast"
    querystring = {"latitude": str(latitude), "longitude": str(longitude), "lang": "EN"}
    headers = {
        "x-rapidapi-key": API_KEY,
        "x-rapidapi-host": "open-weather13.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring, timeout=10)
        
        # Handle rate limiting (429 error)
        if response.status_code == 429:
            st.warning("⚠️ Weather API rate limit reached. Showing demo data instead.")
            return get_demo_weather_data(latitude, longitude)
        
        response.raise_for_status()
        data = response.json()
        
        # Debug: Show raw temperature for troubleshooting
        if 'list' in data and len(data['list']) > 0:
            raw_temp = data['list'][0]['main']['temp']
            st.info(f"🔍 Debug: Raw API temperature = {raw_temp}")
        
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        st.info("📊 Showing demo weather data instead.")
        return get_demo_weather_data(latitude, longitude)

# --- Demo Data Function ---
def get_demo_weather_data(latitude=28.6139, longitude=77.2090):
    """Generate realistic demo weather data when API fails"""
    import random
    from datetime import datetime, timedelta
    
    demo_data = {
        "city": {"name": "Delhi", "country": "IN"},
        "list": []
    }
    
    # Generate 5 days of demo weather data
    base_temp = 25 + random.uniform(-5, 10)  # Base temperature around 25°C
    
    for i in range(5):
        day_date = datetime.now() + timedelta(days=i)
        daily_temp = base_temp + random.uniform(-3, 3)
        
        weather_conditions = [
            {"main": "Clear", "description": "clear sky", "icon": "01d"},
            {"main": "Clouds", "description": "few clouds", "icon": "02d"},
            {"main": "Clouds", "description": "scattered clouds", "icon": "03d"},
            {"main": "Haze", "description": "haze", "icon": "50d"}
        ]
        
        condition = random.choice(weather_conditions)
        
        demo_data["list"].append({
            "dt": int(day_date.timestamp()),
            "main": {
                "temp": daily_temp,
                "feels_like": daily_temp + random.uniform(-2, 2),
                "humidity": random.randint(40, 80),
                "pressure": random.randint(1010, 1020)
            },
            "weather": [condition],
            "wind": {
                "speed": random.uniform(2, 8)
            },
            "dt_txt": day_date.strftime("%Y-%m-%d 12:00:00")
        })
    
    return demo_data

# --- Temperature Conversion Function ---
def convert_temp(temp_kelvin, units="Metric"):
    """Convert temperature from Kelvin based on user preference"""
    if temp_kelvin > 200:  # Likely Kelvin (K > 200)
        celsius = temp_kelvin - 273.15
    else:  # Already in Celsius
        celsius = temp_kelvin
    
    # Get user's preferred units from session state
    user_units = st.session_state.get("app_units", "Metric")
    
    if user_units == "Imperial":
        fahrenheit = (celsius * 9/5) + 32
        return f"{fahrenheit:.1f}°F"
    else:
        return f"{celsius:.1f}°C"

# --- Main Display Function ---
def display_weather(forecast_data):
    current = forecast_data['list'][0]
    city_name = forecast_data.get('city', {}).get('name', 'N/A')
    
    # Convert temperature based on user preference
    temp_display = convert_temp(current['main']['temp'])
    feels_like_display = convert_temp(current['main']['feels_like'])
    
    # --- Main Weather Display ---
    with st.container():
        st.markdown(f"""
        <div class="glass-card main-weather-display">
            <h3>{city_name}</h3>
            <h1>{temp_display}</h1>
            <h4>{current['weather'][0]['description'].title()}</h4>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()

    # --- Info Cards Row ---
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"""
        <div class="info-card">
            <div class="label">💧 Humidity</div>
            <div class="value">{current['main']['humidity']}%</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="info-card">
            <div class="label">💨 Wind Speed</div>
            <div class="value">{round(current['wind']['speed'] * 3.6) if st.session_state.get('app_units', 'Metric') == 'Metric' else round(current['wind']['speed'] * 2.237)} {'km/h' if st.session_state.get('app_units', 'Metric') == 'Metric' else 'mph'}</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="info-card">
            <div class="label">{t('feels_like')}</div>
                        <div class="value">{feels_like_display}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader(t('5_day_forecast'))

    # --- 5-Day Forecast Cards ---
    daily_forecasts = {}
    for forecast in forecast_data['list']:
        date = pd.to_datetime(forecast['dt_txt']).date()
        if date not in daily_forecasts and "12:00:00" in forecast['dt_txt']:
            daily_forecasts[date] = forecast
            
    final_daily_list = list(daily_forecasts.values())[:5]
    
    if len(final_daily_list) >= 5:
        cols = st.columns(5)
        for i, item in enumerate(final_daily_list):
            with cols[i]:
                day_name = pd.to_datetime(item['dt_txt']).strftime('%a')
                temp_display_daily = convert_temp(item['main']['temp'])
                icon = item['weather'][0]['icon']
                icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"
                
                st.markdown(f"""
                <div class="day-forecast-card">
                    <h5>{day_name}</h5>
                    <img src="{icon_url}" width="60">
                    <h4>{temp_display_daily}</h4>
                </div>
                """, unsafe_allow_html=True)

# ==============================================================================
# --- APP LOGIC ---
# ==============================================================================
st.title(f"🌤️ {t('weather forecast')}")
st.markdown(f"#### {t('weather subtitle')}")

st.sidebar.header(t('city_selection'))
city_options = {
    "New Delhi, India": (28.6139, 77.2090),
    "Chennai, India": (13.0827, 80.2707),
    "Mumbai, India": (19.0760, 72.8777),
    "Bangalore, India": (12.9716, 77.5946),
    "Kolkata, India": (22.5726, 88.3639),
    "Hyderabad, India": (17.3850, 78.4867),
    "Pune, India": (18.5204, 73.8567)
}
selected_city = st.sidebar.selectbox(t('choose_city'), list(city_options.keys()))

if st.sidebar.button(t('get_weather_forecast')):
    lat, lon = city_options[selected_city]
    with st.spinner(f"{t('fetching_weather')} {selected_city}..."):
        forecast = get_5_day_forecast(lat, lon)
    if forecast:
        display_weather(forecast)
    else:
        st.error(t('failed retrieve'))
else:
    st.info(t('Choose City Info'))

# --- API Key Setup Instructions ---
with st.expander(t('setup instructions')):
    st.markdown("""
    **To get live weather data:**
    1. Sign up at [RapidAPI](https://rapidapi.com/)
    2. Subscribe to the [OpenWeather API](https://rapidapi.com/openweatherapi/api/openweather-map/)
    3. Create a `.env` file in your project root
    4. Add your API key: `RAPIDAPI_KEY=your_api_key_here`
    
    **Currently showing demo data for demonstration purposes.**
    """)
