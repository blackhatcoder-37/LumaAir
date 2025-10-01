# Home.py (Demo Version)
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

st.set_page_config(page_title="LumaAir - Home", page_icon="🌬️", layout="wide")

# Initialize theme settings
if "app_theme" not in st.session_state:
    st.session_state.app_theme = "Dark"
if "app_language" not in st.session_state:
    st.session_state.app_language = "English"
if "app_units" not in st.session_state:
    st.session_state.app_units = "Metric"

def load_css_with_theme():
    """Load CSS with dynamic theme support"""
    if st.session_state.app_theme == "Light":
        # Comprehensive Light theme CSS
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 25%, #e2e8f0 50%, #f8fafc 75%, #ffffff 100%);
            background-attachment: fixed;
        }
        
        /* Override all Streamlit text colors for light theme */
        .stApp, .stApp div, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, 
        .stApp span, .stApp label, .stMarkdown, .stSelectbox label, .stButton label, .stSlider label {
            color: #1e293b !important;
        }
        
        /* Sidebar styling for light theme */
        .css-1d391kg, .css-1lcbmhc, .css-1outpf7, .stSidebar {
            background-color: rgba(248, 250, 252, 0.95) !important;
            color: #1e293b !important;
        }
        
        .glass-card {
            background: rgba(255, 255, 255, 0.95) !important;
            backdrop-filter: blur(20px);
            border: 1px solid rgba(148, 163, 184, 0.3) !important;
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(15, 23, 42, 0.1) !important;
            color: #1e293b !important;
        }
        
        .glass-card h1, .glass-card h2, .glass-card h3, .glass-card h4, .glass-card h5, .glass-card h6,
        .glass-card p, .glass-card div, .glass-card span {
            color: #1e293b !important;
        }
        
        .info-card {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid rgba(148, 163, 184, 0.3) !important;
            border-radius: 12px;
            padding: 1rem;
            text-align: center;
            transition: all 0.3s ease;
            color: #1e293b !important;
        }
        
        .info-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 12px 40px rgba(15, 23, 42, 0.15) !important;
        }
        
        .info-card .label {
            color: #64748b !important;
            font-size: 0.9rem;
            font-weight: 600;
        }
        
        .info-card .value {
            color: #1e293b !important;
            font-size: 1.5rem;
            font-weight: 700;
        }
        
        /* Button styling for light theme */
        .stButton > button {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border: none !important;
        }
        
        /* Input field styling */
        .stSelectbox > div > div, .stSlider > div {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #1e293b !important;
        }
        </style>
        """, unsafe_allow_html=True)
    else:
        # Dark theme CSS (load from file)
        try:
            with open("style.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except:
            # Fallback dark theme
            st.markdown("""
            <style>
            .stApp {
                background: linear-gradient(135deg, #0f1419 0%, #1a2332 25%, #2d3748 50%, #1a202c 75%, #0f1419 100%);
                background-attachment: fixed;
            }
            .glass-card {
                background: linear-gradient(145deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%);
                backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                border-radius: 16px;
                padding: 1.5rem;
                margin: 1rem 0;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }
            </style>
            """, unsafe_allow_html=True)

# Apply theme and language system
from theme_loader import apply_global_theme
from language_system import t
apply_global_theme()

# Utility functions for unit conversions
def convert_temperature(temp_k, units="Metric"):
    """Convert temperature from Kelvin"""
    if units == "Imperial":
        # Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32
        temp_c = temp_k - 273.15
        temp_f = (temp_c * 9/5) + 32
        return f"{temp_f:.1f}°F"
    else:
        # Kelvin to Celsius: K - 273.15
        temp_c = temp_k - 273.15
        return f"{temp_c:.1f}°C"

def get_unit_symbol(units="Metric"):
    """Get appropriate unit symbols"""
    if units == "Imperial":
        return {"temp": "°F", "speed": "mph", "distance": "miles"}
    else:
        return {"temp": "°C", "speed": "km/h", "distance": "km"}

# --- Demo Data Generation ---
def generate_demo_forecast(site_id):
    """Generate realistic demo air quality forecast data"""
    hours = 24
    base_time = datetime.now()
    times = [base_time + timedelta(hours=i) for i in range(hours)]
    
    # Simulate realistic O3 and NO2 patterns
    np.random.seed(site_id)  # Different data per site
    
    # O3 typically peaks during midday, NO2 peaks during traffic hours
    o3_base = np.random.normal(45, 15, hours)
    no2_base = np.random.normal(35, 10, hours)
    
    # Add daily patterns
    for i, time in enumerate(times):
        hour = time.hour
        # O3 peaks around noon
        o3_multiplier = 1 + 0.3 * np.sin((hour - 6) * np.pi / 12)
        # NO2 peaks during rush hours
        if 7 <= hour <= 9 or 17 <= hour <= 19:
            no2_multiplier = 1.4
        else:
            no2_multiplier = 0.8
            
        o3_base[i] *= o3_multiplier
        no2_base[i] *= no2_multiplier
    
    # Ensure positive values
    o3_predictions = np.maximum(o3_base, 5)
    no2_predictions = np.maximum(no2_base, 5)
    
    return pd.DataFrame({
        'Time': times,
        'O3 Prediction (ugm³)': np.round(o3_predictions, 2),
        'NO2 Prediction (ugm³)': np.round(no2_predictions, 2)
    })

# --- UI & APP LOGIC ---
st.markdown("""
<div style="text-align: center; padding: 2rem 0; animation: fadeInUp 0.8s ease-out;">
    <h1 style="background: linear-gradient(135deg, #3b82f6 0%, #8b5cf6 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; font-size: 3.5rem; font-weight: 800; margin-bottom: 0.5rem; letter-spacing: -0.02em;">
        🌬️ LumaAir
    </h1>
    <p style="color: #94a3b8; font-size: 1.2rem; font-weight: 500; margin-bottom: 2rem;">
        Advanced Air Quality Intelligence Platform
    </p>
</div>
""", unsafe_allow_html=True)

# --- Modern Info Banner ---
st.markdown("""
<div style="background: linear-gradient(135deg, rgba(59, 130, 246, 0.1) 0%, rgba(139, 92, 246, 0.05) 100%); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 16px; padding: 1.5rem; margin: 2rem 0; text-align: center;">
    <div style="display: flex; align-items: center; justify-content: center; gap: 1rem;">
        <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center;">
            🚀
        </div>
        <div style="text-align: left;">
            <div style="color: #3b82f6; font-weight: 600; font-size: 1.1rem;">Demo Mode Active</div>
            <div style="color: #64748b; font-size: 0.9rem;">Powered by machine learning • Real-time forecasting • 7 monitoring zones</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.header(t("forecast_config"))
    
    site_options = {
        "Site 1 - Punjabi Bagh, West Delhi": 1,
        "Site 2 - IGI Airport, Southwest Delhi": 2,
        "Site 3 - Lodhi Colony, South Delhi": 3,
        "Site 4 - North Delhi (Haryana Border)": 4,
        "Site 5 - Okhla, Southeast Delhi": 5,
        "Site 6 - Rohini, Northwest Delhi": 6,
        "Site 7 - Burari, North Delhi": 7
    }
    selected_site_name = st.selectbox(t("select_site"), options=list(site_options.keys()))
    selected_site_id = site_options[selected_site_name]
    
    # Display coordinates for selected site
    site_coordinates = {
        1: (28.69536, 77.18168),
        2: (28.5718, 77.07125), 
        3: (28.58278, 77.23441),
        4: (28.82286, 77.10197),
        5: (28.53077, 77.27123),
        6: (28.72954, 77.09601),
        7: (28.71052, 77.24951)
    }
    
    lat, lon = site_coordinates[selected_site_id]
    st.markdown(f"""
    <div style="background: rgba(59, 130, 246, 0.1); border-left: 3px solid #3b82f6; padding: 0.75rem; border-radius: 5px; margin: 1rem 0;">
        <p style="margin: 0; color: #3b82f6; font-weight: 600; font-size: 0.9rem;">📍 Coordinates</p>
        <p style="margin: 0; color: #64748b; font-size: 0.8rem;">Lat: {lat}°, Lon: {lon}°</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown(f"**{t('forecast_params')}**")
    st.markdown(f"• **{t('duration')}**")
    st.markdown(f"• **{t('pollutants')}**")
    st.markdown(f"• **{t('update_freq')}**")
    
    if st.button(t("generate_forecast"), use_container_width=True):
        st.session_state['run_forecast'] = True
        st.session_state['site_id'] = selected_site_id
        st.session_state['site_name'] = selected_site_name

# --- Main Dashboard ---
if 'run_forecast' not in st.session_state:
    # --- Dashboard Welcome Section ---
    st.markdown(f"""
    <div class="glass-card" style="text-align: center; margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 1.5rem;">
            <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 12px; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; font-size: 1.8rem;">
                🌟
            </div>
            <div style="text-align: left;">
                <h3 style="margin: 0; color: #f8fafc; font-size: 1.5rem; font-weight: 700;">{t("welcome_title")}</h3>
                <p style="margin: 0; color: #94a3b8; font-size: 0.95rem;">{t("welcome_subtitle")}</p>
            </div>
        </div>
        <p style="color: #cbd5e1; font-size: 1rem; line-height: 1.6; margin-bottom: 1.5rem;">
            Harness the power of machine learning to get precise O₃ and NO₂ concentration predictions across Delhi's monitoring network. Make informed decisions about outdoor activities and health protection.
        </p>
        <div style="background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 12px; padding: 1rem; margin-top: 1rem;">
            <p style="margin: 0; color: #3b82f6; font-weight: 600;">
                👈 Select a monitoring site from the sidebar and generate your forecast
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # --- Modern Stats Cards ---
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #10b981, #059669); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                    🎯
                </div>
            </div>
            <div class="label">Forecast Accuracy</div>
            <div class="value">24-Hour</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Advanced ML Models</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                    🏢
                </div>
            </div>
            <div class="label">Monitoring Network</div>
            <div class="value">7 Zones</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Delhi NCR Coverage</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                    🧪
                </div>
            </div>
            <div class="label">Pollutants Tracked</div>
            <div class="value">O₃ & NO₂</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Real-time Analysis</div>
        </div>
        """, unsafe_allow_html=True)

else:
    site_id = st.session_state['site_id']
    site_name = st.session_state['site_name']

    with st.spinner(f"🔮 Generating forecast for {site_name}..."):
        # Generate demo forecast data
        forecast_df = generate_demo_forecast(site_id)
        
        # --- Modern Dashboard Results Header ---
        st.markdown(f"""
        <div class="glass-card" style="text-align: center; margin-bottom: 2rem;">
            <div style="display: flex; align-items: center; justify-content: center; gap: 1rem; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #059669, #10b981); border-radius: 12px; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                    📊
                </div>
                <div style="text-align: left;">
                    <h3 style="margin: 0; color: #f8fafc; font-size: 1.4rem; font-weight: 700;">Air Quality Forecast</h3>
                    <p style="margin: 0; color: #94a3b8; font-size: 0.9rem;">{site_name} • Next 24 Hours</p>
                </div>
            </div>
            <div style="background: rgba(16, 185, 129, 0.1); border: 1px solid rgba(16, 185, 129, 0.3); border-radius: 10px; padding: 0.75rem; margin-top: 1rem;">
                <p style="margin: 0; color: #10b981; font-weight: 500; font-size: 0.9rem;">
                    ✅ Forecast generated successfully • Updated now
                </p>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # KPI Metrics
        avg_o3 = forecast_df['O3 Prediction (ugm³)'].mean()
        avg_no2 = forecast_df['NO2 Prediction (ugm³)'].mean()
        max_o3 = forecast_df['O3 Prediction (ugm³)'].max()
        peak_o3_time = forecast_df.loc[forecast_df['O3 Prediction (ugm³)'].idxmax()]['Time'].strftime('%I:%M %p')
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            # Determine O3 status color
            o3_color = "#10b981" if avg_o3 < 60 else "#f59e0b" if avg_o3 < 120 else "#ef4444"
            st.markdown(f"""
            <div class="info-card">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                    <div style="background: linear-gradient(135deg, {o3_color}, {o3_color}90); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                        💨
                    </div>
                </div>
                <div class="label">Avg O₃ Concentration</div>
                <div class="value">{avg_o3:.1f} <span style="font-size: 0.8em;">μg/m³</span></div>
                <div style="color: {o3_color}; font-size: 0.8rem; font-weight: 600; margin-top: 0.5rem;">
                    {"Good" if avg_o3 < 60 else "Moderate" if avg_o3 < 120 else "Unhealthy"}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # Determine NO2 status color
            no2_color = "#10b981" if avg_no2 < 40 else "#f59e0b" if avg_no2 < 80 else "#ef4444"
            st.markdown(f"""
            <div class="info-card">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                    <div style="background: linear-gradient(135deg, {no2_color}, {no2_color}90); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                        🏭
                    </div>
                </div>
                <div class="label">Avg NO₂ Concentration</div>
                <div class="value">{avg_no2:.1f} <span style="font-size: 0.8em;">μg/m³</span></div>
                <div style="color: {no2_color}; font-size: 0.8rem; font-weight: 600; margin-top: 0.5rem;">
                    {"Good" if avg_no2 < 40 else "Moderate" if avg_no2 < 80 else "Unhealthy"}
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class="info-card">
                <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                    <div style="background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">
                        ⚠️
                    </div>
                </div>
                <div class="label">Peak O₃ Expected</div>
                <div class="value">{peak_o3_time}</div>
                <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">
                    Max: {max_o3:.1f} μg/m³
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.divider()

        # Chart and Data Tabs with Modern Design
        st.markdown("""
        <div style="margin: 2rem 0;">
            <h3 style="color: #1e293b; margin-bottom: 1.5rem; text-align: center; font-weight: 700; font-size: 1.4rem;">
                📊 Detailed Forecast Analysis
            </h3>
        </div>
        """, unsafe_allow_html=True)
        
        tab1, tab2 = st.tabs(["📈 Interactive Chart", "📄 Raw Data"])

        with tab1:
            # Enhanced chart with modern styling
            fig = px.line(forecast_df, x='Time', y=['O3 Prediction (ugm³)', 'NO2 Prediction (ugm³)'],
                          title="Air Quality Prediction Timeline", 
                          markers=True, 
                          template="plotly_white")
            
            # Modern chart styling
            fig.update_layout(
                title={
                    'text': "🔮 Pollutant Concentration Forecast",
                    'x': 0.5,
                    'xanchor': 'center',
                    'font': {'size': 20, 'color': '#1e293b', 'family': 'Arial, sans-serif'}
                },
                xaxis_title="Time Period", 
                yaxis_title="Concentration (μg/m³)", 
                legend_title="Pollutant Type",
                paper_bgcolor='rgba(248, 250, 252, 0.8)', 
                plot_bgcolor='rgba(255, 255, 255, 0.9)',
                font=dict(color='#1e293b', size=12),
                margin=dict(l=20, r=20, t=80, b=20),
                height=500,
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1,
                    bgcolor="rgba(255, 255, 255, 0.8)",
                    bordercolor="rgba(0, 0, 0, 0.1)",
                    borderwidth=1
                )
            )
            
            # Enhanced trace styling
            fig.update_traces(
                line=dict(width=4),
                marker=dict(size=8, line=dict(width=2, color='white')),
                hovertemplate="<b>%{fullData.name}</b><br>Time: %{x}<br>Concentration: %{y:.1f} μg/m³<extra></extra>"
            )
            
            # Color scheme for pollutants
            colors = ['#3b82f6', '#ef4444']  # Blue for O3, Red for NO2
            for i, trace in enumerate(fig.data):
                trace.line.color = colors[i % len(colors)]
                trace.marker.color = colors[i % len(colors)]
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.markdown("""
            <div class="glass-card" style="padding: 1.5rem;">
                <h4 style="color: #1e293b; margin-bottom: 1rem;">📋 Detailed Forecast Dataset</h4>
                <p style="color: #64748b; margin-bottom: 1rem;">Complete hourly predictions for the next 24 hours</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Enhanced dataframe display
            st.dataframe(
                forecast_df,
                use_container_width=True,
                height=400,
                column_config={
                    "Time": st.column_config.DatetimeColumn("🕐 Time"),
                    "O3 Prediction (ugm³)": st.column_config.NumberColumn(
                        "💨 O₃ Level",
                        help="Ozone concentration prediction",
                        format="%.1f μg/m³"
                    ),
                    "NO2 Prediction (ugm³)": st.column_config.NumberColumn(
                        "🏭 NO₂ Level", 
                        help="Nitrogen dioxide concentration prediction",
                        format="%.1f μg/m³"
                    )
                }
            )
            
        # --- Health Advisory ---
        st.markdown("""
        <div class="glass-card">
            <h4>💡 Health Advisory</h4>
            <p><b>Current Conditions:</b> Based on predicted levels, outdoor activities are generally safe with normal precautions.</p>
            <p><b>Recommendations:</b></p>
            <ul>
                <li>🏃‍♂️ Exercise outdoors during early morning hours when O₃ levels are typically lower</li>
                <li>😷 Consider wearing a mask if you have respiratory sensitivities</li>
                <li>🚗 Limit vehicle use during peak pollution hours</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

# --- SETTINGS FOOTER SECTION ---
st.markdown(f"""
<div style="margin-top: 4rem; border-top: 1px solid rgba(255, 255, 255, 0.1); padding-top: 3rem;">
    <div class="glass-card" style="text-align: center; margin-bottom: 2rem;">
        <h3 style="color: #f8fafc; margin-bottom: 1rem; display: flex; align-items: center; justify-content: center; gap: 0.5rem;">
            <span style="background: linear-gradient(135deg, #6366f1, #8b5cf6); border-radius: 8px; width: 32px; height: 32px; display: flex; align-items: center; justify-content: center; font-size: 0.9rem;">⚙️</span>
            {t("settings_title")}
        </h3>
    </div>
</div>
""", unsafe_allow_html=True)

# Settings Footer - Two Column Layout
col_left, col_right = st.columns(2)

with col_left:
    st.markdown(f"""
    <div class="glass-card">
        <h4 style="color: #3b82f6; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🎨</span> {t("app_preferences")}
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    # Theme Selector with instant switching
    theme_options = ["Dark", "Light", "Auto"]
    current_theme = st.session_state.app_theme
    
    selected_theme = st.selectbox(
        t("theme"), 
        theme_options,
        index=theme_options.index(current_theme) if current_theme in theme_options else 0,
        key="theme_selector"
    )
    
    # Apply theme change immediately
    if selected_theme != st.session_state.app_theme:
        st.session_state.app_theme = selected_theme
        st.rerun()
    
    # Language selector
    language_options = ["English", "Hindi", "Spanish", "French"]
    selected_language = st.selectbox(
        t("language"), 
        language_options,
        index=language_options.index(st.session_state.app_language) if st.session_state.app_language in language_options else 0,
        key="language_selector"
    )
    
    # Apply language change immediately and reload interface
    if selected_language != st.session_state.app_language:
        st.session_state.app_language = selected_language
        st.rerun()
    
    # Units selector  
    units_options = ["Metric", "Imperial"]
    selected_units = st.selectbox(
        t("units"), 
        units_options,
        index=units_options.index(st.session_state.app_units) if st.session_state.app_units in units_options else 0,
        key="units_selector"
    )
    st.session_state.app_units = selected_units
    
    st.markdown(f"""
    <div class="glass-card" style="margin-top: 1rem;">
        <h4 style="color: #10b981; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🔔</span> {t("notifications")}
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    col_btn1, col_btn2 = st.columns(2)
    with col_btn1:
        if st.button(t("refresh_data"), use_container_width=True, key="refresh_footer"):
            # Clear cache and refresh
            st.cache_data.clear()
            st.toast("🔄 Data refreshed successfully!", icon="✅")
    
    with col_btn2:
        if st.button(t("save_prefs"), use_container_width=True, key="save_footer"):
            st.success(f"✅ Preferences Saved Successfully!")
            st.info(f"🌙 **{t('theme')}**: {st.session_state.app_theme}\n🌐 **{t('language')}**: {st.session_state.app_language}\n📏 **{t('units')}**: {st.session_state.app_units}")
            st.balloons()

with col_right:
    st.markdown(f"""
    <div class="glass-card">
        <h4 style="color: #f59e0b; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>📊</span> {t("app_info")}
        </h4>
    </div>
    """, unsafe_allow_html=True)
    
    # App Stats and Info
    st.markdown(f"""
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1rem; margin: 1rem 0;">
        <div style="background: rgba(59, 130, 246, 0.1); border-left: 3px solid #3b82f6; padding: 1rem; border-radius: 8px;">
            <p style="margin: 0; color: #3b82f6; font-weight: 600; font-size: 0.9rem;">{t("version")}</p>
            <p style="margin: 0; color: #f8fafc; font-size: 1.1rem; font-weight: 700;">v2.5.0</p>
        </div>
        <div style="background: rgba(16, 185, 129, 0.1); border-left: 3px solid #10b981; padding: 1rem; border-radius: 8px;">
            <p style="margin: 0; color: #10b981; font-weight: 600; font-size: 0.9rem;">{t("ai_model")}</p>
            <p style="margin: 0; color: #f8fafc; font-size: 1.1rem; font-weight: 700;">Gemini 2.5</p>
        </div>
        <div style="background: rgba(245, 158, 11, 0.1); border-left: 3px solid #f59e0b; padding: 1rem; border-radius: 8px;">
            <p style="margin: 0; color: #f59e0b; font-weight: 600; font-size: 0.9rem;">{t("data_sites")}</p>
            <p style="margin: 0; color: #f8fafc; font-size: 1.1rem; font-weight: 700;">7 Locations</p>
        </div>
        <div style="background: rgba(139, 92, 246, 0.1); border-left: 3px solid #8b5cf6; padding: 1rem; border-radius: 8px;">
            <p style="margin: 0; color: #8b5cf6; font-weight: 600; font-size: 0.9rem;">{t("active_theme")}</p>
            <p style="margin: 0; color: #f8fafc; font-size: 1.1rem; font-weight: 700;">{st.session_state.app_theme} Mode</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card" style="margin-top: 1rem;">
        <h4 style="color: #ef4444; margin-bottom: 1rem; display: flex; align-items: center; gap: 0.5rem;">
            <span>🌐</span> Quick Links
        </h4>
        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap;">
            <button onclick="window.open('https://github.com/lumaair', '_blank')" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; font-size: 0.8rem;">📂 GitHub</button>
            <button onclick="window.open('https://docs.lumaair.com', '_blank')" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; font-size: 0.8rem;">📚 Docs</button>
            <button onclick="window.open('https://support.lumaair.com', '_blank')" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem 1rem; border-radius: 8px; cursor: pointer; font-size: 0.8rem;">💬 Support</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Final Footer
st.markdown(f"""
<div style="text-align: center; margin-top: 3rem; padding: 2rem 0; border-top: 1px solid rgba(255, 255, 255, 0.1);">
    <div style="margin-bottom: 1rem;">
        <div style="display: inline-flex; align-items: center; gap: 1rem; background: rgba(20, 20, 40, 0.8); padding: 1rem 2rem; border-radius: 50px; border: 1px solid rgba(255, 255, 255, 0.1);">
            <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 50%; width: 40px; height: 40px; display: flex; align-items: center; justify-content: center; font-size: 1.2rem;">🌟</div>
            <div style="text-align: left;">
                <h4 style="margin: 0; color: #f8fafc; font-size: 1rem; font-weight: 700;">{t("app_title")}</h4>
                <p style="margin: 0; color: #94a3b8; font-size: 0.8rem;">{t("tagline")}</p>
            </div>
        </div>
    </div>
    <p style="color: #64748b; margin: 0.5rem 0; font-size: 0.85rem;">{t("powered_by")}</p>
    <p style="color: #475569; margin: 0; font-size: 0.75rem;">{t("copyright")}</p>
</div>
""", unsafe_allow_html=True)