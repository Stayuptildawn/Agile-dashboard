import streamlit as st


def load_css():
    st.markdown(
        """
    <style>
    /* Filter labels */
    .filter-label {
        font-size: 12px;
        color: #666;
        margin-bottom: 4px;
        font-weight: 500;
    }
    
    /* Metric cards */
    .metric-card {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: left;
    }
    
    .metric-icon {
        font-size: 24px;
        margin-bottom: 8px;
    }
    
    .metric-label {
        font-size: 12px;
        color: #666;
        margin-bottom: 8px;
    }
    
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #333;
        margin-bottom: 4px;
    }
    
    .metric-change {
        font-size: 11px;
        color: #10b981;
    }
    
    /* Table styling */
    .table-container {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .table-header {
        font-size: 12px;
        color: #666;
        font-weight: 600;
        padding: 10px 5px;
        border-bottom: 2px solid #e5e7eb;
        margin-bottom: 10px;
    }
    
    /* Sortable table header buttons */
    .table-container button[kind="secondary"] {
        background: transparent !important;
        border: none !important;
        color: #666 !important;
        font-weight: 600 !important;
        font-size: 12px !important;
        padding: 10px 5px !important;
        border-bottom: 2px solid #e5e7eb !important;
        border-radius: 0 !important;
        margin-bottom: 10px;
        text-align: left !important;
        width: 100% !important;
        cursor: pointer !important;
        transition: color 0.2s !important;
    }
    
    .table-container button[kind="secondary"]:hover {
        color: #1677ff !important;
        background: transparent !important;
    }
    
    .table-cell {
        padding: 12px 5px;
        font-size: 14px;
        color: #333;
        border-bottom: 1px solid #f3f4f6;
    }
    
    /* Category badges */
    .category-badge {
        display: inline-block;
        padding: 6px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: 600;
        color: white;
    }
    
    .category-health {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    .category-energy {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    }
    
    .category-transport {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
    }
    
    .category-ai {
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
    }
    
    .category-social {
        background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
    }
    
    .category-technology {
        background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
    }
    
    /* Style Streamlit buttons to look like custom View Chart buttons */
    button[kind="secondary"] {
        background: #6366f1 !important;
        color: white !important;
        border: none !important;
        padding: 6px 12px !important;
        border-radius: 6px !important;
        font-size: 11px !important;
        font-weight: 600 !important;
        width: 100% !important;
        height: 20px !important;
        margin-bottom: -12px !important;
        transition: background 0.2s !important;
        min-height: 28px !important;
        max-height: 28px !important;
    }
    
    button[kind="secondary"]:hover {
        background: #4f46e5 !important;
    }
    
    button[kind="secondary"] p {
        color: white !important;
        margin: 0 !important;
        font-size: 11px !important;
        line-height: 1 !important;
    }
    
    button[kind="secondary"] div {
        padding: 0 !important;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )
