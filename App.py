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
    Select a number from the sidebar, toggle edit mode, and view the live preview.
    """
)

# --- GOOGLE SHEET CSV LINK ---
sheet_url = "https://docs.google.com/spreadsheets/d/1hBPTl0qzmpLGb9nJHJaK0ZogBs-dbhqoDOp1VVj8RgY/export?format=csv"

# --- LOAD DATA ---
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        # Ensure columns exist
        if 'Number' not in df.columns or 'Code' not in df.columns:
            st.error("Google Sheet must have 'Number' and 'Code' columns.")
            return pd.DataFrame(columns=['Number', 'Code'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame(columns=['Number', 'Code'])

df = load_data(sheet_url)

if df.empty:
    st.warning("No data available. Please check your Google Sheet.")
    st.stop()

# --- SIDEBAR ---
st.sidebar.title("🔍 Select or Search Number")

# Search functionality
search_number = st.sidebar.text_input("🔍 Search Number", placeholder="Type to filter...")
numbers = df['Number'].astype(str).tolist()

# Filter numbers by search term
if search_number:
    filtered_numbers = [n for n in numbers if search_number.lower() in n.lower()]
    if not filtered_numbers:
        st.sidebar.warning("No matching numbers found")
        filtered_numbers = numbers
else:
    filtered_numbers = numbers

selected_number = st.sidebar.selectbox("Choose Number", filtered_numbers, key="number_select")

# --- CONTROL TOGGLES ---
st.sidebar.markdown("---")
st.sidebar.subheader("🎛️ Controls")

edit_mode = st.sidebar.toggle("✏️ Edit Mode", value=False, help="Enable to edit the code")
show_code = st.sidebar.toggle("👁️ Show Code Panel", value=True, help="Toggle code visibility")
live_preview = st.sidebar.toggle("🌐 Live Preview", value=True, help="Enable/disable live preview")

# --- FILTER DATA ---
selected_row = df[df['Number'].astype(str) == selected_number]

if not selected_row.empty:
    original_code = selected_row['Code'].values[0]
else:
    original_code = "<p>No code available for this number</p>"

# --- MAIN LAYOUT ---
if live_preview and show_code:
    col1, col2 = st.columns([1, 1])
elif live_preview or show_code:
    col1, col2 = st.columns([1, 0.001]) if live_preview else st.columns([0.001, 1])
else:
    st.info("Both preview and code panel are disabled. Please enable at least one from the sidebar.")
    st.stop()

# --- EDIT MODE HANDLING ---
if edit_mode and show_code:
    if 'edited_code' not in st.session_state:
        st.session_state.edited_code = original_code
    
    # Reset button
    if st.sidebar.button("🔄 Reset to Original", help="Reset edited code to original"):
        st.session_state.edited_code = original_code
        st.rerun()

# Determine which code to use
if edit_mode and 'edited_code' in st.session_state:
    current_code = st.session_state.edited_code
else:
    current_code = original_code

# --- LIVE PREVIEW ---
if live_preview:
    with col1:
        st.subheader(f"🌐 Live Preview - Number: {selected_number}")
        if edit_mode:
            st.caption("⚡ Live editing mode - changes update in real-time")
        
        try:
            st.components.v1.html(current_code, height=600, scrolling=True)
        except Exception as e:
            st.error(f"Error rendering preview: {str(e)}")

# --- CODE EDITOR/VIEWER ---
if show_code:
    with col2:
        if edit_mode:
            st.subheader("✏️ Code Editor")
            st.caption("Edit the code below - changes apply to preview immediately")
            
            # Code editor
            edited_code = st.text_area(
                "HTML/CSS Code",
                value=current_code,
                height=550,
                key="code_editor",
                label_visibility="collapsed"
            )
            
            # Update session state when code changes
            if edited_code != current_code:
                st.session_state.edited_code = edited_code
                st.rerun()
                
        else:
            st.subheader("💻 HTML/CSS Code (Read-only)")
            st.code(current_code, language='html', line_numbers=True)

# --- STATUS BAR ---
st.markdown("---")
status_col1, status_col2, status_col3 = st.columns(3)

with status_col1:
    st.metric("Selected Number", selected_number)

with status_col2:
    mode_status = "✏️ Edit Mode" if edit_mode else "👁️ View Mode"
    st.metric("Current Mode", mode_status)

with status_col3:
    total_entries = len(df)
    st.metric("Total Entries", total_entries)

# --- INSTRUCTIONS ---
with st.expander("📖 Instructions & Tips", expanded=False):
    st.markdown(
        """
        **How to use this app:**
        
        1. **Select a Number**: Use the sidebar dropdown or search to find specific entries
        2. **Toggle Controls**: 
           - **Edit Mode**: Enable to modify code in real-time
           - **Show Code Panel**: Toggle code visibility on/off  
           - **Live Preview**: Enable/disable the preview panel
        3. **Edit Mode Features**:
           - Edit code directly in the text area
           - Changes update the preview immediately
           - Use "Reset to Original" to restore original code
           - Edits are temporary (not saved to the Google Sheet)
        
        **Tips:**
        - Use the search box to quickly find specific numbers
        - Toggle panels off to focus on preview or code only
        - Edit mode is perfect for experimenting with modifications
        """
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.8em;'>"
    "📊 Data loaded from Google Sheets | 🔄 Auto-refreshes on page reload"
    "</div>", 
    unsafe_allow_html=True
)
