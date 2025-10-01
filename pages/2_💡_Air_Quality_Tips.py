# pages/2_💡_Air_Quality_Tips.py
import streamlit as st

st.set_page_config(page_title="Air Quality Tips", page_icon="💡", layout="wide")

from theme_loader import apply_global_theme
apply_global_theme()

st.title("💡 Tips to Improve Air Quality")
st.markdown("#### Practical advice to breathe cleaner air and reduce pollution")

st.markdown("""
<div class="glass-card">
    <h3>🏠 Indoor Air Quality</h3>
    <ul>
        <li><b>Ventilate your home:</b> Open windows for a few minutes each day to allow fresh air to circulate.</li>
        <li><b>Use exhaust fans:</b> Turn on fans in kitchens and bathrooms to remove cooking fumes and moisture.</li>
        <li><b>Clean regularly:</b> Dust, vacuum, and mop to remove particulate matter and allergens.</li>
        <li><b>Get houseplants:</b> Plants like Snake Plants, Spider Plants, and Peace Lilies are known to filter indoor air.</li>
        <li><b>Avoid indoor smoking:</b> Cigarette smoke significantly degrades indoor air quality.</li>
        <li><b>Use air purifiers:</b> HEPA filters can remove fine particles from indoor air.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>🌍 Outdoor Air Quality & Personal Safety</h3>
    <ul>
        <li><b>Use public transport, cycle, or walk:</b> Reduce reliance on personal vehicles, especially during high-pollution days.</li>
        <li><b>Conserve energy:</b> Turn off lights and electronics when not in use.</li>
        <li><b>Check AQI daily:</b> Use your LumaAir forecast to plan your outdoor activities.</li>
        <li><b>Wear a mask:</b> Use N95 or equivalent masks when going outside on high-pollution days.</li>
        <li><b>Time your outdoor activities:</b> Early morning and late evening typically have better air quality.</li>
        <li><b>Avoid burning waste:</b> Never burn garbage, leaves, or other materials.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>🚗 Transportation Tips</h3>
    <ul>
        <li><b>Carpool or use shared rides:</b> Reduce the number of vehicles on the road.</li>
        <li><b>Maintain your vehicle:</b> Regular maintenance improves fuel efficiency and reduces emissions.</li>
        <li><b>Choose cleaner routes:</b> Avoid highly congested roads when possible.</li>
        <li><b>Consider electric vehicles:</b> EVs produce zero local emissions.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>🌱 Community Actions</h3>
    <ul>
        <li><b>Plant trees:</b> Trees absorb pollutants and produce oxygen.</li>
        <li><b>Support clean energy:</b> Advocate for renewable energy sources in your community.</li>
        <li><b>Reduce waste:</b> Less waste means less burning and fewer landfills.</li>
        <li><b>Educate others:</b> Share knowledge about air quality and its health impacts.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# --- Quick AQI Reference ---
st.divider()
st.subheader("📊 Quick AQI Reference")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card" style="background: rgba(0, 255, 0, 0.2);">
        <div class="label">Good (0-50)</div>
        <div class="value">🟢 Safe</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card" style="background: rgba(255, 255, 0, 0.2);">
        <div class="label">Moderate (51-100)</div>
        <div class="value">🟡 Caution</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card" style="background: rgba(255, 0, 0, 0.2);">
        <div class="label">Unhealthy (101+)</div>
        <div class="value">🔴 Avoid</div>
    </div>
    """, unsafe_allow_html=True)