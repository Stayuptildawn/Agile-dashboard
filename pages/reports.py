import streamlit as st
import pandas as pd
from pages import header
from styles import reports as reports_styles
import os

header.show_header("Reports/Analytics")
reports_styles.load_css()

# Load ideas data to count published ideas
csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "ideas.csv")
df = pd.read_csv(csv_path)
published_ideas_count = len(df)

# Dashboard Title
st.markdown("# 📊 Platform Metrics Dashboard")

# Top Metrics Row
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">📦 PUBLISHED IDEAS</div>
        <div class="metric-value">{published_ideas_count}</div>
        <div class="metric-subtitle">Total ideas in the system</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">👁️ INVESTOR VIEWS</div>
        <div class="metric-value">2,847</div>
        <div class="metric-subtitle">Total times ideas were viewed</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-title">❤️ INTERESTS EXPRESSED</div>
        <div class="metric-value">436</div>
        <div class="metric-subtitle">Total investor expressions</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Platform Activity Trends Chart
st.markdown("### 📈 Platform Activity Trends")

# Create tabs for different time periods
tab1, tab2, tab3 = st.tabs(["Weekly", "Monthly", "Yearly"])

with tab1:  # Weekly view
    # Generate sample data for weekly chart
    days_order = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    chart_data_weekly = pd.DataFrame({
        'Day': days_order,
        'Idea Submissions': [20, 26, 24, 30, 38, 35, 42],
        'Investor Views': [8, 11, 10, 15, 18, 17, 21],
        'Interests Expressed': [3, 5, 4, 7, 9, 8, 11]
    })
    
    # Set Day as categorical to preserve order
    chart_data_weekly['Day'] = pd.Categorical(chart_data_weekly['Day'], categories=days_order, ordered=True)
    chart_data_weekly = chart_data_weekly.sort_values('Day')
    
    # Display the line chart
    st.line_chart(chart_data_weekly.set_index('Day'), height=400)

with tab2:  # Monthly view
    # Generate sample data for the chart
    chart_data = pd.DataFrame({
        'Week': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'Week 6'],
        'Idea Submissions': [55, 72, 68, 95, 108, 125],
        'Investor Views': [15, 22, 19, 30, 38, 48],
        'Interests Expressed': [8, 13, 11, 18, 22, 28]
    })
    
    # Display the line chart
    st.line_chart(chart_data.set_index('Week'), height=400)


with tab3:  # Yearly view
    # Generate sample data for yearly chart
    months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    chart_data_yearly = pd.DataFrame({
        'Month': months_order,
        'Idea Submissions': [180, 230, 215, 290, 310, 285, 340, 380, 365, 420, 460, 485],
        'Investor Views': [35, 52, 48, 70, 80, 72, 95, 110, 105, 130, 145, 155],
        'Interests Expressed': [18, 28, 25, 38, 44, 40, 52, 62, 58, 75, 85, 92]
    })
    
    # Set Month as categorical to preserve order
    chart_data_yearly['Month'] = pd.Categorical(chart_data_yearly['Month'], categories=months_order, ordered=True)
    chart_data_yearly = chart_data_yearly.sort_values('Month')
    
    # Display the line chart
    st.line_chart(chart_data_yearly.set_index('Month'), height=400)

st.markdown("<br>", unsafe_allow_html=True)

# Detailed Statistics
st.markdown("### 📊 Detailed Statistics")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-title">Avg. Views per Idea</div>
        <div class="stat-value">52.7</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-title">Conversion Rate</div>
        <div class="stat-value">15.3%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-title">Active This Month</div>
        <div class="stat-value">12</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stat-box">
        <div class="stat-title">Avg. Interest/Idea</div>
        <div class="stat-value">8.1</div>
    </div>
    """, unsafe_allow_html=True)
