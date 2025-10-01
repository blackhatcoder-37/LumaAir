# pages/4_🛒_Helpful_Products.py
import streamlit as st

st.set_page_config(page_title="Helpful Products", page_icon="🛒", layout="wide")

from theme_loader import apply_global_theme
apply_global_theme()

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
    font-size: 0.9rem;
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
            "rating": "★★★★☆ 4.2/5",
            "description": "HEPA filter, covers 678 sq ft, removes 99.97% PM2.5",
            "amazon_link": "https://www.amazon.in/s?k=Philips+AC1215+air+purifier",
            "flipkart_link": "https://www.flipkart.com/search?q=philips%20ac1215%20air%20purifier"
        },
        {
            "name": "Mi Air Purifier 3",
            "image": "https://m.media-amazon.com/images/I/61C+8HFL9jL._SL1500_.jpg",
            "price": "₹9,999",
            "rating": "★★★★☆ 4.1/5",
            "description": "360° air intake, OLED display, app control",
            "amazon_link": "https://www.amazon.in/s?k=Mi+air+purifier+3",
            "flipkart_link": "https://www.flipkart.com/search?q=mi%20air%20purifier%203"
        },
        {
            "name": "Honeywell Air Touch A5",
            "image": "https://m.media-amazon.com/images/I/71qZF3XqXhL._SL1500_.jpg",
            "price": "₹17,990",
            "rating": "★★★★☆ 4.3/5",
            "description": "Pre-filter + HEPA + Activated Carbon, 388 sq ft",
            "amazon_link": "https://www.amazon.in/s?k=Honeywell+Air+Touch+A5+purifier",
            "flipkart_link": "https://www.flipkart.com/search?q=honeywell%20air%20touch%20a5%20purifier"
        }
    ],
    "masks": [
        {
            "name": "3M 8210 N95 Respirator Mask",
            "image": "https://m.media-amazon.com/images/I/71YLo6TKDRL._SL1500_.jpg",
            "price": "₹899 (Pack of 20)",
            "rating": "★★★★★ 4.5/5",
            "description": "NIOSH approved, 95% filtration, comfortable fit",
            "amazon_link": "https://www.amazon.in/s?k=3M+8210+N95+mask",
            "flipkart_link": "https://www.flipkart.com/search?q=3m%20n95%20mask"
        },
        {
            "name": "Cambridge N95 Face Mask",
            "image": "https://m.media-amazon.com/images/I/71M2VXFfX4L._SL1500_.jpg",
            "price": "₹1,299 (Pack of 25)",
            "rating": "★★★★☆ 4.0/5",
            "description": "6-layer protection, BIS certified, Indian brand",
            "amazon_link": "https://www.amazon.in/s?k=Cambridge+N95+mask",
            "flipkart_link": "https://www.flipkart.com/search?q=cambridge%20n95%20mask"
        },
        {
            "name": "Dettol Cambridge N99 Anti-Pollution Mask",
            "image": "https://m.media-amazon.com/images/I/71BQZK5vY9L._SL1500_.jpg",
            "price": "₹399",
            "rating": "★★★★☆ 4.2/5",
            "description": "Washable, N99 protection, comfortable ear loops",
            "amazon_link": "https://www.amazon.in/s?k=Dettol+N99+anti+pollution+mask",
            "flipkart_link": "https://www.flipkart.com/search?q=dettol%20n99%20mask"
        }
    ],
    "plants": [
        {
            "name": "Snake Plant (Sansevieria)",
            "image": "https://m.media-amazon.com/images/I/71uGNPU8pzL._SL1500_.jpg",
            "price": "₹299",
            "rating": "★★★★★ 4.8/5",
            "description": "Releases oxygen at night, low maintenance",
            "amazon_link": "https://www.amazon.in/s?k=snake+plant+sansevieria",
            "flipkart_link": "https://www.flipkart.com/search?q=snake%20plant%20sansevieria"
        },
        {
            "name": "Spider Plant (Chlorophytum)",
            "image": "https://m.media-amazon.com/images/I/61fGZHJK-AL._SL1500_.jpg",
            "price": "₹199",
            "rating": "★★★★☆ 4.6/5",
            "description": "Easy to grow, removes formaldehyde, pet-safe",
            "amazon_link": "https://www.amazon.in/s?k=spider+plant+chlorophytum",
            "flipkart_link": "https://www.flipkart.com/search?q=spider%20plant%20chlorophytum"
        },
        {
            "name": "Peace Lily (Spathiphyllum)",
            "image": "https://m.media-amazon.com/images/I/71xMNBvP3aL._SL1500_.jpg",
            "price": "₹449",
            "rating": "★★★★☆ 4.4/5",
            "description": "Beautiful white flowers, removes toxic gases",
            "amazon_link": "https://www.amazon.in/s?k=peace+lily+plant+spathiphyllum",
            "flipkart_link": "https://www.flipkart.com/search?q=peace%20lily%20plant"
        }
    ]
}

# Display Air Purifiers
st.markdown("""
<div class="glass-card">
    <h3>💨 Air Purifiers</h3>
    <p>Professional-grade air purifiers to remove PM2.5, dust, and allergens from your home</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i, product in enumerate(products["air_purifiers"]):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{product['image']}" class="product-image" alt="{product['name']}">
            <h5 style="color: white; margin: 1rem 0 0.5rem 0;">{product['name']}</h5>
            <div class="product-rating">{product['rating']}</div>
            <div class="product-price">{product['price']}</div>
            <p style="font-size: 0.9rem; color: #b0b0b0; margin: 0.5rem 0;">{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛒 Buy on Amazon", key=f"amazon_purifier_{i}", use_container_width=True):
                st.success(f"Opening Amazon for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Amazon]({product['amazon_link']})**")
        with col2:
            if st.button("🛍️ Buy on Flipkart", key=f"flipkart_purifier_{i}", use_container_width=True):
                st.success(f"Opening Flipkart for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Flipkart]({product['flipkart_link']})**")

st.divider()

# Display Masks
st.markdown("""
<div class="glass-card">
    <h3>😷 N95/N99 Masks</h3>
    <p>High-quality respiratory protection masks for daily commute and outdoor activities</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i, product in enumerate(products["masks"]):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{product['image']}" class="product-image" alt="{product['name']}">
            <h5 style="color: white; margin: 1rem 0 0.5rem 0;">{product['name']}</h5>
            <div class="product-rating">{product['rating']}</div>
            <div class="product-price">{product['price']}</div>
            <p style="font-size: 0.9rem; color: #b0b0b0; margin: 0.5rem 0;">{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛒 Buy on Amazon", key=f"amazon_mask_{i}", use_container_width=True):
                st.success(f"Opening Amazon for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Amazon]({product['amazon_link']})**")
        with col2:
            if st.button("🛍️ Buy on Flipkart", key=f"flipkart_mask_{i}", use_container_width=True):
                st.success(f"Opening Flipkart for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Flipkart]({product['flipkart_link']})**")

st.divider()

# Display Plants
st.markdown("""
<div class="glass-card">
    <h3>🌿 Air-Purifying Plants</h3>
    <p>Natural air purifiers that remove toxins and produce fresh oxygen for your home</p>
</div>
""", unsafe_allow_html=True)

cols = st.columns(3)
for i, product in enumerate(products["plants"]):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="product-card">
            <img src="{product['image']}" class="product-image" alt="{product['name']}">
            <h5 style="color: white; margin: 1rem 0 0.5rem 0;">{product['name']}</h5>
            <div class="product-rating">{product['rating']}</div>
            <div class="product-price">{product['price']}</div>
            <p style="font-size: 0.9rem; color: #b0b0b0; margin: 0.5rem 0;">{product['description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🛒 Buy on Amazon", key=f"amazon_plant_{i}", use_container_width=True):
                st.success(f"Opening Amazon for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Amazon]({product['amazon_link']})**")
        with col2:
            if st.button("🛍️ Buy on Flipkart", key=f"flipkart_plant_{i}", use_container_width=True):
                st.success(f"Opening Flipkart for {product['name']}...")
                st.markdown(f"**[🔗 Click here to open Flipkart]({product['flipkart_link']})**")

# Shopping tips
st.markdown("""
<div class="glass-card">
    <h3>💡 Smart Shopping Tips</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; margin-top: 1rem;">
        <div style="padding: 1rem; background: rgba(0,255,0,0.1); border-radius: 10px; border: 1px solid rgba(0,255,0,0.3);">
            <h5>🎯 Compare Prices</h5>
            <p>Check both Amazon and Flipkart for best deals. Prices can vary significantly between platforms.</p>
        </div>
        <div style="padding: 1rem; background: rgba(255,255,0,0.1); border-radius: 10px; border: 1px solid rgba(255,255,0,0.3);">
            <h5>⭐ Read Reviews</h5>
            <p>Always check user reviews and ratings before purchasing. Look for verified purchase reviews.</p>
        </div>
        <div style="padding: 1rem; background: rgba(255,165,0,0.1); border-radius: 10px; border: 1px solid rgba(255,165,0,0.3);">
            <h5>🏷️ Watch for Sales</h5>
            <p>Best deals during festival seasons, Big Billion Days, Great Indian Festival sales.</p>
        </div>
        <div style="padding: 1rem; background: rgba(0,192,240,0.1); border-radius: 10px; border: 1px solid rgba(0,192,240,0.3);">
            <h5>📦 Check Warranty</h5>
            <p>Ensure products come with manufacturer warranty and check return/exchange policies.</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)