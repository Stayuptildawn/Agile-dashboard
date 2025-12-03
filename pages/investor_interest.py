import streamlit as st
import pandas as pd
from pages import header
from styles import investor_interest as investor_styles
from st_aggrid import AgGrid, GridOptionsBuilder, JsCode
import os

header.show_header("Reports/Analytics")
investor_styles.load_css()

# Load ideas data
csv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "ideas.csv")
df = pd.read_csv(csv_path)

# Convert date columns to datetime
df['Date published'] = pd.to_datetime(df['Date published'], errors='coerce')
df['From date'] = pd.to_datetime(df['From date'], errors='coerce')

# Dashboard Title
st.markdown("# 📊 Investor Interest Overview")

# Filter Section    
st.markdown("### Filter Data")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="filter-label">Category</div>', unsafe_allow_html=True)
    category_filter = st.selectbox("Category", ["All Categories", "AI", "HEALTH", "ENERGY", "TRANSPORT", "TECHNOLOGY", "SOCIAL"], label_visibility="collapsed")

with col2:
    st.markdown('<div class="filter-label">From Date</div>', unsafe_allow_html=True)
    from_date = st.date_input("From Date", value=pd.to_datetime("2025-01-01"), label_visibility="collapsed")

with col3:
    st.markdown('<div class="filter-label">To Date</div>', unsafe_allow_html=True)
    to_date = st.date_input("To Date", value=pd.to_datetime("2025-11-27"), label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# Filter ideas by date range (using Date published)
df_filtered = df.copy()
df_filtered = df_filtered[
    (df_filtered['Date published'].notna()) &
    (df_filtered['Date published'] >= pd.to_datetime(from_date)) &
    (df_filtered['Date published'] <= pd.to_datetime(to_date))
]

# Calculate category metrics from actual data
# Simulate investor views and interests based on idea counts (in real app, these would come from actual investor interaction data)
import numpy as np
np.random.seed(42)  # For consistent simulated data

category_stats = []
for category in ['HEALTH', 'ENERGY', 'TRANSPORT', 'AI', 'SOCIAL', 'TECHNOLOGY']:
    cat_ideas = df_filtered[df_filtered['Category'] == category]
    published_count = len(cat_ideas)
    
    # Simulate investor metrics based on published ideas
    # More ideas = more views/interests (with some randomness)
    if published_count > 0:
        base_views_per_idea = 50 + np.random.randint(10, 40)
        total_views = published_count * base_views_per_idea
        interest_rate = 0.12 + np.random.random() * 0.08  # 12-20%
        total_interests = int(total_views * interest_rate)
    else:
        total_views = 0
        total_interests = 0
        interest_rate = 0
    
    category_stats.append({
        'Category': category,
        'Published Ideas': published_count,
        'Total Investor Views': total_views,
        'Total Interests Expressed': total_interests,
        'Interest Rate': f'{interest_rate * 100:.1f}%' if published_count > 0 else '0.0%'
    })

all_category_data = pd.DataFrame(category_stats)

# Apply category filter
if category_filter != "All Categories":
    filtered_data = all_category_data[all_category_data['Category'] == category_filter.upper()].copy()
else:
    filtered_data = all_category_data.copy()
    
# Remove categories with 0 published ideas from display
filtered_data = filtered_data[filtered_data['Published Ideas'] > 0]

# Calculate metrics based on filtered data
total_views = filtered_data['Total Investor Views'].sum()
total_interests = filtered_data['Total Interests Expressed'].sum()
avg_interest_rate = (total_interests / total_views * 100) if total_views > 0 else 0
hot_category = filtered_data.loc[filtered_data['Total Investor Views'].idxmax(), 'Category'] if len(filtered_data) > 0 else 'N/A'
hot_category_views = filtered_data['Total Investor Views'].max() if len(filtered_data) > 0 else 0

# Top Metrics Row
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">👁️</div>
        <div class="metric-label">Total Investor Views</div>
        <div class="metric-value">{total_views:,}</div>
        <div class="metric-change">+12% in last month</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">❤️</div>
        <div class="metric-label">Total Interests Expressed</div>
        <div class="metric-value">{total_interests}</div>
        <div class="metric-change">+8% in last month</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">📊</div>
        <div class="metric-label">Avg. Interest Rate</div>
        <div class="metric-value">{avg_interest_rate:.1f}%</div>
        <div class="metric-change">+2% in last month</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-icon">🔥</div>
        <div class="metric-label">Hot Category</div>
        <div class="metric-value">{hot_category}</div>
        <div class="metric-change">{hot_category_views} views this month</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Category Interest Metrics Table
st.markdown("### 📋 Category Interest Metrics")

# Use filtered data for the table
category_data = filtered_data

# Create a container with two columns: table and buttons
table_col, button_col = st.columns([5, 1])

with table_col:
    # Configure AgGrid
    gb = GridOptionsBuilder.from_dataframe(category_data)

    # Suppress menu for all columns by default
    gb.configure_default_column(suppressMenu=True)

    # Configure all columns as sortable
    gb.configure_column("Category", sortable=True, width=120)
    gb.configure_column("Published Ideas", sortable=True, width=140)
    gb.configure_column("Total Investor Views", sortable=True, width=180)
    gb.configure_column("Total Interests Expressed", sortable=True, width=220)
    gb.configure_column("Interest Rate", sortable=True, width=130)

    # Category column styling with gradient badges
    category_style = JsCode("""
    function(params){
        const v = params.value;
        const base = {'border-radius':'6px','padding':'6px 12px','font-weight':'600','color':'white','display':'inline-block','textAlign':'center'};
        if (v === 'HEALTH') return {...base, 'background':'linear-gradient(135deg, #667eea 0%, #764ba2 100%)'};
        if (v === 'ENERGY') return {...base, 'background':'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)'};
        if (v === 'TRANSPORT') return {...base, 'background':'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)'};
        if (v === 'AI') return {...base, 'background':'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)'};
        if (v === 'SOCIAL') return {...base, 'background':'linear-gradient(135deg, #fa709a 0%, #fee140 100%)'};
        if (v === 'TECHNOLOGY') return {...base, 'background':'linear-gradient(135deg, #30cfd0 0%, #330867 100%)'};
        return base;
    }
    """)
    gb.configure_column("Category", cellStyle=category_style)

    # Disable selection
    gb.configure_selection(selection_mode='disabled')

    # Build grid options
    grid_opts = gb.build()
    grid_opts["domLayout"] = "normal"

    # Render AgGrid and capture the response to get sorted data
    grid_response = AgGrid(
        category_data,
        gridOptions=grid_opts,
        allow_unsafe_jscode=True,
        fit_columns_on_grid_load=True,
        height=300,
        theme="balham"
    )
    
    # Get the displayed (possibly sorted) data
    displayed_data = grid_response['data']

with button_col:
    # Add spacing to align with table header and first row  
    st.markdown('<div style="height: 56px;"></div>', unsafe_allow_html=True)
    
    # Use regular Streamlit buttons (simpler and safer)
    # Use the displayed_data order to match the sorted table
    for idx, row in displayed_data.iterrows():
        category = row['Category']
        # Create a container for each button to control styling
        if st.button("View Chart", key=f"chart_{category}_{idx}", use_container_width=True):
            st.session_state.selected_category = category
            st.rerun()

st.markdown("<br>", unsafe_allow_html=True)

# Display chart for selected category
selected_cat = st.session_state.get('selected_category', 'TECHNOLOGY')
st.markdown(f"### 📈 {selected_cat} - Investor Interest Trends Over Time")

# Generate category-specific data for the trend chart
months_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']

# Different trend patterns for each category
category_trends = {
    'HEALTH': {
        'Investor Views': [45, 52, 58, 62, 68, 72, 76, 78, 80, 82, 87],
        'Interests Expressed': [8, 9, 10, 11, 12, 13, 13, 14, 14, 15, 15]
    },
    'ENERGY': {
        'Investor Views': [35, 38, 42, 48, 52, 55, 58, 60, 62, 64, 68],
        'Interests Expressed': [5, 6, 7, 8, 9, 9, 10, 10, 11, 11, 12]
    },
    'TRANSPORT': {
        'Investor Views': [28, 32, 36, 40, 44, 48, 50, 52, 54, 56, 58],
        'Interests Expressed': [4, 5, 6, 6, 7, 8, 8, 9, 9, 10, 10]
    },
    'AI': {
        'Investor Views': [22, 26, 30, 34, 36, 38, 40, 42, 44, 45, 48],
        'Interests Expressed': [3, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9]
    },
    'SOCIAL': {
        'Investor Views': [10, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22],
        'Interests Expressed': [1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4]
    },
    'TECHNOLOGY': {
        'Investor Views': [8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18],
        'Interests Expressed': [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    }
}

# Get data for selected category
category_data_trends = category_trends.get(selected_cat, category_trends['TECHNOLOGY'])
trend_data = pd.DataFrame({
    'Month': months_order,
    'Investor Views': category_data_trends['Investor Views'],
    'Interests Expressed': category_data_trends['Interests Expressed']
})

# Set Month as categorical to preserve order
trend_data['Month'] = pd.Categorical(trend_data['Month'], categories=months_order, ordered=True)
trend_data = trend_data.sort_values('Month')

# Display the line chart
st.line_chart(trend_data.set_index('Month'), height=300)


