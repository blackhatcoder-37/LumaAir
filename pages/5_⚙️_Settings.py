# pages/5_⚙️_Settings.py
import streamlit as st
import json
import os

st.set_page_config(page_title="Settings", page_icon="⚙️", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("style.css")

# Settings file path
SETTINGS_FILE = "lumaair_settings.json"

# Default settings
DEFAULT_SETTINGS = {
    "theme": "dark",
    "default_site": 1,
    "notifications": True,
    "auto_refresh": False,
    "language": "English",
    "units": "metric",
    "forecast_hours": 24,
    "show_coordinates": True,
    "api_timeout": 30
}

def load_settings():
    """Load settings from file or return defaults"""
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except:
            return DEFAULT_SETTINGS.copy()
    return DEFAULT_SETTINGS.copy()

def save_settings(settings):
    """Save settings to file"""
    try:
        with open(SETTINGS_FILE, 'w') as f:
            json.dump(settings, f, indent=2)
        return True
    except:
        return False

# Load current settings
current_settings = load_settings()

# Page Header
st.markdown("""
<div class="glass-card" style="text-align: center; margin-bottom: 2rem;">
    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 1.5rem;">
        <div style="background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 12px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;">
            ⚙️
        </div>
        <div style="text-align: left;">
            <h2 style="margin: 0; color: #f8fafc; font-size: 1.8rem; font-weight: 700;">LumaAir Settings</h2>
            <p style="margin: 0; color: #94a3b8; font-size: 0.95rem;">Customize your air quality monitoring experience</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Create two columns for settings layout
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #f8fafc; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <span style="background: linear-gradient(135deg, #3b82f6, #1d4ed8); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">🎨</span>
            App Preferences
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme Selection
    theme_options = ["Dark", "Light", "Auto"]
    current_theme = current_settings.get("theme", "dark").title()
    selected_theme = st.selectbox(
        "🌙 App Theme",
        theme_options,
        index=theme_options.index(current_theme) if current_theme in theme_options else 0,
        help="Choose your preferred visual theme"
    )
    current_settings["theme"] = selected_theme.lower()
    
    # Language Selection
    language_options = ["English", "Hindi", "Spanish", "French"]
    selected_language = st.selectbox(
        "🌐 Language",
        language_options,
        index=language_options.index(current_settings.get("language", "English")),
        help="Select your preferred language"
    )
    current_settings["language"] = selected_language
    
    # Units Selection
    units_options = ["Metric (°C, km/h)", "Imperial (°F, mph)"]
    units_display = "Metric (°C, km/h)" if current_settings.get("units", "metric") == "metric" else "Imperial (°F, mph)"
    selected_units = st.selectbox(
        "📏 Units",
        units_options,
        index=units_options.index(units_display),
        help="Choose measurement units"
    )
    current_settings["units"] = "metric" if "Metric" in selected_units else "imperial"
    
    st.markdown("""
    <div class="glass-card" style="margin-top: 2rem;">
        <h3 style="color: #f8fafc; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <span style="background: linear-gradient(135deg, #10b981, #059669); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">🔔</span>
            Notifications
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Notification Settings
    notifications_enabled = st.checkbox(
        "📢 Enable Notifications",
        value=current_settings.get("notifications", True),
        help="Receive alerts about air quality changes"
    )
    current_settings["notifications"] = notifications_enabled
    
    auto_refresh = st.checkbox(
        "🔄 Auto-refresh Data",
        value=current_settings.get("auto_refresh", False),
        help="Automatically update air quality data"
    )
    current_settings["auto_refresh"] = auto_refresh
    
    show_coordinates = st.checkbox(
        "📍 Show Coordinates",
        value=current_settings.get("show_coordinates", True),
        help="Display latitude/longitude for monitoring sites"
    )
    current_settings["show_coordinates"] = show_coordinates

with col2:
    st.markdown("""
    <div class="glass-card">
        <h3 style="color: #f8fafc; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <span style="background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">📊</span>
            Forecast Settings
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Default monitoring site
    site_names = [
        "Punjabi Bagh, West Delhi",
        "IGI Airport, Southwest Delhi", 
        "Lodhi Colony, South Delhi",
        "North Delhi (Haryana Border)",
        "Okhla, Southeast Delhi",
        "Rohini, Northwest Delhi",
        "Burari, North Delhi"
    ]
    
    default_site_index = current_settings.get("default_site", 1) - 1
    selected_site = st.selectbox(
        "🏢 Default Monitoring Site",
        site_names,
        index=default_site_index if 0 <= default_site_index < len(site_names) else 0,
        help="Your preferred default location for forecasts"
    )
    current_settings["default_site"] = site_names.index(selected_site) + 1
    
    # Forecast duration
    forecast_hours = st.slider(
        "⏰ Forecast Duration (Hours)",
        min_value=6,
        max_value=72,
        value=current_settings.get("forecast_hours", 24),
        step=6,
        help="How far ahead to predict air quality"
    )
    current_settings["forecast_hours"] = forecast_hours
    
    # API timeout
    api_timeout = st.slider(
        "🌐 API Timeout (Seconds)",
        min_value=10,
        max_value=60,
        value=current_settings.get("api_timeout", 30),
        step=5,
        help="Maximum wait time for data requests"
    )
    current_settings["api_timeout"] = api_timeout
    
    st.markdown("""
    <div class="glass-card" style="margin-top: 2rem;">
        <h3 style="color: #f8fafc; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
            <span style="background: linear-gradient(135deg, #ef4444, #dc2626); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">💾</span>
            Data Management
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Data Management Options
    col2a, col2b = st.columns(2)
    
    with col2a:
        if st.button("💾 Save Settings", use_container_width=True):
            if save_settings(current_settings):
                st.success("✅ Settings saved successfully!")
                st.balloons()
            else:
                st.error("❌ Failed to save settings")
    
    with col2b:
        if st.button("🔄 Reset to Default", use_container_width=True):
            if save_settings(DEFAULT_SETTINGS):
                st.success("✅ Settings reset to default!")
                st.rerun()
            else:
                st.error("❌ Failed to reset settings")

# Current Settings Display
st.markdown("""
<div class="glass-card" style="margin-top: 2rem;">
    <h3 style="color: #f8fafc; margin-bottom: 1.5rem; display: flex; align-items: center; gap: 0.5rem;">
        <span style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">📋</span>
        Current Configuration
    </h3>
</div>
""", unsafe_allow_html=True)

# Display current settings in a nice format
col3, col4 = st.columns(2)

with col3:
    st.markdown(f"""
    <div style="background: rgba(59, 130, 246, 0.1); border-left: 3px solid #3b82f6; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
        <h4 style="margin: 0 0 0.5rem 0; color: #3b82f6;">App Settings</h4>
        <p style="margin: 0.2rem 0; color: #94a3b8;">🎨 Theme: {current_settings['theme'].title()}</p>
        <p style="margin: 0.2rem 0; color: #94a3b8;">🌐 Language: {current_settings['language']}</p>
        <p style="margin: 0.2rem 0; color: #94a3b8;">📏 Units: {current_settings['units'].title()}</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 1rem; border-radius: 8px; margin: 0.5rem 0;">
        <h4 style="margin: 0 0 0.5rem 0; color: #10b981;">Forecast Settings</h4>
        <p style="margin: 0.2rem 0; color: #94a3b8;">🏢 Default Site: {site_names[current_settings['default_site']-1]}</p>
        <p style="margin: 0.2rem 0; color: #94a3b8;">⏰ Duration: {current_settings['forecast_hours']} hours</p>
        <p style="margin: 0.2rem 0; color: #94a3b8;">🌐 API Timeout: {current_settings['api_timeout']}s</p>
    </div>
    """, unsafe_allow_html=True)

# App Information
st.markdown("""
<div class="glass-card" style="margin-top: 2rem; text-align: center;">
    <h4 style="color: #f8fafc; margin-bottom: 1rem;">About LumaAir</h4>
    <div style="display: flex; justify-content: space-around; text-align: center;">
        <div>
            <p style="color: #64748b; margin: 0; font-size: 0.8rem;">Version</p>
            <p style="color: #f8fafc; margin: 0; font-weight: 600;">v2.5.0</p>
        </div>
        <div>
            <p style="color: #64748b; margin: 0; font-size: 0.8rem;">Last Updated</p>
            <p style="color: #f8fafc; margin: 0; font-weight: 600;">Oct 2025</p>
        </div>
        <div>
            <p style="color: #64748b; margin: 0; font-size: 0.8rem;">AI Model</p>
            <p style="color: #f8fafc; margin: 0; font-weight: 600;">Gemini 2.5</p>
        </div>
        <div>
            <p style="color: #64748b; margin: 0; font-size: 0.8rem;">Data Sources</p>
            <p style="color: #f8fafc; margin: 0; font-weight: 600;">7 Sites</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div style="text-align: center; margin-top: 3rem; padding: 2rem; color: #64748b;">
    <p style="margin: 0; font-size: 0.9rem;">🌟 LumaAir - Advanced Air Quality Intelligence Platform</p>
    <p style="margin: 0.5rem 0 0 0; font-size: 0.8rem;">Powered by AI • Real-time Delhi Monitoring • Health-Focused Solutions</p>
</div>
""", unsafe_allow_html=True)