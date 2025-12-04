import streamlit as st

# IMPORTANT
st.set_page_config(
    page_title="UPM Innovation Platform - Idea Details",
    page_icon="💡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import pandas as pd
from pages import header
from styles import edit_idea as edit_idea  # reuse same CSS


# Show the header navigation
header.show_header("Ideas")

# Load styling
edit_idea.load_css()
st.subheader("1. Idea Details")


def _get_selected_idea():
    """Read-only version: get idea from open_id and map to fields."""
    if "home_docs" not in st.session_state:
        st.error("Hmm, couldn't load ideas. Try refreshing the page.")
        return None

    df = st.session_state.home_docs
    open_id = st.session_state.get("open_id")

    if open_id is None:
        st.warning("No idea selected to open.")
        return None

    try:
        row = df.loc[df["id"] == open_id].iloc[0]
    except Exception:
        st.error(f"Could not find idea with ID {open_id}")
        return None

    return {
        "id": int(row["id"]),
        "Idea Title": str(row.get("Name", "")),
        "Category of the idea": str(row.get("Category", "")),
        "Short Description": str(row.get("Description", ""))[:200],
        "Detailed Description": str(row.get("Detailed Description", "")),
        "Estimated Impact / Target Audience": str(row.get("Estimated Impact / Target Audience", "")),
        "Document name": str(row.get("Document name", "")),
        "Visibility Setting": str(row.get("Visibility Setting", "Public")),
        "Status": str(row.get("Status", "")),
        "Owner": str(row.get("Owner", "")),
        "Date published": str(row.get("Date published", "")),
    }


idea = _get_selected_idea()

if idea is None:
    st.error("No idea found to open. Redirecting to Ideas...")
    import time
    time.sleep(2)
    st.switch_page("pages/dashboard.py")
    st.stop()

# Display title and metadata badges
st.markdown(f"""
<div style="background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); margin-bottom: 20px;">
    <h2 style="margin: 0 0 20px 0; color: #111827;">{idea['Idea Title']}</h2>
    <div style="display: flex; gap: 10px; flex-wrap: wrap; margin-bottom: 20px;">
        <span style="background: #10b981; color: white; padding: 6px 14px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
            📂 {idea["Category of the idea"]}
        </span>
        <span style="background: #6366f1; color: white; padding: 6px 14px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
            📅 {idea.get("Date published", "N/A")[:10]}
        </span>
        <span style="background: #10b981; color: white; padding: 6px 14px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
            ✓ {idea.get("Status", "N/A")}
        </span>
        <span style="background: #8b5cf6; color: white; padding: 6px 14px; border-radius: 6px; font-size: 13px; display: inline-flex; align-items: center; gap: 6px;">
            👁️ {idea.get("Visibility Setting", "Public")}
        </span>
    </div>
    <p style="margin: 0; color: #4b5563; line-height: 1.6;">{idea["Short Description"]}</p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Check if user is admin for engagement metrics
is_admin = st.session_state.get("role") == "admin"

if is_admin:
    # Engagement Metrics (only for admin)
    st.markdown("### 📊 Engagement Metrics")
    
    metric_col1, metric_col2 = st.columns(2)
    
    with metric_col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 30px; border-radius: 10px; text-align: center;">
            <div style="font-size: 48px; font-weight: bold; color: white;">127</div>
            <div style="font-size: 14px; color: rgba(255,255,255,0.9);">Investor Views</div>
        </div>
        """, unsafe_allow_html=True)
    
    with metric_col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); padding: 30px; border-radius: 10px; text-align: center;">
            <div style="font-size: 48px; font-weight: bold; color: white;">23</div>
            <div style="font-size: 14px; color: rgba(255,255,255,0.9);">Interests Expressed</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)

# Two-column layout for main content
left_col, right_col = st.columns([2, 1])

with left_col:
    # Detailed Description
    st.markdown("### 📝 Detailed Description")
    st.markdown(f"""
    <div style="background: #f9fafb; padding: 20px; border-radius: 8px; border-left: 4px solid #6366f1;">
        {idea["Detailed Description"]}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Uploaded Files
    st.markdown("### 📎 Uploaded Files")
    displayed_doc = idea.get("Document name") or "No document attached"
    st.markdown(f"""
    <div style="background: white; border: 2px dashed #d1d5db; padding: 40px; border-radius: 8px; text-align: center;">
        <div style="font-size: 48px; margin-bottom: 10px;">📄</div>
        <div style="font-size: 14px; color: #6b7280; font-weight: 600;">{displayed_doc}</div>
        <button style="margin-top: 15px; background: #6366f1; color: white; border: none; padding: 8px 16px; border-radius: 6px; cursor: pointer;">📥 Download File</button>
    </div>
    """, unsafe_allow_html=True)

with right_col:
    # Project Information
    st.markdown("### 🔷 Project Information")
    st.markdown(f"""
    <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb; margin-bottom: 10px;">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">Category</div>
        <div style="font-size: 14px; font-weight: 600; color: #111827;">{idea["Category of the idea"]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb; margin-bottom: 10px;">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">Target Audience</div>
        <div style="font-size: 14px; font-weight: 600; color: #111827;">{idea["Estimated Impact / Target Audience"]}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="background: white; padding: 15px; border-radius: 8px; border: 1px solid #e5e7eb; margin-bottom: 10px;">
        <div style="font-size: 12px; color: #6b7280; margin-bottom: 4px;">Status</div>
        <div style="font-size: 14px; font-weight: 600; color: #10b981;">✓ {idea.get("Status", "N/A")}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Student/Team Information
    st.markdown("### 👥 Student/Team Information")
    
    # Owner info
    owner = idea.get("Owner", "Unknown")
    st.markdown(f"""
    <div style="background: white; padding: 12px; border-radius: 8px; border: 1px solid #e5e7eb; margin-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 10px;">
            <div style="width: 32px; height: 32px; border-radius: 50%; background: #6366f1; color: white; display: flex; align-items: center; justify-content: center; font-weight: bold;">
                {owner[0].upper() if owner else "?"}
            </div>
            <div>
                <div style="font-size: 13px; font-weight: 600; color: #111827;">{owner}</div>
                <div style="font-size: 11px; color: #6b7280;">Project Lead/Owner</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Back button
if st.button("← Back to Ideas", use_container_width=False):
    st.session_state.pop("open_id", None)
    st.switch_page("pages/dashboard.py")
