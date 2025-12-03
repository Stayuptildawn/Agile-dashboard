import streamlit as st


def load_css():
    st.markdown(
        """
    <style>
      :root { 
        --blue: #1677ff; 
      }

      /* ===== Top header (white card) ===== */
      .app-header {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 14px 16px;
        display: flex; 
        align-items: center; 
        justify-content: space-between;
        box-shadow: 0 4px 10px rgba(0,0,0,.05);
      }

      .title h1 { 
        margin: 0; 
        font-size: 22px; 
        font-weight: 800; 
        color: var(--blue); 
      }
      
      .title p { 
        margin: 0; 
        font-size: 13px; 
        color: #475569; 
      }

      .user-icon {
        font-size: 26px;
        margin-bottom: 4px;
      }
      
      .user-name {
        font-weight: 600; 
        color: #111; 
        font-size: 14px;
        text-align: right;
      }

      /* ===== Navigation bar (blue strip) ===== */
      .navbar {
        background: var(--blue);
        border-radius: 12px;
        padding: 10px 14px;
        box-shadow: 0 3px 10px rgba(0,0,0,.06);
        margin: 12px 0 18px 0;

        display: flex;
        flex-direction: row;
        align-items: center;
        flex-wrap: nowrap;          /* stay on ONE row */
        gap: 8px;
        overflow-x: auto;           /* if too many items, scroll horizontally */
        white-space: nowrap;        /* prevent internal line breaks */
      }

      .navbar a.navlink,
      .navbar span.sep {
        color: #ffffff;
        text-decoration: none;
        font-weight: 700;
        font-size: 13px;
      }

      .navbar a.navlink {
        padding: 6px 10px;
        border-radius: 999px;
        display: inline-block;
        min-height: 32px;
        line-height: 1.4;
      }

      .navbar a.navlink:hover {
        background: rgba(255,255,255,0.16);
      }

      .navbar a.navlink.active {
        background: #ffffff;
        color: var(--blue);
      }

      .navbar .sep {
        opacity: 0.9;
      }

      /* Override Streamlit's page_link styling in navbar */
      .navbar a[data-testid="stPageLink-NavLink"] {
        font-size: 13px !important;
        padding: 6px 10px !important;
        min-height: 32px !important;
        white-space: normal !important;
        line-height: 1.4 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
      }

      .navbar a[data-testid="stPageLink-NavLink"] p {
        margin: 0 !important;
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
      }

      /* Make navbar columns flexible to accommodate text */
      .navbar [data-testid="column"] {
        min-width: 100px !important;
        flex: 1 1 auto !important;
      }

      /* Target all buttons in navbar */
      .navbar button,
      .navbar a {
        font-size: 12px !important;
        white-space: normal !important;
        word-wrap: break-word !important;
        overflow-wrap: break-word !important;
        height: auto !important;
        min-height: 36px !important;
        padding: 8px 12px !important;
      }
    </style>
    """,
        unsafe_allow_html=True,
    )
