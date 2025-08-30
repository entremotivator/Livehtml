import streamlit as st
import pandas as pd

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Enhanced Google Sheet Code Viewer",
    layout="wide"
)

# --- TITLE ---
st.title("📄 Live Google Sheets HTML/CSS Viewer")
st.markdown(
    """
    This app reads a public Google Sheet and displays HTML/CSS code live.
    Select a number from the sidebar or search, and view the live preview and code.
    """
)

# --- GOOGLE SHEET CSV LINK ---
sheet_url = "https://docs.google.com/spreadsheets/d/1hBPTl0qzmpLGb9nJHJaK0ZogBs-dbhqoDOp1VVj8RgY/export?format=csv"

# --- LOAD DATA ---
@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    # Ensure columns exist
    if 'Number' not in df.columns or 'Code' not in df.columns:
        st.error("Google Sheet must have 'Number' and 'Code' columns.")
        return pd.DataFrame(columns=['Number', 'Code'])
    return df

df = load_data(sheet_url)

if df.empty:
    st.stop()

# --- SIDEBAR ---
st.sidebar.title("🔍 Select or Search Number")
search_number = st.sidebar.text_input("Search Number")
numbers = df['Number'].astype(str).tolist()

# Filter numbers by search term
if search_number:
    filtered_numbers = [n for n in numbers if search_number in n]
else:
    filtered_numbers = numbers

selected_number = st.sidebar.selectbox("Choose Number", filtered_numbers)

# --- FILTER DATA ---
selected_row = df[df['Number'].astype(str) == selected_number]

if not selected_row.empty:
    code_data = selected_row['Code'].values[0]
else:
    code_data = "<p>No code available</p>"

# --- MAIN LAYOUT ---
col1, col2 = st.columns([1, 1])

# Live Preview
with col1:
    st.subheader(f"🌐 Live Preview for Number: {selected_number}")
    st.components.v1.html(code_data, height=600, scrolling=True)

# Raw Code Viewer
with col2:
    st.subheader("💻 HTML/CSS Code")
    st.code(code_data, language='html')

# --- FULL TABLE VIEW ---
st.subheader("📋 All Numbers & Codes")
st.dataframe(df, use_container_width=True)

st.markdown(
    """
    **Instructions:**  
    - Use the sidebar to select a Number.  
    - Live preview updates automatically.  
    - Copy code from the code panel for your projects.
    """
)
