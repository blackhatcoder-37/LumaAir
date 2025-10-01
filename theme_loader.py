# theme_loader.py - Shared theme system for all pages
import streamlit as st

def apply_global_theme():
    """Apply theme to all pages based on session state"""
    # Initialize theme if not exists
    if "app_theme" not in st.session_state:
        st.session_state.app_theme = "Dark"
    
    if st.session_state.app_theme == "Light":
        # Comprehensive Light theme CSS
        st.markdown("""
        <style>
        .stApp {
            background: linear-gradient(135deg, #ffffff 0%, #f8fafc 25%, #e2e8f0 50%, #f8fafc 75%, #ffffff 100%) !important;
            background-attachment: fixed;
        }
        
        /* Override all text colors for light theme */
        .stApp, .stApp div, .stApp p, .stApp h1, .stApp h2, .stApp h3, .stApp h4, .stApp h5, .stApp h6, 
        .stApp span, .stApp label, .stMarkdown, .stSelectbox label, .stButton label, .stSlider label,
        .stTextInput label, .stTextArea label, .stChatMessage div {
            color: #1e293b !important;
        }
        
        /* Transparent sidebar styling for light theme */
        .css-1d391kg, .css-1lcbmhc, .css-1outpf7, .stSidebar, .css-1cypcdb {
            background-color: rgba(248, 250, 252, 0.3) !important;
            backdrop-filter: blur(15px) !important;
            border-right: 1px solid rgba(148, 163, 184, 0.2) !important;
            color: #1e293b !important;
        }
        
        /* Chat message styling for light theme */
        .stChatMessage {
            background-color: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid rgba(148, 163, 184, 0.2) !important;
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
        }
        
        .info-card .value {
            color: #1e293b !important;
        }
        
        /* Button styling for light theme */
        .stButton > button {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border: none !important;
        }
        
        /* Input and form styling */
        .stSelectbox > div > div, .stSlider > div, .stTextInput > div > div, .stTextArea > div > div {
            background-color: rgba(255, 255, 255, 0.9) !important;
            color: #1e293b !important;
            border: 1px solid rgba(148, 163, 184, 0.3) !important;
        }
        
        /* Product card styling for light theme */
        .product-card {
            background: rgba(255, 255, 255, 0.9) !important;
            border: 1px solid rgba(148, 163, 184, 0.2) !important;
            color: #1e293b !important;
        }
        
        .product-card:hover {
            background: rgba(248, 250, 252, 0.95) !important;
            border: 1px solid rgba(59, 130, 246, 0.4) !important;
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