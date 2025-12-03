import streamlit as st


def load_css():
    st.markdown(
        """
    <style>
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin: 10px 0;
    }
    .metric-title {
        font-size: 14px;
        color: #666;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .metric-value {
        font-size: 36px;
        font-weight: bold;
        color: #333;
        margin-bottom: 5px;
    }
    .metric-subtitle {
        font-size: 12px;
        color: #999;
    }
    .stat-box {
        background-color: #f8f9fa;
        padding: 15px;
        border-radius: 8px;
        border-left: 3px solid #4A90E2;
    }
    .stat-title {
        font-size: 12px;
        color: #666;
        margin-bottom: 5px;
    }
    .stat-value {
        font-size: 28px;
        font-weight: bold;
        color: #333;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
