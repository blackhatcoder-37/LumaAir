# pages/4_🛒_Helpful_Products.py
import streamlit as st
import webbrowser

st.set_page_config(page_title="Helpful Products", page_icon="🛒", layout="wide")

def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_css("style.css")

# Custom CSS for clickable product cards
st.markdown("""
<style>
.product-card {
    background: rgba(20, 20, 40, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 15px;
    padding: 1rem;
    text-align: center;
    margin: 0.5rem 0;
    transition: all 0.3s ease;
    cursor: pointer;
    position: relative;
}

.product-card:hover {
    transform: translateY(-5px);
    background: rgba(30, 30, 50, 0.9);
    border: 1px solid rgba(255, 255, 255, 0.3);
    box-shadow: 0 8px 25px rgba(0, 192, 240, 0.3);
}

.product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 1rem;
}

.product-price {
    color: #00c0f0;
    font-size: 1.2rem;
    font-weight: bold;
    margin: 0.5rem 0;
}

.product-rating {
    color: #ffd700;
    margin: 0.5rem 0;
}

.shop-buttons {
    display: flex;
    gap: 0.5rem;
    margin-top: 1rem;
}
</style>
""", unsafe_allow_html=True)

st.title("🛒 Helpful Products for Better Air Quality")
st.markdown("#### Click the buttons below each product to shop on Amazon or Flipkart")

# Product data with real links
products = {
    "air_purifiers": [
        {
            "name": "Philips AC1215/20 Air Purifier",
            "image": "https://m.media-amazon.com/images/I/61B2mcDqNzL._SL1500_.jpg",
            "price": "₹14,995",
            "rating": "★★★★☆ 4.2",
            "description": "HEPA filter, covers 678 sq ft, removes 99.97% PM2.5",
            "amazon_link": "https://www.amazon.in/Philips-AC1215-Purifier-Numerical-Display/dp/B073TMQX7Y",
            "flipkart_link": "https://www.flipkart.com/philips-ac1215-20-portable-room-air-purifier/p/itmf2g3xgzthzdzz"
        },
        {
            "name": "Mi Air Purifier 3",
            "image": "https://m.media-amazon.com/images/I/61C+8HFL9jL._SL1500_.jpg",
            "price": "₹9,999",
            "rating": "★★★★☆ 4.1",
            "description": "360° air intake, OLED display, app control",
            "amazon_link": "https://www.amazon.in/Mi-Air-Purifier-filtration-Application/dp/B08C7DXD33",
            "flipkart_link": "https://www.flipkart.com/mi-air-purifier-3-portable-room-air-purifier/p/itm4a3c89674e5b3"
        },
        {
            "name": "Honeywell Air Touch A5",
            "image": "https://m.media-amazon.com/images/I/71qZF3XqXhL._SL1500_.jpg",
            "price": "₹17,990",
            "rating": "★★★★☆ 4.3",
            "description": "Pre-filter + HEPA + Activated Carbon, 388 sq ft",
            "amazon_link": "https://www.amazon.in/Honeywell-Air-Touch-Purifier-HPA5100WB/dp/B08T1JY8QH",
            "flipkart_link": "https://www.flipkart.com/honeywell-air-touch-a5-portable-room-air-purifier/p/itm5a9c2b2c0e346"
        }
    ],
    "masks": [
        {
            "name": "3M 8210 N95 Respirator Mask",
            "image": "https://m.media-amazon.com/images/I/71YLo6TKDRL._SL1500_.jpg",
            "price": "₹899 (Pack of 20)",
            "rating": "★★★★★ 4.5",
            "description": "NIOSH approved, 95% filtration, comfortable fit",
            "amazon_link": "https://www.amazon.in/3M-8210-Respirator-Mask-Pack/dp/B0899KQWYF",
            "flipkart_link": "https://www.flipkart.com/3m-8210-n95-respirator-mask/p/itmfb2a4c6cd8f5d"
        },
        {
            "name": "Cambridge N95 Face Mask",
            "image": "https://m.media-amazon.com/images/I/71M2VXFfX4L._SL1500_.jpg",
            "price": "₹1,299 (Pack of 25)",
            "rating": "★★★★☆ 4.0",
            "description": "6-layer protection, BIS certified, Indian brand",
            "amazon_link": "https://www.amazon.in/Cambridge-Basic-N95-Mask-Pack/dp/B08YN7HQXP",
            "flipkart_link": "https://www.flipkart.com/cambridge-basic-n95-mask/p/itm9a5b2f8e6d7c1"
        },
        {
            "name": "Dettol Cambridge N99 Anti-Pollution Mask",
            "image": "https://m.media-amazon.com/images/I/71BQZK5vY9L._SL1500_.jpg",
            "price": "₹399",
            "rating": "★★★★☆ 4.2",
            "description": "Washable, N99 protection, comfortable ear loops",
            "amazon_link": "https://www.amazon.in/Dettol-Cambridge-Anti-Pollution-Mask-N99/dp/B08CRMQ5XN",
            "flipkart_link": "https://www.flipkart.com/dettol-cambridge-n99-anti-pollution-mask/p/itm2f8e6b9c4a5d3"
        }
    ],
    "plants": [
        {
            "name": "Snake Plant (Sansevieria)",
            "image": "https://m.media-amazon.com/images/I/71uGNPU8pzL._SL1500_.jpg",
            "price": "₹299",
            "rating": "★★★★★ 4.8",
            "description": "Releases oxygen at night, low maintenance",
            "amazon_link": "https://www.amazon.in/Nurturing-Green-Snake-Plant-Sansevieria/dp/B07X7HMHQR",
            "flipkart_link": "https://www.flipkart.com/nurturing-green-snake-plant/p/itm3e5a7f9b2c4d1"
        },
        {
            "name": "Spider Plant (Chlorophytum)",
            "image": "https://m.media-amazon.com/images/I/61fGZHJK-AL._SL1500_.jpg",
            "price": "₹199",
            "rating": "★★★★☆ 4.6",
            "description": "Easy to grow, removes formaldehyde, pet-safe",
            "amazon_link": "https://www.amazon.in/Green-Spider-Plant-Chlorophytum-Comosum/dp/B08QVXN2LM",
            "flipkart_link": "https://www.flipkart.com/green-spider-plant/p/itm9b4c2a5f6e8d7"
        },
        {
            "name": "Peace Lily (Spathiphyllum)",
            "image": "https://m.media-amazon.com/images/I/71xMNBvP3aL._SL1500_.jpg",
            "price": "₹449",
            "rating": "★★★★☆ 4.4",
            "description": "Beautiful white flowers, removes toxic gases",
            "amazon_link": "https://www.amazon.in/Peace-Lily-Plant-Spathiphyllum-Indoor/dp/B08R8JXZMP",
            "flipkart_link": "https://www.flipkart.com/peace-lily-plant/p/itm5c6a9b2e7f4d8"
        }
    ]
}

# Display products by category
st.markdown("""
<div class="glass-card">
    <h3>💨 Air Purifiers</h3>
    <p>Professional-grade air purifiers to remove PM2.5, dust, and allergens from your home</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h5>💨 HEPA Air Purifiers</h5>
        <p><b>Purpose:</b> Remove 99.97% of particles ≥0.3 microns</p>
        <p><b>Best for:</b> PM2.5, dust, allergens, smoke</p>
        <p><b>Room size:</b> Choose based on CADR rating</p>
        <p><b>Price range:</b> ₹5,000 - ₹50,000</p>
        <p><b>Brands:</b> Philips, Xiaomi, Honeywell, Sharp</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h5>🌿 Air-Purifying Plants</h5>
        <p><b>Top choices:</b> Snake Plant, Spider Plant, Peace Lily</p>
        <p><b>Benefits:</b> Natural air filtering, oxygen production</p>
        <p><b>Maintenance:</b> Low to moderate watering</p>
        <p><b>Coverage:</b> 1-2 plants per 100 sq ft</p>
        <p><b>Cost:</b> ₹200 - ₹2,000 per plant</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h5>🌀 Exhaust Fans & Ventilation</h5>
        <p><b>Kitchen:</b> Remove cooking fumes and moisture</p>
        <p><b>Bathroom:</b> Control humidity and odors</p>
        <p><b>Features:</b> Low noise, energy efficient</p>
        <p><b>Installation:</b> Window or wall mounted</p>
        <p><b>Price:</b> ₹1,500 - ₹8,000</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>😷 Personal Protection</h3>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="info-card">
        <h5>😷 N95/KN95 Masks</h5>
        <p><b>Protection:</b> 95% filtration efficiency</p>
        <p><b>Use for:</b> PM2.5, pollution, allergens</p>
        <p><b>Duration:</b> Single-use or up to 8 hours</p>
        <p><b>Fit:</b> Proper seal around nose and mouth</p>
        <p><b>Cost:</b> ₹20 - ₹100 per mask</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h5>🕶️ Protective Eyewear</h5>
        <p><b>Purpose:</b> Shield eyes from pollution particles</p>
        <p><b>Features:</b> UV protection, wraparound design</p>
        <p><b>Best for:</b> Outdoor activities, cycling</p>
        <p><b>Materials:</b> Polycarbonate lenses</p>
        <p><b>Range:</b> ₹500 - ₹5,000</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="info-card">
        <h5>📱 Air Quality Monitors</h5>
        <p><b>Measures:</b> PM2.5, PM10, humidity, temperature</p>
        <p><b>Features:</b> Real-time data, app connectivity</p>
        <p><b>Benefits:</b> Track indoor air quality trends</p>
        <p><b>Brands:</b> IQAir, Dyson, Mi Air Monitor</p>
        <p><b>Price:</b> ₹3,000 - ₹25,000</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">
    <h3>🚗 Vehicle & Commute</h3>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="info-card">
        <h5>🚙 Car Air Purifiers</h5>
        <p><b>Installation:</b> Dashboard or cup holder mount</p>
        <p><b>Power:</b> 12V car adapter or USB</p>
        <p><b>Coverage:</b> Suitable for car cabin size</p>
        <p><b>Features:</b> HEPA filter, ionizer, compact design</p>
        <p><b>Brands:</b> Philips GoPure, Sharp, Kent</p>
        <p><b>Cost:</b> ₹2,000 - ₹15,000</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="info-card">
        <h5>🏍️ Anti-Pollution Masks for Bikers</h5>
        <p><b>Design:</b> Covers nose and mouth completely</p>
        <p><b>Features:</b> Replaceable filters, comfortable straps</p>
        <p><b>Protection:</b> PM2.5, exhaust fumes, dust</b>
        <p><b>Brands:</b> Cambridge, Vogmask, Atlanta Healthcare</p>
        <p><b>Duration:</b> Filters last 1-2 weeks with daily use</p>
        <p><b>Price:</b> ₹500 - ₹3,000</p>
    </div>
    """, unsafe_allow_html=True)

# Shopping recommendations
st.markdown("""
<div class="glass-card">
    <h3>🛍️ Where to Buy</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;">
            <h5>🌐 Online Platforms</h5>
            <p>Amazon, Flipkart, Nykaa<br>Wide selection, reviews, delivery</p>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;">
            <h5>🏪 Retail Stores</h5>
            <p>Croma, Reliance Digital<br>Physical inspection, immediate pickup</p>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;">
            <h5>🏥 Pharmacy Chains</h5>
            <p>Apollo, MedPlus<br>Masks, basic air monitors</p>
        </div>
        <div style="text-align: center; padding: 1rem; background: rgba(255,255,255,0.1); border-radius: 10px;">
            <h5>🌱 Nurseries</h5>
            <p>Local plant nurseries<br>Air-purifying plants, expert advice</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Budget planning
st.markdown("""
<div class="glass-card">
    <h3>💰 Budget Planning Guide</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="padding: 1rem; background: rgba(0,255,0,0.1); border-radius: 10px; border: 1px solid rgba(0,255,0,0.3);">
            <h5>🟢 Basic Protection (₹2,000-5,000)</h5>
            <ul>
                <li>N95 masks (pack of 50)</li>
                <li>2-3 air-purifying plants</li>
                <li>Basic exhaust fan</li>
            </ul>
        </div>
        <div style="padding: 1rem; background: rgba(255,255,0,0.1); border-radius: 10px; border: 1px solid rgba(255,255,0,0.3);">
            <h5>🟡 Moderate Setup (₹10,000-25,000)</h5>
            <ul>
                <li>Small room air purifier</li>
                <li>Air quality monitor</li>
                <li>Anti-pollution mask for commuting</li>
                <li>Car air purifier</li>
            </ul>
        </div>
        <div style="padding: 1rem; background: rgba(255,165,0,0.1); border-radius: 10px; border: 1px solid rgba(255,165,0,0.3);">
            <h5>🟠 Comprehensive (₹50,000+)</h5>
            <ul>
                <li>Whole-home air purification</li>
                <li>Smart air quality monitoring</li>
                <li>Premium protective gear</li>
                <li>Professional installation</li>
            </ul>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)