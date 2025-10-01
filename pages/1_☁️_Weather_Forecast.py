# pages/1_☁️_Weather_Forecast.py

import streamlit as st
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(page_title="Weather Forecast", page_icon="☁️", layout="wide")

# --- Load Theme ---
from theme_loader import apply_global_theme
apply_global_theme()

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
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        # Debug: Show raw temperature for troubleshooting
        if 'list' in data and len(data['list']) > 0:
            raw_temp = data['list'][0]['main']['temp']
            st.info(f"🔍 Debug: Raw API temperature = {raw_temp}")
        
        return data
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching weather data: {e}")
        st.warning("Falling back to demo data...")
        return get_demo_weather_data()

# --- Demo Data Function ---
def get_demo_weather_data():
    return {
        "city": {"name": "New Delhi"},
        "list": [
            {
                "dt_txt": "2025-10-01 12:00:00",
                "main": {"temp": 32, "humidity": 65, "feels_like": 35},
                "weather": [{"description": "partly cloudy", "icon": "02d"}],
                "wind": {"speed": 2.5}
            },
            {
                "dt_txt": "2025-10-02 12:00:00",
                "main": {"temp": 30, "humidity": 70, "feels_like": 33},
                "weather": [{"description": "cloudy", "icon": "03d"}],
                "wind": {"speed": 3.0}
            },
            {
                "dt_txt": "2025-10-03 12:00:00",
                "main": {"temp": 28, "humidity": 75, "feels_like": 31},
                "weather": [{"description": "light rain", "icon": "10d"}],
                "wind": {"speed": 3.5}
            },
            {
                "dt_txt": "2025-10-04 12:00:00",
                "main": {"temp": 29, "humidity": 68, "feels_like": 32},
                "weather": [{"description": "sunny", "icon": "01d"}],
                "wind": {"speed": 2.0}
            },
            {
                "dt_txt": "2025-10-05 12:00:00",
                "main": {"temp": 31, "humidity": 60, "feels_like": 34},
                "weather": [{"description": "clear sky", "icon": "01d"}],
                "wind": {"speed": 2.2}
            }
        ]
    }

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
            <div class="label">🌡️ Feels Like</div>
                        <div class="value">{feels_like_display}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.subheader("5-Day Forecast")

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
st.title("☁️ Weather Forecast")
st.markdown("#### Real-time weather information for major Indian cities")

st.sidebar.header("City Selection")
city_options = {
    "New Delhi, India": (28.6139, 77.2090),
    "Chennai, India": (13.0827, 80.2707),
    "Mumbai, India": (19.0760, 72.8777),
    "Bangalore, India": (12.9716, 77.5946),
    "Kolkata, India": (22.5726, 88.3639),
    "Hyderabad, India": (17.3850, 78.4867),
    "Pune, India": (18.5204, 73.8567)
}
selected_city = st.sidebar.selectbox("Choose a city:", list(city_options.keys()))

if st.sidebar.button("🌤️ Get Weather Forecast"):
    lat, lon = city_options[selected_city]
    with st.spinner(f"Fetching weather for {selected_city}..."):
        forecast = get_5_day_forecast(lat, lon)
    if forecast:
        display_weather(forecast)
    else:
        st.error("Failed to retrieve forecast.")
else:
    st.info("Choose a city and click the button to see the weather forecast.")

# --- API Key Setup Instructions ---
with st.expander("🔧 Setup Instructions"):
    st.markdown("""
    **To get live weather data:**
    1. Sign up at [RapidAPI](https://rapidapi.com/)
    2. Subscribe to the [OpenWeather API](https://rapidapi.com/openweatherapi/api/openweather-map/)
    3. Create a `.env` file in your project root
    4. Add your API key: `RAPIDAPI_KEY=your_api_key_here`
    
    **Currently showing demo data for demonstration purposes.**
    """)