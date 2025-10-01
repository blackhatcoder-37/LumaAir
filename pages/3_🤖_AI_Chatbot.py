# pages/3_🤖_AI_Chatbot.py
import streamlit as st
import requests
import json
import google.generativeai as genai

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

from theme_loader import apply_global_theme
from language_system import t
apply_global_theme()

st.title(t("chatbot_title"))
st.markdown(f"#### {t('chatbot_subtitle')}")

# Configure Google Gemini API
GOOGLE_API_KEY = "AIzaSyCnUeRptqOkVdBKY6DdYklxOzzp3Bw79x0"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini model
@st.cache_resource
def load_model():
    return genai.GenerativeModel('gemini-2.5-flash')

model = load_model()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your LumaAir AI Assistant. I can help you with:\n\n• Air quality information and forecasts\n• Health recommendations based on pollution levels\n• Tips to improve air quality\n• Understanding pollutant types (O₃, NO₂, PM2.5, etc.)\n• Environmental protection advice\n\nWhat would you like to know?"}
    ]

# Demo responses for common questions
demo_responses = {
    "what is o3": "Ozone (O₃) is a secondary pollutant formed when nitrogen oxides and volatile organic compounds react in sunlight. High O₃ levels can cause respiratory issues and are typically highest during sunny afternoons.",
    
    "what is no2": "Nitrogen Dioxide (NO₂) is primarily produced by vehicle emissions and industrial activities. It can irritate airways and increase susceptibility to respiratory infections. Levels are typically highest during rush hours.",
    
    "air quality tips": "Here are key air quality tips:\n• Check daily AQI forecasts\n• Limit outdoor exercise when AQI > 100\n• Use N95 masks on high pollution days\n• Keep indoor plants like Snake Plants\n• Avoid burning waste\n• Use public transport\n• Ventilate your home regularly",
    
    "health effects": "Air pollution can cause:\n• Short-term: Eye irritation, coughing, throat irritation\n• Long-term: Asthma, lung disease, heart problems\n• Vulnerable groups: Children, elderly, pregnant women, people with respiratory conditions need extra protection",
    
    "improve indoor air": "To improve indoor air quality:\n• Use air purifiers with HEPA filters\n• Ventilate regularly (early morning/late evening)\n• Keep houseplants (Spider plants, Peace lilies)\n• Avoid indoor smoking\n• Use exhaust fans while cooking\n• Clean regularly to reduce dust"
}

def get_ai_response(user_message):
    """Generate AI responses using Google Gemini with air quality context"""
    try:
        # Create a comprehensive prompt for air quality context
        system_prompt = """You are LumaAir AI Assistant, an expert in air quality, pollution, and environmental health. 
        You specialize in helping people understand air pollution, its health effects, and practical solutions.
        
        Key areas of expertise:
        - Air pollutants: O₃ (Ozone), NO₂ (Nitrogen Dioxide), PM2.5, PM10, CO, SO₂
        - Health effects and vulnerable populations
        - Air quality index (AQI) interpretation
        - Indoor and outdoor air quality improvement
        - Delhi's specific air quality challenges
        - Protective measures and recommendations
        
        Provide helpful, accurate, and actionable advice. Keep responses concise but informative.
        Focus specifically on air quality topics. If asked about unrelated topics, politely redirect to air quality matters."""
        
        full_prompt = f"{system_prompt}\n\nUser Question: {user_message}\n\nResponse:"
        
        # Generate response using Gemini
        response = model.generate_content(full_prompt)
        if response.text:
            return response.text
        else:
            return "I'm sorry, I couldn't generate a response. Please try rephrasing your question about air quality."
        
    except Exception as e:
        # Fallback to demo responses if API fails
        user_lower = user_message.lower()
        
        if any(keyword in user_lower for keyword in ["o3", "ozone"]):
            return demo_responses["what is o3"]
        elif any(keyword in user_lower for keyword in ["no2", "nitrogen"]):
            return demo_responses["what is no2"]
        elif any(keyword in user_lower for keyword in ["tips", "advice", "improve"]):
            return demo_responses["air quality tips"]
        elif any(keyword in user_lower for keyword in ["health", "effects", "symptoms"]):
            return demo_responses["health effects"]
        elif any(keyword in user_lower for keyword in ["indoor", "home", "house"]):
            return demo_responses["improve indoor air"]
        else:
            return f"I apologize, but I'm having trouble connecting to my AI service right now. Please try asking about specific air quality topics like pollutants, health effects, or improvement tips."

# Chat interface
st.markdown("""
<div class="glass-card">
    <h4>💬 Chat with AI Assistant</h4>
</div>
""", unsafe_allow_html=True)

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        if message["role"] == "assistant":
            st.markdown(f"""
            <div class="glass-card" style="margin: 0.5rem 0; padding: 1rem;">
                {message["content"]}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(message["content"])

# Chat input
if prompt := st.chat_input(t("chat_placeholder")):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_ai_response(prompt)
            st.markdown(f"""
            <div class="glass-card" style="margin: 0.5rem 0; padding: 1rem;">
                {response}
            </div>
            """, unsafe_allow_html=True)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})

# Suggested questions
st.markdown("""
<div class="glass-card">
    <h5>💡 Try asking about:</h5>
    <div style="display: flex; flex-wrap: wrap; gap: 0.5rem; margin-top: 1rem;">
        <button onclick="document.querySelector('[data-testid=stChatInputTextArea]').value = 'What is O3 and how does it affect health?'; document.querySelector('[data-testid=stChatInputTextArea]').focus();" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem; border-radius: 8px; cursor: pointer;">O₃ Health Effects</button>
        <button onclick="document.querySelector('[data-testid=stChatInputTextArea]').value = 'Give me tips to improve indoor air quality'; document.querySelector('[data-testid=stChatInputTextArea]').focus();" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem; border-radius: 8px; cursor: pointer;">Indoor Air Tips</button>
        <button onclick="document.querySelector('[data-testid=stChatInputTextArea]').value = 'What should I do on high pollution days?'; document.querySelector('[data-testid=stChatInputTextArea]').focus();" style="background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.2); color: white; padding: 0.5rem; border-radius: 8px; cursor: pointer;">High Pollution Days</button>
    </div>
</div>
""", unsafe_allow_html=True)

# Clear chat button
if st.button(t("clear_chat"), use_container_width=True):
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your LumaAir AI Assistant. How can I help you with air quality today?"}
    ]
    st.rerun()