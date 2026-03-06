# Agile Dashboard

A multi-page Streamlit application for managing, reviewing, and tracking innovation ideas — built with role-based access, CSV persistence, and a modular page architecture.

---

## Overview

I built this to give teams a lightweight, no-database platform for submitting and tracking innovation ideas through a full lifecycle — from draft to published. It supports both public visitors browsing ideas and authenticated users managing their own submissions. The goal was to keep deployment friction near zero while still providing a real, usable product.

---

## Tech Stack

- **Python 3.8+**
- **Streamlit 1.29+** — web framework and UI
- **Pandas** — data handling and CSV operations
- **streamlit-aggrid** — interactive, sortable data tables
- **HTML / CSS** — custom styling via a centralized `styles/` module

---

## Project Structure

```
Agile-dashboard/
│
├── streamlit_app.py          # Entry point — loads CSV data, manages session state, routes pages
├── generate_initial_data.py  # One-time script to seed ideas.csv with sample data
├── requirements.txt          # Python dependencies
│
├── pages/
│   ├── home.py               # Public landing page with stats, category breakdown, recent activity
│   ├── login.py              # Authentication with rate limiting and lockout handling
│   ├── dashboard.py          # Full ideas table for authenticated users (filter, sort, delete)
│   ├── myIdeas.py            # Personal workspace — view, edit, publish, or delete your ideas
│   ├── publish_idea.py       # New idea submission form (draft or publish)
│   ├── edit_idea.py          # Edit an existing idea, auto-saves to CSV
│   ├── openIdea.py           # Detailed single-idea view
│   ├── investor_interest.py  # Investor-facing idea exploration page
│   ├── messages.py           # In-app messaging interface
│   ├── reports.py            # Reporting and analytics view
│   ├── profile.py            # User profile page (in progress)
│   ├── sprints.py            # Sprint tracking (in progress)
│   ├── team.py               # Team management (in progress)
│   ├── experiments.py        # Experimental features sandbox
│   └── header.py             # Shared navigation component used across all pages
│
├── styles/                   # Per-page CSS modules loaded at runtime
│   ├── main.py               # Global base styles
│   ├── login.py              # Login page styles
│   ├── dashboard.py          # Dashboard table styles
│   ├── header.py             # Navigation bar styles
│   ├── edit_idea.py          # Form styles
│   └── home.py               # Home page styles
│
├── data/                     # Flat-file storage (no database required)
│   ├── ideas.csv             # All submitted ideas
│   ├── users.csv             # User credentials
│   └── login_attempts.csv    # Failed login tracking for rate limiting
│
└── elements/                 # Static assets (logos, UI images)
```

---

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Stayuptildawn/Agile-dashboard.git
   cd Agile-dashboard
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install streamlit pandas streamlit-aggrid
   ```

4. **(Optional) Seed the database with sample ideas:**
   ```bash
   python generate_initial_data.py
   ```

5. **Start the app:**
   ```bash
   streamlit run streamlit_app.py
   ```

   The app will open at `http://localhost:8501`.

6. **Default login credentials:**
   - Username: `admin`
   - Password: `aA1234`

   > ⚠️ For any real deployment, replace these with hashed credentials. Plaintext passwords in CSV are for demo use only.

---

## Key Output / Results

Once running, you get a fully functional multi-page web app where public users can browse and filter published ideas, and authenticated users can submit, manage, and track their own ideas through a draft → review → published workflow — all persisted automatically to local CSV files.

---

## Author

**Mohammad Soleimani Roudi**
[GitHub](https://github.com/Stayuptildawn)
