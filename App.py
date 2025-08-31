import streamlit as st
import pandas as pd
from io import BytesIO
import base64

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Enhanced Code Viewer - Google Sheets Integration",
    layout="wide"
)

# --- LOAD DATA FUNCTION ---
@st.cache_data
def load_data(url):
    try:
        df = pd.read_csv(url)
        # Check for required columns
        required_columns = ['Number', 'Code']
        optional_columns = ['Title', 'Category', 'Description']
        
        # Ensure required columns exist
        for col in required_columns:
            if col not in df.columns:
                st.error(f"Google Sheet must have '{col}' column.")
                return pd.DataFrame(columns=required_columns + optional_columns)
        
        # Add missing optional columns with defaults
        for col in optional_columns:
            if col not in df.columns:
                if col == 'Title':
                    df[col] = df['Number'].astype(str) + " - Custom Code"
                elif col == 'Category':
                    df[col] = "Custom"
                elif col == 'Description':
                    df[col] = "Custom HTML/CSS code from Google Sheets"
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return pd.DataFrame(columns=['Number', 'Code', 'Title', 'Category', 'Description'])

def generate_pdf_from_html(html_content, title="Document"):
    """Generate PDF from HTML with improved formatting for all content types"""
    try:
        from reportlab.lib.pagesizes import A4, letter
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
        from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
        from reportlab.lib.units import inch
        from reportlab.lib import colors
        from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
        from html.parser import HTMLParser
        import re
        
        class EnhancedHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.content = []
                self.current_text = ""
                self.in_title = False
                self.in_header = False
                self.in_paragraph = False
                self.in_list = False
                self.in_table = False
                self.header_level = 1
                self.list_items = []
                self.table_rows = []
                self.current_row = []
                
            def handle_starttag(self, tag, attrs):
                if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    self.in_header = True
                    self.header_level = int(tag[1])
                elif tag == 'p':
                    self.in_paragraph = True
                elif tag in ['ul', 'ol']:
                    self.in_list = True
                    self.list_items = []
                elif tag == 'li':
                    self.current_text = ""
                elif tag == 'title':
                    self.in_title = True
                elif tag == 'table':
                    self.in_table = True
                    self.table_rows = []
                elif tag == 'tr':
                    self.current_row = []
                elif tag == 'br':
                    self.current_text += "\n"
                    
            def handle_endtag(self, tag):
                if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    if self.current_text.strip():
                        self.content.append(('header', self.current_text.strip(), self.header_level))
                    self.current_text = ""
                    self.in_header = False
                elif tag == 'p':
                    if self.current_text.strip():
                        self.content.append(('paragraph', self.current_text.strip()))
                    self.current_text = ""
                    self.in_paragraph = False
                elif tag in ['ul', 'ol']:
                    if self.list_items:
                        self.content.append(('list', self.list_items))
                    self.in_list = False
                elif tag == 'li':
                    if self.current_text.strip():
                        self.list_items.append(self.current_text.strip())
                    self.current_text = ""
                elif tag == 'title':
                    self.in_title = False
                elif tag == 'table':
                    if self.table_rows:
                        self.content.append(('table', self.table_rows))
                    self.in_table = False
                elif tag == 'tr':
                    if self.current_row:
                        self.table_rows.append(self.current_row)
                elif tag in ['td', 'th']:
                    if self.current_text.strip():
                        self.current_row.append(self.current_text.strip())
                    self.current_text = ""
                    
            def handle_data(self, data):
                if not self.in_title:  # Skip title content
                    self.current_text += data
                    
            def get_content(self):
                # Add any remaining text as paragraph
                if self.current_text.strip():
                    self.content.append(('paragraph', self.current_text.strip()))
                return self.content
        
        # Create PDF buffer
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, topMargin=1*inch, bottomMargin=1*inch)
        
        # Enhanced styles
        styles = getSampleStyleSheet()
        
        # Custom styles for better formatting
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontSize=24,
            spaceAfter=30,
            textColor=colors.HexColor('#2c3e50'),
            alignment=TA_CENTER
        )
        
        heading_styles = {
            1: ParagraphStyle('CustomH1', parent=styles['Heading1'], fontSize=20, spaceAfter=20, textColor=colors.HexColor('#34495e')),
            2: ParagraphStyle('CustomH2', parent=styles['Heading2'], fontSize=18, spaceAfter=18, textColor=colors.HexColor('#34495e')),
            3: ParagraphStyle('CustomH3', parent=styles['Heading3'], fontSize=16, spaceAfter=16, textColor=colors.HexColor('#34495e')),
            4: ParagraphStyle('CustomH4', parent=styles['Heading4'], fontSize=14, spaceAfter=14, textColor=colors.HexColor('#34495e')),
            5: ParagraphStyle('CustomH5', parent=styles['Heading5'], fontSize=12, spaceAfter=12, textColor=colors.HexColor('#34495e')),
            6: ParagraphStyle('CustomH6', parent=styles['Heading6'], fontSize=11, spaceAfter=11, textColor=colors.HexColor('#34495e'))
        }
        
        body_style = ParagraphStyle(
            'CustomBody',
            parent=styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            leading=14,
            textColor=colors.HexColor('#2c3e50'),
            alignment=TA_JUSTIFY
        )
        
        list_style = ParagraphStyle(
            'CustomList',
            parent=styles['Normal'],
            fontSize=11,
            leftIndent=20,
            spaceAfter=6,
            leading=14,
            textColor=colors.HexColor('#2c3e50')
        )
        
        # Parse HTML content
        parser = EnhancedHTMLParser()
        parser.feed(html_content)
        content_elements = parser.get_content()
        
        # Build PDF content
        story = []
        
        # Add title
        story.append(Paragraph(title, title_style))
        story.append(Spacer(1, 20))
        
        # Process parsed content
        for element in content_elements:
            if element[0] == 'header':
                level = element[2] if len(element) > 2 else 1
                style = heading_styles.get(level, heading_styles[1])
                story.append(Paragraph(element[1], style))
                
            elif element[0] == 'paragraph':
                # Clean up text and handle special characters
                text = element[1].replace('&nbsp;', ' ').replace('&amp;', '&')
                story.append(Paragraph(text, body_style))
                
            elif element[0] == 'list':
                for item in element[1]:
                    story.append(Paragraph(f"• {item}", list_style))
                story.append(Spacer(1, 10))
                
            elif element[0] == 'table':
                if element[1]:  # If table has rows
                    table_data = element[1]
                    table = Table(table_data)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f8f9fa')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                        ('TEXTCOLOR', (0, 1), (-1, -1), colors.HexColor('#2c3e50')),
                        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                        ('FONTSIZE', (0, 1), (-1, -1), 9),
                        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#dee2e6'))
                    ]))
                    story.append(table)
                    story.append(Spacer(1, 15))
        
        # If no structured content found, fall back to simple text extraction
        if not story or len(story) <= 2:  # Only title and spacer
            # Simple text extraction as fallback
            clean_text = re.sub(r'<[^>]+>', ' ', html_content)
            clean_text = re.sub(r'\s+', ' ', clean_text).strip()
            
            if clean_text:
                # Split into paragraphs
                paragraphs = [p.strip() for p in clean_text.split('\n') if p.strip()]
                if not paragraphs:
                    paragraphs = [clean_text[:1000] + "..." if len(clean_text) > 1000 else clean_text]
                
                for para in paragraphs:
                    if para:
                        story.append(Paragraph(para, body_style))
                        story.append(Spacer(1, 12))
        
        # Build PDF
        doc.build(story)
        buffer.seek(0)
        return buffer.getvalue()
        
    except ImportError:
        st.error("ReportLab package is required for PDF generation. Please install it.")
        return None
    except Exception as e:
        st.error(f"Error generating PDF: {str(e)}")
        return None

def clean_html_for_download(html_content):
    """Clean HTML content for download - embed CSS properly without showing raw code"""
    import re
    
    # Extract CSS from style tags
    css_pattern = r'<style[^>]*>(.*?)</style>'
    css_matches = re.findall(css_pattern, html_content, re.DOTALL)
    
    # Remove script tags completely
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    
    # If CSS found, ensure it's properly embedded in head
    if css_matches:
        combined_css = '\n'.join(css_matches)
        
        # Remove existing style tags
        html_content = re.sub(css_pattern, '', html_content, flags=re.DOTALL)
        
        # Add CSS to head section
        if '<head>' in html_content:
            html_content = html_content.replace('<head>', f'<head>\n<style>\n{combined_css}\n</style>')
        else:
            # Add head section if missing
            html_content = html_content.replace('<html>', '<html>\n<head>\n<style>\n{combined_css}\n</style>\n</head>')
    
    return html_content

# --- TITLE ---
st.title("🚀 Enhanced Code Viewer - Google Sheets Integration")
st.markdown(
    """
    Professional code viewer with Google Sheets integration, live preview, and PDF download capabilities.
    Load your HTML/CSS code from Google Sheets and view with enhanced formatting.
    """
)

# --- SIDEBAR ---
st.sidebar.title("🎯 Code Selection")

sheet_url = st.sidebar.text_input(
    "Google Sheet CSV URL:",
    value="https://docs.google.com/spreadsheets/d/1eFZcnDoGT2NJHaEQSgxW5psN5kvlkYx1vtuXGRFTGTk/export?format=csv",
    help="Enter the CSV export URL of your Google Sheet. Required columns: Number, Code. Optional: Title, Category, Description"
)

if sheet_url:
    df = load_data(sheet_url)
    
    if not df.empty:
        st.sidebar.markdown("### Google Sheets Data")
        
        # Category filter for Google Sheets
        if 'Category' in df.columns:
            sheet_categories = list(set(df['Category'].tolist()))
            selected_sheet_category = st.sidebar.selectbox("Filter by Category:", ["All Categories"] + sheet_categories)
            
            if selected_sheet_category != "All Categories":
                df = df[df['Category'] == selected_sheet_category]
        
        # Number selection
        numbers = df['Number'].tolist()
        selected_number = st.sidebar.selectbox("Choose Number:", numbers)
        
        # Get selected row
        selected_row = df[df['Number'] == selected_number].iloc[0]
        current_code = selected_row['Code']
        
        # Display info
        st.sidebar.markdown("### Selected Item Info")
        st.sidebar.write(f"**Title:** {selected_row.get('Title', 'N/A')}")
        st.sidebar.write(f"**Category:** {selected_row.get('Category', 'N/A')}")
        st.sidebar.write(f"**Description:** {selected_row.get('Description', 'N/A')}")
        
    else:
        st.sidebar.error("No data loaded. Please check your Google Sheet URL.")
        current_code = "<h1>No Data</h1><p>Please provide a valid Google Sheet URL.</p>"
        selected_row = {'Title': 'No Data', 'Category': 'Error', 'Description': 'No data available'}
else:
    st.sidebar.warning("Please enter a Google Sheet URL to load data.")
    current_code = "<h1>Welcome</h1><p>Please enter a Google Sheet URL in the sidebar to load your HTML/CSS code.</p>"
    selected_row = {'Title': 'Welcome', 'Category': 'Info', 'Description': 'Enter Google Sheet URL to begin'}

# --- DISPLAY CONTROLS ---
st.sidebar.markdown("---")
st.sidebar.markdown("### 🎛️ Display Controls")

show_live_preview = st.sidebar.toggle("🔴 Live Preview", value=True, help="Show rendered HTML/CSS preview")
show_code_panel = st.sidebar.toggle("📝 Show Code Panel", value=False, help="Display code editor/viewer")
edit_mode = st.sidebar.toggle("✏️ Edit Mode", value=False, help="Enable code editing")

halt_edit = st.sidebar.toggle("🔒 Lock Edit", value=False, help="Prevent accidental code modifications")

if halt_edit and edit_mode:
    st.sidebar.warning("Edit mode disabled due to edit lock")
    edit_mode = False

# --- MAIN CONTENT AREA ---
if show_live_preview and show_code_panel:
    # Two-column layout
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 🔴 Live Preview")
        if current_code:
            st.components.v1.html(current_code, height=700, scrolling=True)
        else:
            st.info("No code to preview")
    
    with col2:
        st.markdown("### 📝 Code Editor/Viewer")
        if edit_mode and not halt_edit:
            edited_code = st.text_area(
                "Edit HTML/CSS Code:",
                value=current_code,
                height=600,
                help="Edit the code and see live preview updates"
            )
            if edited_code != current_code:
                current_code = edited_code
                st.rerun()
        else:
            st.code(current_code, language="html")

elif show_live_preview:
    # Live preview only (default)
    st.markdown("### 🔴 Live Preview")
    if current_code:
        st.components.v1.html(current_code, height=700, scrolling=True)
    else:
        st.info("No code to preview")

elif show_code_panel:
    # Code panel only
    st.markdown("### 📝 Code Editor/Viewer")
    if edit_mode and not halt_edit:
        edited_code = st.text_area(
            "Edit HTML/CSS Code:",
            value=current_code,
            height=600,
            help="Edit the code and see live preview updates"
        )
        if edited_code != current_code:
            current_code = edited_code
            st.rerun()
    else:
        st.code(current_code, language="html")

else:
    st.info("Enable Live Preview or Code Panel to view content")

# --- DOWNLOAD SECTION ---
st.markdown("---")
st.markdown("### 📥 Download Options")

col1, col2, col3 = st.columns(3)

with col1:
    if current_code and current_code.strip():
        pdf_data = generate_pdf_from_html(current_code, selected_row.get('Title', 'Document'))
        if pdf_data:
            st.download_button(
                label="📄 Download PDF",
                data=pdf_data,
                file_name=f"{selected_row.get('Title', 'document').replace(' ', '_')}.pdf",
                mime="application/pdf",
                help="Download as formatted PDF document"
            )
        else:
            if st.button("📄 Download PDF"):
                st.error("PDF generation requires reportlab package")
    else:
        st.write("")  # Empty space for alignment

with col2:
    # HTML download
    if current_code and current_code.strip():
        clean_html = clean_html_for_download(current_code)
        st.download_button(
            label="🌐 Download HTML",
            data=clean_html,
            file_name=f"{selected_row.get('Title', 'document').replace(' ', '_')}.html",
            mime="text/html",
            help="Download as HTML file with embedded CSS"
        )
    else:
        st.write("")  # Empty space for alignment

with col3:
    # Reset button for edit mode
    if edit_mode and not halt_edit:
        if st.button("🔄 Reset Code"):
            st.rerun()
    else:
        st.write("")  # Empty space for alignment

# --- STATUS BAR ---
st.markdown("---")
col1, col2, col3, col4 = st.columns(4)

with col1:
    if sheet_url and 'df' in locals() and not df.empty:
        st.metric("Total Entries", len(df))
    else:
        st.metric("Total Entries", 0)

with col2:
    if 'selected_row' in locals():
        st.metric("Current Category", selected_row.get('Category', 'N/A'))
    else:
        st.metric("Current Category", "N/A")

with col3:
    edit_status = "🔒 Locked" if halt_edit else ("✏️ Editing" if edit_mode else "👁️ Viewing")
    st.metric("Edit Status", edit_status)

with col4:
    preview_status = "🔴 Live" if show_live_preview else "📝 Code" if show_code_panel else "⚫ Hidden"
    st.metric("Preview Status", preview_status)

# --- INSTRUCTIONS ---
with st.expander("📖 Instructions & Tips", expanded=False):
    st.markdown(
        """
        **How to use this enhanced code viewer:**
        
        **Google Sheets Setup:**
        - Create a Google Sheet with your HTML/CSS code
        - Required columns: **Number**, **Code**
        - Optional columns: **Title**, **Category**, **Description**
        - Get the CSV export URL: File → Share → Publish to web → CSV format
        
        **Display Controls:**
        - **Live Preview**: View rendered HTML/CSS (ON by default)
        - **Show Code Panel**: Display code editor/viewer (OFF by default for cleaner view)
        - **Edit Mode**: Enable real-time code editing
        - **Lock Edit**: Prevent accidental modifications
        
        **Enhanced Features:**
        - **Category Filtering**: Filter entries by category
        - **Better Defaults**: Live preview on, code off for immediate visual impact
        - **Larger Preview**: Increased height for better viewing experience
        - **PDF Downloads**: Available for ALL entries, not just specific ones
        - **HTML Downloads**: Clean HTML with embedded CSS
        
        **Tips:**
        - Start with live preview to see the design immediately
        - Enable code panel only when you need to edit or study the code
        - Use edit lock to prevent accidental changes
        - Edit mode provides real-time preview updates
        """
    )

# --- FOOTER ---
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.8em;'>"
    "🚀 Enhanced Code Viewer | Google Sheets Integration | Real-time Editing | PDF Downloads for All"
    "</div>", 
    unsafe_allow_html=True
)
