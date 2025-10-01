import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime, date, timedelta
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pretrained_prediction_engine import PretrainedPredictionEngine
from theme_loader import apply_global_theme

def main():
    """Main function for pretrained data predictions page"""
    
    # Apply theme
    apply_global_theme()
    
    # Page configuration
    st.title("📊 Pretrained Data Predictions")
    st.markdown("### Historical predictions using trained ML models (2019-2024)")
    
    # Information note about predictions
    st.info("ℹ️ **Note**: This page demonstrates prediction capabilities using realistic synthetic data patterns based on your trained models. The predictions show typical pollution behavior with daily, seasonal, and site-specific variations.")
    
    # Initialize prediction engine
    if 'prediction_engine' not in st.session_state:
        with st.spinner("Loading pretrained models..."):
            st.session_state.prediction_engine = PretrainedPredictionEngine()
    
    engine = st.session_state.prediction_engine
    
    # Sidebar controls
    st.sidebar.header("📊 Pretrained Data Predictions")
    
    # Site selection
    available_sites = engine.get_available_sites()
    if not available_sites:
        st.error("No pretrained models found. Please check model files.")
        return
    
    site_options = {site_id: engine.get_site_name(site_id) for site_id in available_sites}
    selected_site = st.sidebar.selectbox(
        "Select Monitoring Site",
        options=list(site_options.keys()),
        format_func=lambda x: site_options[x],
        key="pretrained_site_selector"
    )
    
    # Pollutant selection
    pollutant_options = {
        "O3": "O₃ (Ozone)",
        "NO2": "NO₂ (Nitrogen Dioxide)"
    }
    selected_pollutant = st.sidebar.selectbox(
        "Select Pollutant",
        options=list(pollutant_options.keys()),
        format_func=lambda x: pollutant_options[x],
        key="pretrained_pollutant_selector"
    )
    
    # Time period selection
    time_period_options = {
        "hourly": "Hourly",
        "24hrs": "24 Hours",
        "weekly": "Weekly"
    }
    
    selected_period = st.sidebar.selectbox(
        "Select Time Period",
        options=list(time_period_options.keys()),
        format_func=lambda x: time_period_options[x],
        key="pretrained_period_selector"
    )
    
    # Date range selection
    st.sidebar.subheader("Select Date Range")
    
    # Set date limits for 2019-2024
    min_date = date(2019, 1, 1)
    max_date = date(2024, 12, 31)
    
    start_date = st.sidebar.date_input(
        "Start Date",
        value=date(2023, 1, 1),
        min_value=min_date,
        max_value=max_date,
        key="pretrained_start_date"
    )
    
    end_date = st.sidebar.date_input(
        "End Date",
        value=date(2023, 1, 31),
        min_value=min_date,
        max_value=max_date,
        key="pretrained_end_date"
    )
    
    # Validate date range
    if start_date >= end_date:
        st.sidebar.error("End date must be after start date")
        return
    
    # Check for reasonable date range based on period
    date_diff = (end_date - start_date).days
    if selected_period == "hourly" and date_diff > 31:
        st.sidebar.warning("⚠️ Large date range selected for hourly data. Consider reducing for better performance.")
    elif selected_period == "weekly" and date_diff < 7:
        st.sidebar.warning("⚠️ Short date range for weekly data. Consider increasing the range.")
    
    # Generate predictions button
    if st.sidebar.button("🔮 Generate Predictions", type="primary", key="generate_pretrained_pred"):
        generate_predictions(engine, selected_site, selected_pollutant, 
                           start_date, end_date, selected_period)

def generate_predictions(engine, site_id, pollutant, start_date, end_date, time_period):
    """Generate and display predictions"""
    
    # Convert dates to datetime
    start_datetime = datetime.combine(start_date, datetime.min.time())
    end_datetime = datetime.combine(end_date, datetime.max.time())
    
    with st.spinner("Generating predictions..."):
        # Get predictions
        predictions_df = engine.predict_pollutant(
            site_id, pollutant, start_datetime, end_datetime, time_period
        )
        
        if predictions_df is None or predictions_df.empty:
            st.error("No predictions available. Please check your selections.")
            return
        
        # Store in session state
        st.session_state.predictions_data = predictions_df
        st.session_state.prediction_params = {
            'site_id': site_id,
            'pollutant': pollutant,
            'time_period': time_period,
            'start_date': start_date,
            'end_date': end_date
        }
    
    # Display results
    display_prediction_results(engine, predictions_df)

def display_prediction_results(engine, predictions_df):
    """Display prediction results with charts and statistics"""
    
    params = st.session_state.prediction_params
    
    st.header("📈 Prediction Results")
    
    # Summary info
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="🏢 Site",
            value=engine.get_site_name(params['site_id'])
        )
    
    with col2:
        pollutant_display = "O₃" if params['pollutant'] == "O3" else "NO₂"
        st.metric(
            label="🧪 Pollutant", 
            value=pollutant_display
        )
    
    with col3:
        period_display = {
            'hourly': 'Hourly',
            '24hrs': '24 Hours', 
            'weekly': 'Weekly'
        }
        st.metric(
            label="⏰ Period",
            value=period_display[params['time_period']]
        )
    
    with col4:
        st.metric(
            label="📊 Data Points",
            value=len(predictions_df)
        )
    
    # Create main chart
    display_prediction_chart(predictions_df, params)
    
    # Summary statistics
    display_summary_statistics(engine, predictions_df, params)
    
    # Model information
    display_model_information(engine, params)

def display_prediction_chart(predictions_df, params):
    """Create and display the main prediction chart"""
    
    st.subheader("📈 Prediction Timeline")
    
    pollutant_col = f"{params['pollutant']}_prediction"
    
    # Create the main time series plot
    fig = go.Figure()
    
    # Add main prediction line
    fig.add_trace(go.Scatter(
        x=predictions_df['datetime'],
        y=predictions_df[pollutant_col],
        mode='lines+markers',
        name=f"{params['pollutant']} Predictions",
        line=dict(width=2, color='#3498db'),
        marker=dict(size=4)
    ))
    
    # Add threshold lines for health standards
    if params['pollutant'] == 'O3':
        # WHO guideline for O3 (100 μg/m³ = ~50 ppb)
        fig.add_hline(y=120, line_dash="dash", line_color="red", 
                     annotation_text="Unhealthy Threshold (120 μg/m³)")
        fig.add_hline(y=100, line_dash="dot", line_color="orange",
                     annotation_text="WHO Guideline (100 μg/m³)")
    elif params['pollutant'] == 'NO2':
        # WHO guideline for NO2 (40 μg/m³)
        fig.add_hline(y=40, line_dash="dash", line_color="red",
                     annotation_text="WHO Guideline (40 μg/m³)")
        fig.add_hline(y=25, line_dash="dot", line_color="orange",
                     annotation_text="Good Quality (25 μg/m³)")
    
    # Customize layout
    fig.update_layout(
        title=f"{params['pollutant']} Predictions - {params['site_id']}",
        xaxis_title="Date/Time",
        yaxis_title=f"{params['pollutant']} Concentration (μg/m³)",
        hovermode='x unified',
        height=500,
        showlegend=True,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)'
    )
    
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgray')
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Additional charts in columns
    col1, col2 = st.columns(2)
    
    with col1:
        # Distribution histogram
        fig_hist = px.histogram(
            predictions_df, 
            x=pollutant_col,
            nbins=30,
            title=f"{params['pollutant']} Distribution",
            color_discrete_sequence=['#3498db']
        )
        fig_hist.update_layout(height=300, showlegend=False)
        st.plotly_chart(fig_hist, use_container_width=True)
    
    with col2:
        # Box plot by time component
        if params['time_period'] == 'hourly':
            predictions_df['hour'] = predictions_df['datetime'].dt.hour
            fig_box = px.box(
                predictions_df,
                x='hour', 
                y=pollutant_col,
                title="Hourly Variation",
                color_discrete_sequence=['#2ecc71']
            )
        else:
            predictions_df['day_of_week'] = predictions_df['datetime'].dt.day_name()
            fig_box = px.box(
                predictions_df,
                x='day_of_week',
                y=pollutant_col, 
                title="Daily Variation",
                color_discrete_sequence=['#2ecc71']
            )
        
        fig_box.update_layout(height=300, showlegend=False)
        fig_box.update_xaxes(tickangle=45)
        st.plotly_chart(fig_box, use_container_width=True)

def display_summary_statistics(engine, predictions_df, params):
    """Display summary statistics for predictions"""
    
    st.subheader("📊 Summary Statistics")
    
    # Get summary from engine
    summary = engine.get_prediction_summary(predictions_df)
    
    if not summary:
        st.error("Could not generate summary statistics")
        return
    
    # Display key metrics in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric(
            label="Mean Value",
            value=f"{summary['mean']:.2f} μg/m³"
        )
    
    with col2:
        st.metric(
            label="Standard Deviation",
            value=f"{summary['std']:.2f} μg/m³"
        )
    
    with col3:
        st.metric(
            label="Minimum",
            value=f"{summary['min']:.2f} μg/m³"
        )
    
    with col4:
        st.metric(
            label="Maximum",
            value=f"{summary['max']:.2f} μg/m³"
        )
    
    with col5:
        st.metric(
            label="Median",
            value=f"{summary['median']:.2f} μg/m³"
        )
    
    # Threshold exceedances
    st.subheader("⚠️ Threshold Exceedances")
    
    threshold_col1, threshold_col2 = st.columns(2)
    
    with threshold_col1:
        if params['pollutant'] == 'O3':
            exceeds_120 = summary['above_threshold']['O3_120']
            total_points = summary['count']
            percentage = (exceeds_120 / total_points * 100) if total_points > 0 else 0
            
            st.metric(
                label="Above 120 μg/m³ (Unhealthy)",
                value=f"{exceeds_120}",
                delta=f"{percentage:.1f}% of total"
            )
        
        elif params['pollutant'] == 'NO2':
            exceeds_40 = summary['above_threshold']['NO2_40']
            total_points = summary['count']
            percentage = (exceeds_40 / total_points * 100) if total_points > 0 else 0
            
            st.metric(
                label="Above 40 μg/m³ (WHO Guideline)",
                value=f"{exceeds_40}",
                delta=f"{percentage:.1f}% of total"
            )
    
    with threshold_col2:
        # Show data range
        st.metric(
            label="Date Range",
            value=f"{params['start_date']} to {params['end_date']}"
        )

def display_model_information(engine, params):
    """Display information about the model used"""
    
    st.subheader("🤖 Model Information")
    
    model_info = engine.get_model_info(params['site_id'], params['pollutant'])
    
    if not model_info:
        st.error("Model information not available")
        return
    
    # Display model details in columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(
            label="Model Type",
            value=model_info.get('model_type', 'Unknown')
        )
        
        st.metric(
            label="Number of Features",
            value=str(model_info.get('n_features', 'Unknown'))
        )
    
    with col2:
        fitted_status = "✅ Fitted" if model_info.get('is_fitted', False) else "❌ Not Fitted"
        st.metric(
            label="Model Status",
            value=fitted_status
        )
        
        st.metric(
            label="Best Iteration",
            value=str(model_info.get('best_iteration', 'Unknown'))
        )
    
    with col3:
        st.metric(
            label="Estimators",
            value=str(model_info.get('n_estimators', 'Unknown'))
        )
    
    # Feature importance (if available)
    if 'feature_names' in model_info and len(model_info['feature_names']) > 0:
        with st.expander("📋 Model Features", expanded=False):
            feature_names = model_info['feature_names']
            if hasattr(feature_names, 'tolist'):
                feature_names = feature_names.tolist()
            
            # Display in columns for better readability
            cols = st.columns(3)
            for i, feature in enumerate(feature_names):
                with cols[i % 3]:
                    st.text(f"• {feature}")

# Run the page
if __name__ == "__main__":
    main()
else:
    main()