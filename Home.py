# Home.py - LumaAir Intelligence Platform with Live Predictions
import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
import requests
from theme_loader import apply_global_theme
from language_system import get_text
from live_prediction_engine import prediction_engine

st.set_page_config(page_title="LumaAir - Home", page_icon="🌬️", layout="wide")

# Initialize session state
if "app_theme" not in st.session_state:
    st.session_state.app_theme = "Dark"
if "app_language" not in st.session_state:
    st.session_state.app_language = "English"
if "app_units" not in st.session_state:
    st.session_state.app_units = "Metric"

def load_css_with_theme():
    """Load CSS with dynamic theme support"""
    if st.session_state.app_theme == "Light":
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 25%, #e2e8f0 50%, #f8fafc 75%, #ffffff 100%);
            background-attachment: fixed;
        }
        .stApp, .stApp div, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, 
        .stApp span, .stApp label, .stMarkdown, .stSelectbox label, .stButton label, .stSlider label {
            color: #1e293b !important;
        }
        .glass-card {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.9) 0%, rgba(248, 250, 252, 0.8) 100%);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 16px;
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            color: #1e293b !important;
        }
        .info-card {
            background: linear-gradient(145deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.9) 100%);
            border: 1px solid rgba(0, 0, 0, 0.1);
            border-radius: 12px;
            padding: 1.2rem;
            text-align: center;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.05);
            color: #1e293b !important;
        }
        .value { font-size: 1.8rem; font-weight: 700; color: #1e293b !important; }
        .label { color: #64748b !important; font-size: 0.9rem; font-weight: 600; }
        </style>
        """, unsafe_allow_html=True)
    else:
        try:
            with open("style.css") as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except:
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

# Apply theme and get translation function
apply_global_theme()
load_css_with_theme()
t = get_text

# Main title
st.markdown(f"""
<div class="glass-card" style="text-align: center; background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; margin-bottom: 2rem;">
    <h1 style="margin: 0; font-size: 2.5rem; font-weight: 800;">🌟 LumaAir Intelligence</h1>
    <p style="margin: 0.5rem 0 0 0; font-size: 1.1rem; opacity: 0.9;">Advanced Air Quality Forecasting Platform</p>
</div>
""", unsafe_allow_html=True)

# Enhanced sidebar
with st.sidebar:
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); color: white; padding: 1rem; border-radius: 12px; margin-bottom: 1rem; text-align: center;">
        <h3 style="margin: 0;">🎯 {t("monitoring_sites")}</h3>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 0.9rem;">Delhi NCR Network</p>
    </div>
    """, unsafe_allow_html=True)
    
    monitoring_sites = {
        "Site 1 (28.69536, 77.18168): Near Punjabi Bagh": "🏢 West Delhi",
        "Site 2 (28.5718, 77.07125): IGI Airport T3": "✈️ Airport Zone",
        "Site 3 (28.58278, 77.23441): Lodhi Colony Metro": "🚇 South Delhi",
        "Site 4 (28.82286, 77.10197): Haryana Border": "🌆 North Delhi",
        "Site 5 (28.53077, 77.27123): Okhla Industrial": "🏭 Industrial Zone",
        "Site 6 (28.72954, 77.09601): Rohini Metro": "🏘️ Northwest Delhi", 
        "Site 7 (28.71052, 77.24951): Burari Crossing": "🛣️ North Delhi"
    }
    
    selected_site = st.selectbox(
        "📍 Select Monitoring Location",
        options=list(monitoring_sites.keys()),
        format_func=lambda x: f"{monitoring_sites[x]} - {x.split(':')[1].strip()}"
    )
    
    if st.button("🚀 Generate Live Forecast", use_container_width=True, type="primary"):
        st.session_state.run_forecast = True
    
    st.markdown("---")
    
    st.markdown(f"""
    <div class="glass-card" style="padding: 1rem;">
        <h4 style="margin-bottom: 1rem;">📊 Network Status</h4>
        <div style="margin-bottom: 0.5rem;">🟢 <strong>7 Sites Online</strong></div>
        <div style="margin-bottom: 0.5rem;">⚡ <strong>Live Updates</strong></div>
        <div style="margin-bottom: 0.5rem;">🤖 <strong>AI Predictions</strong></div>
        <div>🌍 <strong>Multi-Language</strong></div>
    </div>
    """, unsafe_allow_html=True)

# Main content
if 'run_forecast' not in st.session_state:
    # Dashboard Welcome Section
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
            🚀 <strong>NEW: Live Weather Integration!</strong> Get precise O₃ and NO₂ predictions that update daily based on real weather conditions across Delhi's monitoring network.
        </p>
        <div style="background: rgba(59, 130, 246, 0.1); border: 1px solid rgba(59, 130, 246, 0.3); border-radius: 12px; padding: 1rem; margin-top: 1rem;">
            <p style="margin: 0; color: #3b82f6; font-weight: 600;">
                👈 Select a monitoring site from the sidebar and generate your live forecast
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #10b981, #059669); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">🎯</div>
            </div>
            <div class="label">Forecast Accuracy</div>
            <div class="value">24-Hour</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Live Weather Data</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #f59e0b, #d97706); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">🌍</div>
            </div>
            <div class="label">Monitoring Sites</div>
            <div class="value">7 Active</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Real Delhi Locations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="info-card">
            <div style="display: flex; align-items: center; justify-content: center; margin-bottom: 1rem;">
                <div style="background: linear-gradient(135deg, #8b5cf6, #7c3aed); border-radius: 50%; width: 50px; height: 50px; display: flex; align-items: center; justify-content: center; font-size: 1.5rem;">⚡</div>
            </div>
            <div class="label">Update Frequency</div>
            <div class="value">Live</div>
            <div style="color: #64748b; font-size: 0.8rem; margin-top: 0.5rem;">Changes Daily</div>
        </div>
        """, unsafe_allow_html=True)

else:
    # Live Forecast Generation
    st.markdown(f"""
    <div class="glass-card" style="text-align: center;">
        <h2 style="color: #f8fafc; margin-bottom: 0.5rem;">🎯 Live Forecast Results</h2>
        <p style="color: #94a3b8; margin-bottom: 1.5rem;">Location: {selected_site.split(':')[1].strip()}</p>
        <div style="background: linear-gradient(135deg, #3b82f6, #8b5cf6); border-radius: 12px; padding: 0.8rem; display: inline-block; margin-bottom: 1rem;">
            <span style="color: white; font-weight: 600;">🕐 Generated at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Generate LIVE predictions
    with st.spinner('🔄 Generating live predictions with real weather data...'):
        forecast_df = prediction_engine.calculate_live_predictions(selected_site)
        current_aqi = prediction_engine.get_current_aqi_status(selected_site)
        
        # Display live data status
        if forecast_df['Weather_Updated'].iloc[0]:
            st.success("✅ **Live Data Active**: Predictions updated with real weather conditions!")
        else:
            st.info("📡 **Backup Mode**: Using advanced time-based patterns")
    
    # Forecast display with tabs
    tab1, tab2 = st.tabs(["📈 Interactive Charts", "📋 Data Table"])
    
    with tab1:
        # Interactive plot
        fig = go.Figure()
        
        # Add O3 trace
        fig.add_trace(go.Scatter(
            x=forecast_df['Time'],
            y=forecast_df['O3 Prediction (ugm³)'],
            mode='lines+markers',
            name='O₃ (Ozone)',
            line=dict(width=4, color='#3b82f6'),
            marker=dict(size=8, color='#3b82f6')
        ))
        
        # Add NO2 trace
        fig.add_trace(go.Scatter(
            x=forecast_df['Time'],
            y=forecast_df['NO2 Prediction (ugm³)'],
            mode='lines+markers',
            name='NO₂ (Nitrogen Dioxide)',
            line=dict(width=4, color='#ef4444'),
            marker=dict(size=8, color='#ef4444')
        ))
        
        # Enhanced layout
        fig.update_layout(
            title=f"🌟 Live Air Quality Predictions - {selected_site.split(':')[1].strip()}",
            xaxis_title="Time",
            yaxis_title="Concentration (μg/m³)",
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        # Enhanced dataframe display
        st.dataframe(
            forecast_df.drop('Weather_Updated', axis=1),
            use_container_width=True,
            height=400
        )
        
        # Live Health Recommendations
        st.markdown("### 🏥 Live Health Recommendations")
        health_recs = prediction_engine.generate_health_recommendations(forecast_df)
        for rec in health_recs:
            st.markdown(f"- {rec}")
            
    # Current AQI Status (if available)
    if current_aqi:
        with st.expander("📊 Current Air Quality Index (Live)", expanded=False):
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Current NO₂", f"{current_aqi['current_no2']} μg/m³")
            with col2:
                st.metric("Current O₃", f"{current_aqi['current_o3']} μg/m³")
            with col3:
                st.metric("US EPA Index", current_aqi['us_epa_index'])
            with col4:
                st.metric("UK DEFRA Index", current_aqi['gb_defra_index'])
    
    # Generate new forecast button
    if st.button("🔄 Generate New Forecast", use_container_width=True):
        st.session_state.run_forecast = True
        st.rerun()

# Footer with settings
st.markdown("---")
footer_col1, footer_col2, footer_col3 = st.columns([2, 1, 1])

with footer_col1:
    st.markdown("""
    <div style="padding: 0.5rem;">
        <p style="margin: 0; color: #64748b; font-size: 0.9rem;">
            🌟 LumaAir Intelligence Platform- Advanced air quality forecasting with live weather integration.<br>
            🔬 Predictions update daily with real weather conditions from RapidAPI.
        </p>
    </div>
    """, unsafe_allow_html=True)

with footer_col2:
    # Theme selector with unique key
    theme_options = ["Dark", "Light", "Auto"]
    selected_theme = st.selectbox(
        "🎨 Theme",
        options=theme_options,
        index=theme_options.index(st.session_state.app_theme),
        key="main_theme_selector"
    )
    
    if selected_theme != st.session_state.app_theme:
        st.session_state.app_theme = selected_theme
        st.rerun()

with footer_col3:
    # Language selector with unique key
    language_options = ["English", "Hindi", "Spanish", "French"]
    selected_language = st.selectbox(
        "🌍 Language",
        options=language_options,
        index=language_options.index(st.session_state.app_language),
        key="main_language_selector"
    )
    
    if selected_language != st.session_state.app_language:
        st.session_state.app_language = selected_language
        st.rerun()
